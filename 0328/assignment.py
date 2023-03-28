# Todo ORM 실습
# 1. 할 일 생성
'''
content: 실습 제출
priority: 5
completed: False
deadline: 오늘 날짜(년-월-일)
'''
Todo.objects.create(content='실습 제출', priority=5, completed=False, deadline='2023-03-28')


# 2. 아래 할 일 생성
'''
  content: 데일리 설문(오후) 제출
  deadline: 오늘 날짜(년-월-일)
'''
Todo.objects.create(content='데일리 설문(오후) 제출', deadline='2023-03-28')


# 3. 임의의 할 일 5개 생성
Todo.objects.create(content='알고리즘 문제 풀이', deadline='2023-03-28')
Todo.objects.create(content='TIL 작성', deadline='2023-03-28')
Todo.objects.create(content='요가', deadline='2023-03-28')

todo = Todo()
todo.content = '넷플릭스 명상 4편 보기'
todo.deadline = '2023-03-28'
todo.save()

todo = Todo(content='만달로리안 시즌3 보기', deadline='2023-04-01')
todo.save()


# 4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
target = Todo.objects.order_by('pk').values()
for element in target:
    print(element)


# 5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
target = Todo.objects.order_by('-priority').values()
for element in target:
    print(element)


# 6. pk가 1인 단일 데이터의 아래 필드 조회
# (pk, content, priority, deadline, created_at)
target = Todo.objects.filter(pk=1).values('pk', 'content', 'priority', 'deadline', 'created_at')
for element in target:
    print(element)


# 신문 Model & ORM
# 1. pk 필드가 1인 단일 데이터의 journalist 필드 조회
Newspaper.objects.get(pk=1)


# 2. journalist 필드가 Laney Mccullough인 데이터 개수 조회
Newspaper.objects.filter(journalist__exact='Laney Mccullough').count()


# 3. pk 필드 기준 내림차순으로 정렬한 모든 데이터 조회
Newspaper.objects.order_by('-pk')


# 4. created_at 필드 기준 내림차순으로 정렬한 모든 데이터 조회
Newspaper.objects.order_by('-created_at')


# 5. journalist 필드가 Britney를 포함하는 데이터 개수 조회
Newspaper.objects.filter(journalist__contains='Britney').count()


# 6. journalist 필드가 ['Britney Mahoney', 'Arianna Walls', 'Carl Short']에 속하는 데이터 개수 조회
Newspaper.objects.filter(journalist__in=['Britney Mahoney', 'Arianna Walls', 'Carl Short']).count()


# 7. created_at 필드가 2000-01-01 이후 데이터 개수 조회
Newspaper.objects.filter(created_at__gt='2000-01-01').count()


# 8. 마지막 단일 데이터의 title, content, journalist 필드를 조회하고 아래와 같은 형식으로 출력
# title : Teach father within million consumer baby its.
# content : Then member effort want site. Radio represent yard bag fine. Congress movie ten along.
# Hand receive agree science present main. Other member every.
# journalist : Laney Mccullough
target = Newspaper.objects.all().order_by('-pk').values()[0]
target_field = ['title', 'content', 'journalist']
for field in target_field:
    for key, value in target.items():
        if field == key:
            print(f'{key}: {value}')
