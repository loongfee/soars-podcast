require 'net/http'
require 'uri'

Jekyll::Hooks.register :posts, :pre_render do |post|
  if post.data['file']
    # 获取文件大小
    begin
      uri = URI(post.data['file'])
      response = Net::HTTP.start(uri.host, uri.port, use_ssl: uri.scheme == 'https') do |http|
        http.head(uri.path)
      end
      
      if response['content-length']
        post.data['length'] = response['content-length'].to_i
      end
    rescue => e
      puts "Error getting file size for #{post.data['title']}: #{e.message}"
    end
  end
end