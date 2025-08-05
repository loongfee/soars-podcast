#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import requests
import tempfile
import yaml
import wave

def get_audio_metadata(url):
    """获取音频文件的元数据"""
    try:
        # 下载文件头部来获取基本信息
        response = requests.head(url, timeout=10)
        file_size = int(response.headers.get('content-length', 0))
        print("  File size: {} bytes".format(file_size))
        
        # 下载完整文件来获取时长（临时文件）
        print("  Downloading audio file...")
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
            response = requests.get(url, timeout=60)
            temp_file.write(response.content)
            temp_file.flush()
            temp_file_path = temp_file.name
            
        try:
            # 使用 wave 模块获取音频时长
            print("  Analyzing WAV file...")
            with wave.open(temp_file_path, 'rb') as wav_file:
                frames = wav_file.getnframes()
                sample_rate = wav_file.getframerate()
                duration_seconds = int(frames / sample_rate)
                duration_formatted = "{}:{:02d}".format(duration_seconds // 60, duration_seconds % 60)
                print("  Duration: {}".format(duration_formatted))
                return file_size, duration_formatted
                
        except Exception as e:
            print("  Error reading WAV file: {}".format(e))
            
        finally:
            # 手动删除临时文件
            try:
                os.unlink(temp_file_path)
            except:
                pass
        
        return file_size, None
        
    except Exception as e:
        print("Error processing {}: {}".format(url, e))
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
    
    print("Processing: {}".format(front_matter.get('title', 'Unknown')))
    
    # 获取音频元数据 - 只在字段不存在或为空时更新
    needs_length = 'length' not in front_matter or not front_matter['length']
    needs_duration = 'duration' not in front_matter or not front_matter['duration']
    
    if needs_length or needs_duration:
        file_size, duration = get_audio_metadata(front_matter['file'])
        
        if file_size and needs_length:
            front_matter['length'] = file_size
            print("  Updated length: {}".format(file_size))
        
        if duration and needs_duration:
            front_matter['duration'] = duration
            print("  Updated duration: {}".format(duration))
    else:
        print("  Skipping - metadata already exists")
    
    # 重新写入文件
    new_content = "---\n{}---\n{}".format(yaml.dump(front_matter, default_flow_style=False, allow_unicode=True, default_style=None), post_content)
    
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







