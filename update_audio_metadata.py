#!/usr/bin/env python3
import os
import re
import requests
from mutagen import File
import tempfile
import yaml

def get_audio_metadata(url):
    """获取音频文件的元数据"""
    try:
        # 下载文件头部来获取基本信息
        response = requests.head(url, timeout=10)
        file_size = int(response.headers.get('content-length', 0))
        
        # 下载完整文件来获取时长（临时文件）
        with tempfile.NamedTemporaryFile() as temp_file:
            response = requests.get(url, timeout=30)
            temp_file.write(response.content)
            temp_file.flush()
            
            # 使用 mutagen 获取音频时长
            audio_file = File(temp_file.name)
            if audio_file and audio_file.info:
                duration_seconds = int(audio_file.info.length)
                duration_formatted = f"{duration_seconds // 60}:{duration_seconds % 60:02d}"
                return file_size, duration_formatted
            
        return file_size, None
        
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return None, None

def update_post_metadata(file_path):
    """更新单个文章的元数据"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取 front matter
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        return False
    
    front_matter_str, post_content = match.groups()
    front_matter = yaml.safe_load(front_matter_str)
    
    if 'file' not in front_matter:
        return False
    
    print(f"Processing: {front_matter.get('title', 'Unknown')}")
    
    # 获取音频元数据
    file_size, duration = get_audio_metadata(front_matter['file'])
    
    if file_size:
        front_matter['length'] = file_size
        print(f"  Updated length: {file_size}")
    
    if duration:
        front_matter['duration'] = duration
        print(f"  Updated duration: {duration}")
    
    # 重新写入文件
    new_content = f"---\n{yaml.dump(front_matter, default_flow_style=False, allow_unicode=True)}---\n{post_content}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    """处理所有文章"""
    posts_dir = '_posts'
    
    if not os.path.exists(posts_dir):
        print("_posts directory not found!")
        return
    
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(posts_dir, filename)
            update_post_metadata(file_path)

if __name__ == "__main__":
    main()