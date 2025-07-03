# features/steps/pitch_steps.py
from behave import given, when, then
from fastapi.testclient import TestClient
from app.main import app

@given("教練已準備好一段投球影片")
def step_given_ready_video(context):
    context.client = TestClient(app)
    context.video_path = "test.mp4"
    with open(context.video_path, "wb") as f:
        f.write(b"FAKE VIDEO CONTENT")  # 建立假影片

@when("教練上傳該影片至系統")
def step_when_upload_video(context):
    with open(context.video_path, "rb") as f:
        response = context.client.post("/upload", files={"file": f})
    context.response = response

@then("系統應回傳 landing frame 資訊")
def step_then_check_response(context):
    assert context.response.status_code == 200
    json_data = context.response.json()
    assert "landing_frame" in json_data
    assert "x" in json_data["landing_frame"]
    assert "y" in json_data["landing_frame"]
