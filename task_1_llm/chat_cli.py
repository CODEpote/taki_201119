import requests

def chat_with_ollama(prompt, model="qwen2.5:7b"):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    try:
        # 【关键修改1】绕过 Clash 代理，直接访问本地服务
        proxies = {"http": None, "https": None}
        response = requests.post(url, json=payload, proxies=proxies)
        response.raise_for_status()
        return response.json()['message']['content']
    except Exception as e:
        return f"出错啦: {e}，请确保 Ollama 在运行且模型已下载！"

if __name__ == "__main__":
    print("===== 本地大模型 CLI 聊天机器人 =====")
    print("输入 quit 或 exit 退出程序")
    
    while True:
        user_input = input("\n你: ")
        if user_input.lower() in ['quit', 'exit']:
            print("再见！")
            break
        
        reply = chat_with_ollama(user_input)
        print(f"AI: {reply}")