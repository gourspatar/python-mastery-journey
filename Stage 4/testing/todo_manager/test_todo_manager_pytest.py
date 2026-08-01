import pytest
from todo_manager import TodoManager


@pytest.fixture
def todo():
    return TodoManager()


def test_add_task(todo):
    todo.add_task("Python")
    assert len(todo.tasks) == 1


def test_add_multiple_tasks(todo):
    todo.add_task("Python")
    todo.add_task("Git")
    assert len(todo.tasks) == 2


def test_add_duplicate_task(todo):
    todo.add_task("Python")

    with pytest.raises(ValueError):
        todo.add_task("Python")


def test_add_empty_task(todo):
    with pytest.raises(ValueError):
        todo.add_task("")


def test_remove_existing_task(todo):
    todo.add_task("Python")
    todo.remove_task("Python")
    assert len(todo.tasks) == 0


def test_remove_missing_task(todo):
    with pytest.raises(ValueError):
        todo.remove_task("Java")


def test_mark_completed(todo):
    todo.add_task("Python")
    todo.mark_completed("Python")
    assert todo.tasks[0]["completed"] is True


def test_mark_completed_missing_task(todo):
    with pytest.raises(ValueError):
        todo.mark_completed("Java")


def test_pending_tasks(todo):
    todo.add_task("Python")
    todo.add_task("Git")
    assert todo.pending_tasks() == ["Python", "Git"]


def test_pending_after_completion(todo):
    todo.add_task("Python")
    todo.mark_completed("Python")
    assert todo.pending_tasks() == []


def test_remove_completed_task(todo):
    todo.add_task("Python")
    todo.mark_completed("Python")
    todo.remove_task("Python")
    assert len(todo.tasks) == 0


def test_task_in_pending(todo):
    todo.add_task("Python")
    assert "Python" in todo.pending_tasks()


def test_completed_not_pending(todo):
    todo.add_task("Python")
    todo.mark_completed("Python")
    assert "Python" not in todo.pending_tasks()


def test_add_three_tasks(todo):
    todo.add_task("A")
    todo.add_task("B")
    todo.add_task("C")
    assert len(todo.tasks) == 3


def test_all_completed(todo):
    todo.add_task("A")
    todo.add_task("B")
    todo.mark_completed("A")
    todo.mark_completed("B")
    assert todo.pending_tasks() == []