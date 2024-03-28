#!/bin/bash

# 默认搜索的文件类型为xml和java
file_extensions=".xml .java"

# 解析命令行参数
while getopts ":jx" opt; do
  case ${opt} in
    j )
      file_extensions=".java"
      ;;
    x )
      file_extensions=".xml"
      ;;
    \? )
      echo "Invalid option: $OPTARG" 1>&2
      exit 1
      ;;
    : )
      echo "Invalid option: $OPTARG requires an argument" 1>&2
      exit 1
      ;;
  esac
done
shift $((OPTIND -1))

# 检查是否提供了搜索字符串
if [ -z "$1" ]; then
  echo "Usage: $0 [-j|-x] <search_string>"
  exit 1
fi

# 记录搜索开始时间
start_time=$(date +%s)

# 执行grep命令搜索文件
search_string="$1"
project_path="./"  # 替换为你的Android项目路径
grep_result=$(grep -rnw "$project_path" -e "$search_string" --include=*{$file_extensions,txt})

# 记录搜索结束时间
end_time=$(date +%s)
search_time=$((end_time - start_time))

# 显示搜索结果
echo "$grep_result"

# 显示搜索时间
echo "Search time: $search_time seconds"
