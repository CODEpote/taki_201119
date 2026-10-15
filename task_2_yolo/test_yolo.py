from ultralytics import YOLO

print("正在加载 YOLO 模型...")
model = YOLO("yolo11n.pt")

print("正在推理示例图片...")
results = model("https://ultralytics.com/images/bus.jpg")

print(f"推理成功！检测到 {len(results[0].boxes)} 个物体。")