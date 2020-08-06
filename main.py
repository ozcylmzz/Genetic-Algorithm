import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib as mpl

k = 3 # Toplam yiyecek sayısı
m = 15 # Toplam hamle sayısı
n = 7 # Oluşturulan kare dünyanın boyutu
yolsayisi = 10 # Populasyonun büyüklüğü
iter = 0 # Nesil sayısı


def creatPath():
    # 1 left
    # 2 up
    # 3 right
    # 4 down
    # In the code below, we select 5 random integers from the range of 1 to 100.

    # Satır sayısı toplam yol sayısı (yolsayisi), sütun sayısı ise toplam hamle
    # sayısı +1 (m+1) olan bir matris rastgele oluşturulur.

    path = [[0 for x in range(m+1)] for y in range(yolsayisi)]
    for l in range(0, yolsayisi):
        randnums = np.random.randint(1, 5, m + 1)
        randnums[m] = 0
        path[l] = randnums
    return path


def Fitness(Matrix, path):

    # Fitness() fonksiyonu 2 parametre alır:
    # 1) Matrix: oluşturulan dünya
    # 2) path: Bireyin izleyeceği yolu saklayan dizi

    # Yola uygun şekilde birey hareket ettirilerek matrisi gezmesi sağlanır.
    # Her adımda bireyin yaşayıp yaşamadığı isAlive() fonksiyonu ile kontrol edilir.
    # Birey duvara çarparsa path dizisi sıfırlanır.
    # Birey yiyeceğe rastlarsa path dizinin son hanesi 1 arttırılır.
    # Oluşan matrisin durumu print_function() fonksiyonu ile yazdırılır.

    j,k = int(n/2),int(n/2)
    matrix = Matrix
    for i in range(0,m):
        if path[i] == 1:
            matrix[j][k] = 0
            k = k -1
            if isAlive(j,k) == True:
                if matrix[j][k] == 1:
                    path[m] += 1
                matrix[j][k] = -1
            else:
                path = [0 for x in range(m+1)]

        if path[i] == 2:
            matrix[j][k] = 0
            j = j - 1
            if isAlive(j, k) == True:
                if matrix[j][k] == 1:
                    path[m] += 1
                matrix[j][k] = -1
            else:
                path = [0 for x in range(m+1)]

        if path[i] == 3:
            matrix[j][k] = 0
            k = k + 1
            if isAlive(j, k) == True:
                if matrix[j][k] == 1:
                    path[m] += 1
                matrix[j][k] = -1
            else:
                path = [0 for x in range(m+1)]

        if path[i] == 4:
            matrix[j][k] = 0
            j = j + 1
            if isAlive(j, k) == True:
                if matrix[j][k] == 1:
                    path[m] += 1
                matrix[j][k] = -1
            else:
                path = [0 for x in range(m+1)]
        # print_function(matrix, n, iter)

    return path


def Fitness2(Matrix, path):

    # Fitness() fonksiyonu ile aynı işlemi yapmaktadır. Fakat karşılaşılan bir
    # sorundan dolayı ihtiyaç duyulmuştur.

    j,k = int(n/2),int(n/2)
    matrix = Matrix
    for i in range(0,m):
        if path[i] == 1:
            matrix[j][k] = 0
            k = k -1
            if isAlive(j,k) == True:
                matrix[j][k] = -1
            else:
                path = [0 for x in range(m+1)]

        if path[i] == 2:
            matrix[j][k] = 0
            j = j - 1
            if isAlive(j, k) == True:
                matrix[j][k] = -1
            else:
                path = [0 for x in range(m+1)]

        if path[i] == 3:
            matrix[j][k] = 0
            k = k + 1
            if isAlive(j, k) == True:
                matrix[j][k] = -1
            else:
                path = [0 for x in range(m+1)]

        if path[i] == 4:
            matrix[j][k] = 0
            j = j + 1
            if isAlive(j, k) == True:
                matrix[j][k] = -1
            else:
                path = [0 for x in range(m+1)]
        print_function(matrix, n, iter)

    return path

def isAlive(j,k):

    # Bireyin yaşayıp yaşamadığını kontrol eder. Eğer duvarlara çarpmışsa False döndürür.

    if (0 <= j and j < n and 0 <= k and k <n):
        return True
    else:
        return False

def selection(path):

    # selection() fonksiyonu 1 parametre alır:
    # 1) path: yolların tutulduğu matris
    # Bireylerin topladığı yiyecek sayısına göre path matrisi sıralanır.
    # Bireylerin seçilme olasılıkları hesaplanıp probablity dizisine alınır.
    # random.choices(path,probabilty,k=yolsayisi) fonksiyonu ile bir sonraki
    # nesli oluşturacak bireyler seçilip path matrisine atanır.

    sum = 0
    probabilty = [0 for x in range(yolsayisi)]
    for i in range(0,yolsayisi):
        sum += path[i][m]
    if sum == 0:
        return -1
    for i in range(0,yolsayisi):
        probabilty[i] = path[i][m]/sum*10
    # print(probabilty)
    path = random.choices(path,probabilty,k=yolsayisi)
    # print('sa',path)
    return path

def crossover(path):

    # crossover() fonksiyonu 1 parametre alır:
    # 1) path: yolların tutulduğu matris
    # selection() fonksiyonu ile seçilen bireyler arasında çaprazlama uygulanır.
    # Çaprazlama yapılırken rastgele belirlenen bir noktadan bölünürler.

    new_path = [[0 for x in range(m+1)] for y in range(yolsayisi)]
    line = int(np.random.randint(0, m, 1))
    for i in range(0,int(yolsayisi/2)):
        new_path[2 * i][:line] = path[2*i][:line]
        new_path[2 * i][line:] = path[2*i+1][line:]
        new_path[2 * i][m] = 0
        new_path[2 * i+1][:line] = path[2 * i+1][:line]
        new_path[2 * i+1][line:] = path[2 * i][line:]
        new_path[2* i+1][m] = 0
    # print('sa',path)
    print('new_path',new_path)
    return new_path

def mutation(path):

    # mutation() fonksiyonu 1 parametre alır:
    # 1) path: yolların tutulduğu matris
    # mutation() fonksiyonu ile rastgele seçilen bireylere mutasyon uygulanır.
    # Belirlenen oran kadar (0,1) uygulanan mutasyon rastgele değerlerin değişmesi ile yapılır.

    prob = int(0.1 * yolsayisi * m)
    for i in range(0,prob):
        path[int(np.random.randint(0, yolsayisi, 1))][int(np.random.randint(0, m, 1))] = int(np.random.randint(1, 5, 1))
    return path

def initMatrix(n,k):
    Matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(0,k):
        while True:
            j = int(np.random.randint(0, n, 1))
            l = int(np.random.randint(0, n, 1))
            if(Matrix[j][l] == 0):
                Matrix[j][l] = 1
                break
    return Matrix

def print_function(Matrix, n, generation_number):

    # Matrisin, bireyin ve yiyeceklerin o anki durumunu görselleştirmek için kullanılan fonksiyondur.

    mpl.style.use('default')
    matfig = plt.figure(figsize=(8, 8))
    plt.matshow(Matrix, fignum=matfig.number)
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, n, 1))
    ax.set_yticks(np.arange(-.5, n, 1))
#    ax.set_color_cycle("black")
    ax.grid(which='both', color="black")
    plt.suptitle(generation_number, fontsize=40)
    plt.show(block=False)

    plt.pause(0.1)
    plt.close()


# Matrix: Oluşturulan kare dünya. Matrise yiyecek atamaları yapılır.
# Bu matriste;
#   bireyin bulunduğu pozisyon (-1) ile,
#   yiyecekler (1) ile,
#   diğer kareler ise (0) ile gösterilir.

# itsDone değişkeni 0 olarak başlatılır. Program bu değişken 0 olduğu sürece
# devam edecek bir döngüye girer.
    # path = creatPath() ile başlangıç matrisi oluştulur.
    # Bu işlemler belirlenen iterasyon sayısı kadar aşağıdaki işlemler tekrar edilir.
        # Yol sayısı kadar devam eden döngüde her birey için
        # Fitness() fonksiyonu çağırılarak uygunluğu hesaplanır.
        # selection() fonksiyonu ile sonraki nesli oluşturmaya uygun olan bireyler seçilir.
        # crossover() fonksiyonu ile seçilen bireyler arasında çaprazlama yapılır.
        # Belirlenen orana göre bireyler mutasyona uğratılır.
        # Bireyler arasında tüm yiyecekleri yiyen varsa başlangıçta 0 olarak belirlenen
        # itsDone. Bu sayede dış döngüden çıkması sağlanır.
    # Program sonlanmadan sonucun bulunduğu jenerasyonun bilgisi ve
    # sonucu bulan bireyin izlediği yol yazdırılır.
# Böylece programın bir sonuç bulana kadar çalışması sağlanır.


itsDone = 0
while itsDone != 1:
    path = creatPath()
    iter = 0
    while iter !=1000:
        print(iter)

        print('before',path)
        for i in range(0, yolsayisi):
            Matrix = [[0 for x in range(n)] for y in range(n)]
            Matrix[int(n/2)][int(n/2)] = -1
            Matrix[5][3] = 1
            Matrix[1][6] = 1
            Matrix[6][4] = 1
            path[i] = Fitness(Matrix, path[i])
            if (path[i][m] == k):
                itsDone = 1
                print('as',path[i])


                Matrix2 = [[0 for x in range(n)] for y in range(n)]
                Matrix2[int(n/2)][int(n/2)] = -1
                Matrix2[5][3] = 1
                Matrix2[1][6] = 1
                Matrix2[6][4] = 1
                Fitness2(Matrix2, path[i])


                break
        if itsDone == 1:
            print('Hepsi yendi',path[i])
            break
        path = sorted(path, key=lambda path_entry: path_entry[m])
        print('after',path)
        path = selection(path)
        if path == -1:
            break
        path = crossover(path)
        path = mutation(path)
        iter += 1
