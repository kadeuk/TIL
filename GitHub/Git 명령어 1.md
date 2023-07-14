### Git 이란
---
1. Git은 분산 버전 관리 시스템이다.
	- 분산 버전 관리 시스템이란 여러 사용자가 공동으로 사용하는 코드의 다양한 버전을 추적하고 관리하는 소프트웨어 도구다. 이런 시스템은 개발자들이 서로의 작업을 병합하고, 과거의 특정 버전으로 되돌아 갈수 있는 기능을 제공한다.
2. Git은 로컬과 원격 저장소에서 작동하고, 변경 사항을 commit하고 push함으로써 코드의 버전을 관리한다.
	- commit은 Git에서 작업 내용을 스탭샷처럼 기록하는 것이다. 이를 통해 파일의 변경사항을 추적하며, 각 commit은 프로젝트의 특정 버전을 의미한다.
3. Git은 여러 사람이 동시에 작업 할때 서로의 작업을 병합하고 충돌을 해결하는 기능을 제공한다.

### Git 명령어
`git [명령어]`

1. `git init`
- Git으로 코드 관리를 시작
- Git에서 새로운 저장소(repository)를 만드는 명령어
- 명령어 실행시 '.git'라는 서브디렉토리가 생성됨.
- 저장소의 모든 정보(버전기록, 설정등)가 저장됨.
- 'git init'은 프로젝트를 처음 시작할 때 한 번만 실행.

2. `git status`
- 현재 상태를 출력(Git에게 현재 상태를 물어봄)

- `git init`직후
```git
On branch master -> master라는 브랜치 위에 있어요. 

No commits yet -> 아직 commit이 없어요. 

nothing to commit (create/copy files and use "git add" to track) -> commit할 것이 없어요.

```

- `touch a.txt`파일 추가후, `git status`
```git
$ touch a.txt
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt

nothing added to commit but untracked files present (use "git add" to track)


```

- `git add a.txt` 직후 `git status`
```git
$ git add a.txt
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt
-> commit할 변경들이 있어요

```

- `git commit`이후
```git
nothing to commit, working tree clean -> commit 할 게 없어요. 작업 폴더는 깔끔해요.
```

- 파일 수정후,
```git
On branch master Changes not staged for commit: 
-> commit하기 위해 stage 되지 않은 변경 사항이 있어요. 
	(use "git add ..." to update what will be committed) 
	(use "git restore ..." to discard changes in working directory)
		modified: test.txt 

no changes added to commit (use "git add" and/or "git commit -a")
```


3. `git add [파일명]`
commit을 위한 stage 
`git add .` : 현재 폴더의 모든 변경 사항 stage


- working directory(wd) 작업중인 폴더 (~/intro)(a.txt를 만들고 `git add`하기)
	- Stage(git add를 하면 여기로 간다)(`git rm cached` 을 하면 다시 working 으로) 여기있는 상태를 사진으로 찍는 행위를 `commit`이라고 한다. 사진을 찍으면 Commit Log로 이동 `git commit`
		- Commit Log(버전 리스트, 로그)(사진찍은 후에 여기로 이동)


4. `git commit -m '커밋메시지'`
>사진을 찍어서 commit log로 이동시키기

- 처음으로 commit을 할 경우
```git
Author identity unknown -> 작자미상 

*** Please tell me who you are. -> 당신이 누군지 알려주세요. 

Run -> 아래의 명령어를 실행주세요. 

	git config --global user.email "you@example.com" 
	git config --global user.name "Your Name"
```

5. `git config`최초에 이메일과, 이름을 설정하기
```git
$ git config --global user.email "이메일"
$ git config --global user.name "이름"
```

6. `git log`
현재까지의 commit을 출력
- `git log`출력화면
```git
commit 1a7d9384d2f9a064e2ddb4719306defeb51ac3cf (HEAD -> master) Author: John Kang -> 작성자 
Date: Tue Mar 16 15:55:10 2021 +0900 -> 날짜 

first commit -> 커밋 메시지
```

- `git log --oneline`
한줄로 출력
```git
7c7abf0 (HEAD -> master) Add title 1a7d938 first commit
```

7. `git remote`
- git remote add [저장소이름] [저장소주소] : git remote add origin https://github.com/hkeryf onttlxisdrlw/basic_git 
	- git에게 원격저장소(remote) 추가(add)를 명령 
- 저장소이름: origin 
- 저장소주소: https://github.com/hkeryfonttlxisdrlw/basic_git

8. `git pull [원격 저장소 이름][브랜치명]`
- 원격 저장소의 변경사항을 로컬 저장소로 가져옴
- 성공시 "Already up to date"또는 새로운 변경사항이 적용된 메시지 출력

9. `git push [원격 저장소 이름][브랜치명]`
- 로컬 저장소의 변경사항을 원격 저장소에 업로드
- 성공시 "Everything up-to-date" 또는 변경사항이 적용된 메시지가 출력

10. `git branch [브랜치명]`
- 새로운 브랜치 만들기
- 성공시 별도의 메시지 출력안함

11. `git checkout [브랜치명]`
- 특정 브랜치로 이동
- 성공시 "Switched to branch [브랜치명]" 메시지가 출력
  