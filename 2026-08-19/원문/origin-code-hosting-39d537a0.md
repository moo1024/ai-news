# Origin Code Hosting

- 출처: Cursor 체인지로그
- 원본 링크: https://cursor.com/changelog/origin-code-hosting
- 발행: 2026-08-17T00:00:00+00:00
- 접근상태: 확인 완료

---

Origin 코드 호스팅 · Cursor 콘텐츠로 건너뛰기 Cursor 모델 Grok Composer Evals 제품 ↓ 에이전트 클라우드 모바일 자동화 CLI 마켓플레이스  ↗ 리뷰 기업 요금제 리소스 ↓ Changelog Blog 문서 커뮤니티 도움말  ↗ 워크숍 포럼  ↗ 채용 모델  → 제품  → 기업 요금제 리소스  → 로그인 문의하기 영업팀에 문의하기 다운로드 2026년 8월 17일  ·  Changelog 
 Changelog Origin 코드 호스팅 이제 Cursor에서 코드를 호스팅할 수 있습니다.

 Origin은 오늘부터 모든 유료 플랜에 초기 베타로 순차 출시됩니다. 에이전트 규모에 맞춰 설계된 핵심 기능인 repo, 풀 리퀘스트, 코드 탐색, GitHub 동기화부터 시작합니다. Agent 네이티브 기능도 곧 제공될 예정입니다.

 
 # Origin Repos 
 새로운 Codebase 탭에서 Origin repo를 관리할 수 있습니다.

 +New 을 클릭하고 이름을 지정하세요. 그러면 CLI 설치 방법과 repo를 clone하거나 로컬 프로젝트를 push하는 명령어를 안내하는 페이지가 표시됩니다. push하면 코드가 Origin에 호스팅됩니다.

 
 첫 번째 repo를 만들 때 codebase 이름을 지정하세요. 이 이름은 모든 repo의 URL 일부가 됩니다: cursor.com/codebase/ acme-corp .

 # GitHub repo 가져오기 
 GitHub repo를 Cursor에서 호스팅하는 repo와 함께 사용할 수 있습니다. GitHub를 Cursor에 연결하고 org를 선택하면 동기화할 수 있는 repo가 표시됩니다. 하나를 선택하면 Cursor가 가져옵니다. 동기화할 항목을 선택할 수 있으며 언제든 repo 연결을 해제할 수 있습니다. 동기화된 repo에 대한 읽기 또는 쓰기 접근 권한이 있는 모든 사용자는 Cursor에서도 해당 repo를 볼 수 있습니다.

 동기화된 repo는 실시간으로 업데이트됩니다. Origin의 복사본에서 찾아보고, 검색하고, pull할 수 있습니다. push는 계속 GitHub로 전송되며, GitHub에서 시작한 모든 작업의 소스 오브 트루스는 GitHub로 유지됩니다. 각 repo 이름 옆의 아이콘은 Cursor에서 호스팅하는 repo와 GitHub에서 가져온 repo를 구분해 줍니다.

 
 # 풀 리퀘스트 
 모든 repo에는 풀 리퀘스트가 있습니다. 풀 리퀘스트를 열어 타임라인, 커밋, 검사 결과, 변경된 파일을 확인하세요. diff를 검토하고 댓글을 남긴 다음 병합하세요.

 
 동기화된 repo의 풀 리퀘스트는 양방향으로 동기화됩니다. Cursor에서 댓글을 남기면 GitHub에 게시되고, GitHub에서 반응을 남기거나 답글을 달면 몇 초 내에 Cursor에 표시됩니다. GitHub에서 나에게 할당된 검토가 있나요? Cursor에서 검토하고 병합하세요.

 
 # 모든 repo에서 Agent 사용 
 이제 코드, PR, 에이전트를 한곳에서 관리할 수 있습니다. 살펴보는 코드 সম্পর্কে Cursor에 질문하세요. 답변을 받거나, 변경 사항을 적용하고, PR을 업데이트하거나 브랜치를 푸시할 수 있습니다.

 
 # Cursor repo용 앱 확장 기능 
 전체 스택이 Origin과 매끄럽게 연동되도록 앱 생태계를 구축하고 있습니다. Vercel, Depot, Buildkite 통합은 이미 사용할 수 있으며, 더 많은 통합도 곧 제공될 예정입니다.

 repo의 앱 탭에서 Vercel을 연결하면 모든 PR에 테스트하고 댓글을 남길 수 있는 미리보기 배포가 제공됩니다. 병합하면 프로덕션에 배포합니다. CI에는 Depot 또는 Buildkite를 연결하세요. 둘 다 기존 GitHub Actions 워크플로우를 실행하며, Buildkite는 자체 네이티브 파이프라인도 실행합니다.

 
 # 설정 
 모든 repo에는 설정이 있습니다. GitHub repo의 동기화 상태를 확인하고, 접근 권한이 있는 사용자를 관리하며, 연결된 앱을 확인하세요.

 
 오늘부터 Origin이 유료 플랜의 모든 사용자에게 초기 베타로 제공됩니다. 단, 관리자가 옵트아웃한 기업 org는 제외됩니다. codebase의 이름을 지정하고 첫 repo를 만드세요.

 문서 에서 자세히 알아보거나 오늘 시작하세요 .
 다음 게시물 → 빌드로 클라우드 Agent 시작 속도 3배 향상 제품 에이전트 Teams 기업 요금제 코드 리뷰 CLI 클라우드 Agent Composer 마켓플레이스  ↗ 리소스 다운로드 Changelog 문서 알아보기  ↗ 가치 계산기 포럼  ↗ 도움말  ↗ 워크숍 상태  ↗ 기업 채용 Blog 커뮤니티 학생 브랜드 미래 Anysphere  ↗ 법률 서비스 약관 허용 가능한 사용 정책 개인정보 처리방침 데이터 사용 보안 연결하다 X  ↗ LinkedIn  ↗ YouTube  ↗ © 2026 Anysphere, Inc. 🛡 SOC 2 인증 🌐 한국어 ↓ English 简体中文 日本語 繁體中文 Español Français Português 한국어 ✓ Deutsch हिन्दी 콘텐츠로 건너뛰기 Cursor 모델 Grok Composer Evals 제품 ↓ 에이전트 클라우드 모바일 자동화 CLI 마켓플레이스  ↗ 리뷰 기업 요금제 리소스 ↓ Changelog Blog 문서 커뮤니티 도움말  ↗ 워크숍 포럼  ↗ 채용 모델  → 제품  → 기업 요금제 리소스  → 로그인 문의하기 영업팀에 문의하기 다운로드 2026년 8월 17일  ·  Changelog 
 Changelog Origin 코드 호스팅 이제 Cursor에서 코드를 호스팅할 수 있습니다.

 Origin은 오늘부터 모든 유료 플랜에 초기 베타로 순차 출시됩니다. 에이전트 규모에 맞춰 설계된 핵심 기능인 repo, 풀 리퀘스트, 코드 탐색, GitHub 동기화부터 시작합니다. Agent 네이티브 기능도 곧 제공될 예정입니다.

 
 # Origin Repos 
 새로운 Codebase 탭에서 Origin repo를 관리할 수 있습니다.

 +New 을 클릭하고 이름을 지정하세요. 그러면 CLI 설치 방법과 repo를 clone하거나 로컬 프로젝트를 push하는 명령어를 안내하는 페이지가 표시됩니다. push하면 코드가 Origin에 호스팅됩니다.

 
 첫 번째 repo를 만들 때 codebase 이름을 지정하세요. 이 이름은 모든 repo의 URL 일부가 됩니다: cursor.com/codebase/ acme-corp .

 # GitHub repo 가져오기 
 GitHub repo를 Cursor에서 호스팅하는 repo와 함께 사용할 수 있습니다. GitHub를 Cursor에 연결하고 org를 선택하면 동기화할 수 있는 repo가 표시됩니다. 하나를 선택하면 Cursor가 가져옵니다. 동기화할 항목을 선택할 수 있으며 언제든 repo 연결을 해제할 수 있습니다. 동기화된 repo에 대한 읽기 또는 쓰기 접근 권한이 있는 모든 사용자는 Cursor에서도 해당 repo를 볼 수 있습니다.

 동기화된 repo는 실시간으로 업데이트됩니다. Origin의 복사본에서 찾아보고, 검색하고, pull할 수 있습니다. push는 계속 GitHub로 전송되며, GitHub에서 시작한 모든 작업의 소스 오브 트루스는 GitHub로 유지됩니다. 각 repo 이름 옆의 아이콘은 Cursor에서 호스팅하는 repo와 GitHub에서 가져온 repo를 구분해 줍니다.

 
 # 풀 리퀘스트 
 모든 repo에는 풀 리퀘스트가 있습니다. 풀 리퀘스트를 열어 타임라인, 커밋, 검사 결과, 변경된 파일을 확인하세요. diff를 검토하고 댓글을 남긴 다음 병합하세요.

 
 동기화된 repo의 풀 리퀘스트는 양방향으로 동기화됩니다. Cursor에서 댓글을 남기면 GitHub에 게시되고, GitHub에서 반응을 남기거나 답글을 달면 몇 초 내에 Cursor에 표시됩니다. GitHub에서 나에게 할당된 검토가 있나요? Cursor에서 검토하고 병합하세요.

 
 # 모든 repo에서 Agent 사용 
 이제 코드, PR, 에이전트를 한곳에서 관리할 수 있습니다. 살펴보는 코드 সম্পর্কে Cursor에 질문하세요. 답변을 받거나, 변경 사항을 적용하고, PR을 업데이트하거나 브랜치를 푸시할 수 있습니다.

 
 # Cursor repo용 앱 확장 기능 
 전체 스택이 Origin과 매끄럽게 연동되도록 앱 생태계를 구축하고 있습니다. Vercel, Depot, Buildkite 통합은 이미 사용할 수 있으며, 더 많은 통합도 곧 제공될 예정입니다.

 repo의 앱 탭에서 Vercel을 연결하면 모든 PR에 테스트하고 댓글을 남길 수 있는 미리보기 배포가 제공됩니다. 병합하면 프로덕션에 배포합니다. CI에는 Depot 또는 Buildkite를 연결하세요. 둘 다 기존 GitHub Actions 워크플로우를 실행하며, Buildkite는 자체 네이티브 파이프라인도 실행합니다.

 
 # 설정 
 모든 repo에는 설정이 있습니다. GitHub repo의 동기화 상태를 확인하고, 접근 권한이 있는 사용자를 관리하며, 연결된 앱을 확인하세요.

 
 오늘부터 Origin이 유료 플랜의 모든 사용자에게 초기 베타로 제공됩니다. 단, 관리자가 옵트아웃한 기업 org는 제외됩니다. codebase의 이름을 지정하고 첫 repo를 만드세요.

 문서 에서 자세히 알아보거나 오늘 시작하세요 .
 다음 게시물 → 빌드로 클라우드 Agent 시작 속도 3배 향상 제품 에이전트 Teams 기업 요금제 코드 리뷰 CLI 클라우드 Agent Composer 마켓플레이스  ↗ 리소스 다운로드 Changelog 문서 알아보기  ↗ 가치 계산기 포럼  ↗ 도움말  ↗ 워크숍 상태  ↗ 기업 채용 Blog 커뮤니티 학생 브랜드 미래 Anysphere  ↗ 법률 서비스 약관 허용 가능한 사용 정책 개인정보 처리방침 데이터 사용 보안 연결하다 X  ↗ LinkedIn  ↗ YouTube  ↗ © 2026 Anysphere, Inc. 🛡 SOC 2 인증 🌐 한국어 ↓ English 简体中文 日本語 繁體中文 Español Français Português 한국어 ✓ Deutsch हिन्दी