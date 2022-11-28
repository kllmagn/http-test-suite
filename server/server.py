import os
import queue
import signal
import socket
import threading

from .handler import handle
from .consts import *


class WorkThread(threading.Thread):
    def __init__(self, work_queue):
        super().__init__()
        self.work_queue = work_queue
        self.daemon = True

    def run(self):
        while True:
            func, args = self.work_queue.get()
            func(*args)
            self.work_queue.task_done()


class ThreadPoolManger(): # Класс для управления пулом потоков
    def __init__(self, thread_number):
        self.thread_number = thread_number # Количество потоков
        self.work_queue = queue.Queue() # Очередь задач
        for _ in range(self.thread_number): # Создание потоков
            thread = WorkThread(self.work_queue)
            thread.start()

    def add_work(self, func, *args): # Добавление задачи в очередь
        self.work_queue.put((func, args))


def run_server(cpu_count=DEFAULT_CPU_COUNT, thread_limit=DEFAULT_THREAD_LIMIT, document_root=DEFAULT_DIR, host=DEFAULT_HOST, port=DEFAULT_PORT):
    cpu_count = min(cpu_count, DEFAULT_CPU_COUNT) # ограничение на число процессов
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind((host, port))
    conn.listen()
    print(f"Сервер запущен: {host}:{port}")
    pids = []
    try:
        for _ in range(cpu_count):
            pid = os.fork() # Создаем дочерний процесс
            if pid != 0:
                print(f"Новый форк, pid = {pid}")
                pids.append(pid)
                thread_pool = ThreadPoolManger(thread_limit)
                while True:
                    sock, _ = conn.accept()
                    thread_pool.add_work(handle, *(sock, document_root))
    except KeyboardInterrupt:
        conn.close()
        for pid in pids: # Отправляем сигнал SIGTERM дочерним процессам
            print(f"Остановка форка, pid = {pid}")
            os.kill(pid, signal.SIGTERM) # Останавливаем дочерний процесс
        print("Сервер остановлен")
