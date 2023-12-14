# Diskret_comand_task(Звіт)

4. Функція strong_coherence_oriented отримує на вхід граф у вигляді словника та шукає компоненти сильної зв’язності за допомогою алгоритму Косараджу.
Містить в собі три підфункції, а саме: dfs та dfs_scc (створює порядок в stack), transpose (перетворює граф).
Алгоритм працює наступним чином:
  1) Кожній вершині надається значення visited = False
  2) Проходиться dfs по графу доти поки кожна вершина не буде мати значення True, вершини додаються в stack
  3) Перетворюється граф за допомогою функції transpose(напрямки ребер міняються в протилежну сторону)
  4) Знову кожній вершині (тепер з transposed_graph) надається значення visited = False
  5) Виконується цикл (поки в stack є елементи), який проходиться dfs_scc по новому графу і додає пройдені вершини в component, який вкінці циклу архівується в dict і додається в результат.

6. Функція search_for_bridges приймає словник з графом і повертає список з усіма мостами цього графу. Спочатку створюється два списки res і edges після цього в edges записуємо всі ребра графу без повторень. Потім знаходимо найменшу і найбільшу вершину графу. І робимо копію списку для редагування в майбутньому. Після цього проходимося по всім ребрам в списку edges, після чого видаляємо ребро зі списку edges_copy і передаємо його функції find_path, якщо вона повертає False то додаємо це ребро в результат.
Функція find_path перевіряє, чи існує шлях від заданої вершини до іншої у графі. Вона приймає кількість вершин n, список ребер edges, початкову вершину source та кінцеву вершину destination, створює граф, використовуючи словник, де ключі - це вершини, а значення - списки сусідніх вершин. Використовуємо рекурсивну функцію neighbor_search, яка шукає шлях з початкової вершини до кінцевої. Повертаємо значення True, якщо шлях існує, та False у протилежному випадку.
