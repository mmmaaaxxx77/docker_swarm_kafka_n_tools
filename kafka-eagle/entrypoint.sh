/opt/kafka-eagle/bin/ke.sh start
find /opt/kafka-eagle/logs -type f \( -name "*.log" \) -exec tail -f "$file" {} +