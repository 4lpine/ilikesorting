from flask import Flask, render_template, request, redirect, url_for
import time

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bubble', methods=['GET', 'POST'])
def bubble():
    if request.method == 'POST':
        numbers = request.form['numbers']
        numbers_list = list(map(int, numbers.split(',')))
        steps = []

        for i in range(len(numbers_list)):
            for j in range(len(numbers_list) - 1):
                if numbers_list[j] > numbers_list[j + 1]:
                    numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
                    # Append a step-by-step description
                    steps.append(numbers_list[:])  # Make a copy of the current state of numbers_list

        return render_template('bubble.html', sorted_numbers=numbers_list, steps=steps)
    
    return render_template('bubble.html')


@app.route('/insertion', methods=['GET', 'POST'])
def insertion():
    if request.method == 'POST':
        numbers = request.form['numbers']
        numbers_list = list(map(int, numbers.split(',')))
        steps = []

        for i in range(1, len(numbers_list)):
            key = numbers_list[i]
            j = i - 1
            while j >= 0 and key < numbers_list[j]:
                numbers_list[j + 1] = numbers_list[j]
                j -= 1
            numbers_list[j + 1] = key
            steps.append(numbers_list[:])  # Append a copy of current state

        return render_template('insertion.html', sorted_numbers=numbers_list, steps=steps)
    
    return render_template('insertion.html')


@app.route('/merge', methods=['GET', 'POST'])
def merge():
    if request.method == 'POST':
        numbers = request.form['numbers']
        numbers_list = list(map(int, numbers.split(',')))
        steps = [numbers_list[:]]
        def merge_sort(arr, steps):
            if len(arr) > 1:
                mid = len(arr) // 2
                L = arr[:mid]
                R = arr[mid:]

                merge_sort(L, steps)
                merge_sort(R, steps)

                i=j=k=0

                while i < len(L) and j < len(R):
                    if L[i] < R[j]:arr[k] = L[i];i += 1
                    else:arr[k] = R[j];j += 1
                    k += 1

                while i < len(L):arr[k] = L[i];i += 1;k += 1
                while j < len(R):arr[k] = R[j];j += 1;k += 1


                steps.append(arr[:])
        
        merge_sort(numbers_list, steps)
        
        return render_template('merge.html', sorted_numbers=numbers_list, steps=steps)
    
    return render_template('merge.html')


@app.route('/selection', methods=['GET', 'POST'])
def selection():
    if request.method == 'POST':
        numbers = request.form['numbers']
        numbers_list = list(map(int, numbers.split(',')))
        steps = []

        for i in range(len(numbers_list)):
            min_idx = i
            for j in range(i + 1, len(numbers_list)):
                if numbers_list[j] < numbers_list[min_idx]:
                    min_idx = j
            numbers_list[i], numbers_list[min_idx] = numbers_list[min_idx], numbers_list[i]
            steps.append(numbers_list[:])  # Append a copy of current state

        return render_template('selection.html', sorted_numbers=numbers_list, steps=steps)
    
    return render_template('selection.html')

app.run(debug=True)