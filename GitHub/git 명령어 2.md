
1. `git clone <repository-url> <folder name>`
`git clone`은 원격 저장소의 repository를 로컬 스시템으로 복사하는 데 사용되는 Git명령어다.

2. `git pull origin master `
`git pull`은 원격 저장소의 수정 내용을 로컬 시스템으로 복사하는 데 사용된다.

3. `git checkout`
Git에서 특정 브랜치나 커밋으로 이동하는데 사용되는 명령어다. 브랜치를 변경하거나, 이전의 커밋 상태로 되돌아갈 때 사용된다.
```bash
$ git checkout branch_name
Switched to branch 'branch_name'
```

4. `git branch`
브랜치를 생성, 삭제 , 이름 변경하거나 리스트를 확인하는데 사용된다. 
```bash
$ git branch new_branch
```

5. `git merge`
두 브랜치의 변경 사항을 합치는데 사용된다. 현재 작업 중인 브랜치에 대른 브랜치의 변경 사항을 적용할 때 사용된다.
```bash
$ git merge source_branch
Updating a3775a..ba6f76f
Fast-forward
 example.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

6. `git stash`
작업중인 변경사항을 임시로 저장하는데 사용된다. 아직 커밋하지 않은 변경사항을 저장하고, 깨끗한 작업 디렉토리로 돌아갈때 유용하다. 
```bash
$ git stash
Saved working directory and index state WIP on main: ba6f76f Add example.txt
```

7. `git diff`
두 커밋이나 브랜치에서의 차이점을 보여주는데 사용된다. 특정 파일의 변경 사항을 확인하거나 , 전체 프로젝트에 대한 변경 사항을 확인할 때 사용된다.
```bash
$ git diff
diff --git a/example.txt b/example.txt
index 22054cd..0d4f250 100644
--- a/example.txt
+++ b/example.txt
@@ -1 +1 @@
-Hello, world!
+Hello, Git!
```