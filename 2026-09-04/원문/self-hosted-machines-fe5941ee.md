# Self-hosted machines

- 출처: Cursor 체인지로그
- 원본 링크: https://cursor.com/changelog/self-hosted-machines
- 발행: 2026-09-02T00:00:00+00:00
- 접근상태: 확인 완료

---

셀프 호스팅 machines · Cursor 콘텐츠로 건너뛰기 Cursor 모델 ↓ Grok Evals 제품 ↓ 에이전트 클라우드 Grok 봇  ↗ 모바일 자동화 CLI 마켓플레이스  ↗ 리뷰 기업 요금제 리소스 ↓ Changelog Blog 문서 커뮤니티 도움말  ↗ 워크숍 포럼  ↗ 채용 모델  → 제품  → 기업 요금제 리소스  → 로그인 문의하기 영업팀에 문의하기 다운로드 2026년 9월 2일  ·  Changelog 
 Changelog 셀프 호스팅 machines Cursor는 도구 실행을 전적으로 자체 네트워크 안에서 처리할 수 있는 셀프 호스팅 machines 을 지원합니다.

 코드베이스, 빌드 산출물, 시크릿은 모두 여러분의 인프라에서 실행되는 내부 머신에 그대로 유지되며, 도구 호출은 에이전트가 로컬에서 처리합니다.

 
 # 동적 pool scheduling 
 My Machines 는 개인 워크플로우를 위해 노트북이나 VM 한 대를 계정에 연결하는 기능입니다.

 Team pools 는 팀 또는 기업을 위해 이름을 지정한 worker 대기열입니다. 요청이 들어오면 역량이 늘어나고 worker 연결이 끊기면 줄어들기 때문에, 셀프 호스팅 machines를 수요에 맞춰 확장할 수 있습니다. Pools는 특정 리포지토리에 묶여 있지 않습니다. pool 이름만 지정하면 사용 가능한 worker 중 어느 것이든 해당 요청을 가져갈 수 있습니다.

 또한 Pools는 유휴 machine을 최대 절전 상태로 전환했다가, 후속 요청이 들어오면 재연결 window 내에 복원할 수 있습니다. 덕분에 다음 prompt 하나를 위해 비용이 많이 드는 역량을 계속 켜 둘 필요가 없습니다.

 
 # 내 샌드박스에서 실행 
 이제 클라우드 Agent를 이미 사용 중인 인프라 에서 실행할 수 있습니다. AWS Lambda, Coder, Cloudflare, Daytona, Modal, Namespace, Vercel, E2B를 지원합니다.

 # Linux 및 Mac에서의 컴퓨터 사용 
 셀프 호스팅 worker가 이제 Linux와 Mac에서 컴퓨터 사용을 지원합니다. 적절한 데스크톱 패키지만 갖춰져 있으면 에이전트가 클릭하고, 입력하고, 스크린샷을 찍고, 브라우저를 조작할 수 있습니다. 에이전트의 데스크톱을 지켜보거나 Cursor에서 직접 제어권을 가져올 수도 있습니다.
 다음 게시물 → repo 없이 Start from scratch 제품 에이전트 Teams 기업 요금제 코드 리뷰 CLI 클라우드 Agent Composer 마켓플레이스  ↗ 리소스 다운로드 Changelog 문서 알아보기  ↗ 가치 계산기 포럼  ↗ 도움말  ↗ 워크숍 상태  ↗ 기업 채용 Blog 커뮤니티 학생 브랜드 미래 Anysphere  ↗ 법률 서비스 약관 허용 가능한 사용 정책 Grok 봇 이용약관 개인정보 처리방침 데이터 사용 보안 연결하다 X  ↗ LinkedIn  ↗ YouTube  ↗ © 2026 Anysphere, Inc. 🛡 SOC 2 | ISO27001 | ISO42001 | AIUC-1 인증 🌐 한국어 ↓ English 简体中文 日本語 繁體中文 Español Français Português 한국어 ✓ Deutsch हिन्दी 콘텐츠로 건너뛰기 Cursor 모델 ↓ Grok Evals 제품 ↓ 에이전트 클라우드 Grok 봇  ↗ 모바일 자동화 CLI 마켓플레이스  ↗ 리뷰 기업 요금제 리소스 ↓ Changelog Blog 문서 커뮤니티 도움말  ↗ 워크숍 포럼  ↗ 채용 모델  → 제품  → 기업 요금제 리소스  → 로그인 문의하기 영업팀에 문의하기 다운로드 2026년 9월 2일  ·  Changelog 
 Changelog 셀프 호스팅 machines Cursor는 도구 실행을 전적으로 자체 네트워크 안에서 처리할 수 있는 셀프 호스팅 machines 을 지원합니다.

 코드베이스, 빌드 산출물, 시크릿은 모두 여러분의 인프라에서 실행되는 내부 머신에 그대로 유지되며, 도구 호출은 에이전트가 로컬에서 처리합니다.

 
 # 동적 pool scheduling 
 My Machines 는 개인 워크플로우를 위해 노트북이나 VM 한 대를 계정에 연결하는 기능입니다.

 Team pools 는 팀 또는 기업을 위해 이름을 지정한 worker 대기열입니다. 요청이 들어오면 역량이 늘어나고 worker 연결이 끊기면 줄어들기 때문에, 셀프 호스팅 machines를 수요에 맞춰 확장할 수 있습니다. Pools는 특정 리포지토리에 묶여 있지 않습니다. pool 이름만 지정하면 사용 가능한 worker 중 어느 것이든 해당 요청을 가져갈 수 있습니다.

 또한 Pools는 유휴 machine을 최대 절전 상태로 전환했다가, 후속 요청이 들어오면 재연결 window 내에 복원할 수 있습니다. 덕분에 다음 prompt 하나를 위해 비용이 많이 드는 역량을 계속 켜 둘 필요가 없습니다.

 
 # 내 샌드박스에서 실행 
 이제 클라우드 Agent를 이미 사용 중인 인프라 에서 실행할 수 있습니다. AWS Lambda, Coder, Cloudflare, Daytona, Modal, Namespace, Vercel, E2B를 지원합니다.

 # Linux 및 Mac에서의 컴퓨터 사용 
 셀프 호스팅 worker가 이제 Linux와 Mac에서 컴퓨터 사용을 지원합니다. 적절한 데스크톱 패키지만 갖춰져 있으면 에이전트가 클릭하고, 입력하고, 스크린샷을 찍고, 브라우저를 조작할 수 있습니다. 에이전트의 데스크톱을 지켜보거나 Cursor에서 직접 제어권을 가져올 수도 있습니다.
 다음 게시물 → repo 없이 Start from scratch 제품 에이전트 Teams 기업 요금제 코드 리뷰 CLI 클라우드 Agent Composer 마켓플레이스  ↗ 리소스 다운로드 Changelog 문서 알아보기  ↗ 가치 계산기 포럼  ↗ 도움말  ↗ 워크숍 상태  ↗ 기업 채용 Blog 커뮤니티 학생 브랜드 미래 Anysphere  ↗ 법률 서비스 약관 허용 가능한 사용 정책 Grok 봇 이용약관 개인정보 처리방침 데이터 사용 보안 연결하다 X  ↗ LinkedIn  ↗ YouTube  ↗ © 2026 Anysphere, Inc. 🛡 SOC 2 | ISO27001 | ISO42001 | AIUC-1 인증 🌐 한국어 ↓ English 简体中文 日本語 繁體中文 Español Français Português 한국어 ✓ Deutsch हिन्दी