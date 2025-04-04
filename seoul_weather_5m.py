#서울 기온 정보를 5분마다 수집하여 csv로 저장

name : Fetch Seoul Weather Data per 5m

on: 
  schedule:
    - cron: "*/5 * * * *"
  workflow_dispatch:
jobs:
  fetch_weather_seoul_5m:
    runs-on: ubuntu-latest

    steps:
      - name: 저장소 체크아웃
        uses: actions/checkout@v3 #현재 git 저장소 가져오기
        with:
         token: ${{secrets.GITHUB_TOKEN}}
      - name: Python 설정
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"

      - name: 필요한 패키지 설치
        run: pip install requests

      - name: 날씨 데이터 가져오기
        env:
          OPENWEATHER_API_KEY: ${{secrets.OPENWEATHER_API_KEY}}
        run: python seoul_weather_5m.py

      - name: 변경 사항 커밋 및 푸시
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions@github.com"
          git add seoul_weather.csv
          git commit -m "Update weather data (auto)"
          git push 
         
  
