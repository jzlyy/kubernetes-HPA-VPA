from locust import HttpUser, task, between
import random

class QuickTestUser(HttpUser):
    wait_time = between(1, 3)  # 更紧凑的等待时间
    
    # 设置目标域名（命令行优先级更高）
    host = "http://your-website.com"  

    def on_start(self):
        """可选：每个用户启动时的初始化（如登录）"""
        # 示例：获取认证token
        resp = self.client.post("/login", json={
            "user": "test",
            "pwd": "123"
        })
        self.token = resp.json().get("token")

    @task(3)  # 高频任务
    def test_homepage(self):
        # 带随机参数的GET请求示例
        pages = ["/", "/about", "/contact"]
        self.client.get(
            url=random.choice(pages),
            headers={"User-Agent": "Locust/QuickTest"}
        )

    @task(2)  # 中频任务
    def search_action(self):
        # 带查询参数的请求
        self.client.get(
            url="/search",
            params={"q": random.choice(["book", "movie", "music"])}
        )

    @task(1)  # 低频任务
    def submit_form(self):
        # POST请求示例（自动处理Content-Type）
        self.client.post(
            url="/submit",
            json={
                "name": f"User{random.randint(1,100)}",
                "value": random.uniform(10, 100)
            },
            headers={"Authorization": f"Bearer {self.token}"}  # 使用初始化获取的token
        )
