# CatCafe
Студенческий проект Python, посвящённый реализации настольной игры "Котокафе". Для учебной практики.

## Правила игры
В данной игре участвуют от 2 до 4 игроков. Игра состоит из раундов, правила раундов описаны ниже. В конце игры побеждает игрок с наибольшим количеством очков.

### Комплектность
* 100 листов игроков (в программе неограниченны)
* 4 карандаша (в программе отсутствуют)
* 5 кубиков

### Ход игры
Каждый раунд игры состоит из трёх фаз:
* Выбор кубиков
* Рисование
* Проверка кошачьих башен

После третьей фазы проверяют, есть ли игрок, у которого заполнены 3 кошачьих башни. Если есть, начинается подсчёт очков. Иначе начинается следующий раунд.

#### 1 фаза - выбор кубиков
В этой фазе:
1. Первый игрок бросает кубики в середине стола (в программе бросает компьютер)
2. Начиная с первого игрока и далее по часовой стрелке каждый игрок выбирает один из кубиков
3. После того как все игроки выберут по кубику, на столе останется один кубик. Он будет называться центральным.

После этого наступает следующая фаза.

#### 2 фаза - рисование
Каждый игрок может нарисовать предмет в свободную ячейку игрового листа или пропустить ход.

Чтобы нарисовать предмет, игрок выбирает кубик (свой или центральный), чьё значение определяет предмет. Оставшийся кубик определяет этаж. Также игрок выбирает столбец (башню), где будет нарисован предмет.

Когда все игроки нарисовали предметы или пропустили ход, наступает следующая фаза.

#### 3 фаза - проверка кошачьих башен
В этой фазе игроки проверяют, есть ли новые заполненные столбцы. Если есть, игрокам начисляются очки. Если есть игрок, имеющий 3 заполненных столбца, начинается подсчёт очков. 

### Подсчёт очков
Подсчёт идёт следующим образом:
* Подсчитываются очки за предметы (в зависимости от их свойств)
* К очкам прибавляются очки за башни.

Игрок(и), набравшие наибольшее количество очков, побеждают.

#### Свойства предметов
* Кошачий домик - (не определено)
* Клубок ниток - в каждой башне: игрок(и) с наибольшим количеством клубков - 8 очков, остальные игроки с клубками - 3 очка
* Игрушка-бабочка - каждый предмет приносит 3 очка
* Миска с кормом - каждая миска: 1 очко за каждый уникальный соседний предмет
* Подушка - каждая подушка: количество очков равно номеру этажу расположения
* Игрушка-мышь - приносят очки за цепи:
  * 1 мышь - 2 очка
  * 2 мыши - 6 очков
  * 3 мыши - 12 очков
  * 4 мыши - 20 очков.

## Пример текстового интерфейса игры
Играют Alice и Bob. Показан раунд игры.

```
Server: Раунд 4
Server: Фаза 1
Alice: Кубики: 4 6 3
Alice: Выберите кубик: 6
-----
Bob: Кубики: 4 3
Bob: Выберите кубик: 3
Server: Центральный кубик: 4
-----
Server: Фаза 2
Server: Центральный кубик: 4
Alice: Кубик: 6
Alice:
          7/3           
     9/5   |   8/4      
6/4   |   6__   |       
 |   6__   |   6__      
5__   |   5__   |   3/2 
 |   5__   |   5__   |  
 |    |   4__   |   4__ 
 |   4__   |   4__   |  
3_M   |    |    |   3__ 
 |   3__   |   3__   |  
2__   |   2_B   |    |  
 |   2_D   |   2__   |  
1__   |   1__   |   1__ 
 |   1__   |   1__   |  
 |    |    |    |    |  
 =    =    =    =    =
Alice: Выберите столбец: 4
Alice: Выберите действие: DISH на 6 этаж (1) или MOUSE на 4 этаж (2): 2
-----
Bob: Кубик: 3
Bob:
          7/3           
     9/5   |   8/4      
6/4   |   6__   |       
 |   6__   |   6__      
5__   |   5__   |   3/2  
 |   5__   |   5__   |  
 |    |   4_Y   |   4__ 
 |   4__   |   4_H   |  
3__   |    |    |   3__ 
 |   3__   |   3__   |  
2__   |   2_M   |    |  
 |   2__   |   2__   |  
1__   |   1__   |   1__ 
 |   1__   |   1__   |  
 |    |    |    |    |  
 =    =    =    =    =
Bob: Выберите столбец: 2
Bob: Выберите действие: DISH на 3 этаж (1) или BUTTERFLY на 4 этаж (2): 1
-----
Server: Фаза 3
Server: Новых заполненных столбцов не обнаружено!
Server: Раунд закончен.
```

## Формат save-файла
```json
{
  "round_g": 4,
  "phase": 3,
  "turn": 0,
  "dices": "4",
  "players": [
    {
      "name": "Alice",
      "dice": 6,
      "score": 0,
      "house": [
        "I I I I I I I I",
        "I E E M I E I I",
        "I E D E E E E I",
        "I E B I E E E I",
        "I E E E M E E I",
        "I E I E E I I I",
        "I I I I I I I I"
      ],
      "kind": "Human"
    },
    {
      "name": "Bob",
      "dice": 3,
      "score": 0,
      "house": [
        "I I I I I I I I",
        "I E E E I E I I", 
        "I E E D E E E I", 
        "I E M I Y E E I", 
        "I E E E H E E I", 
        "I E I E E I I I",
        "I I I I I I I I"
      ],
      "kind": "DummyAI"
    }
  ]
}
```
