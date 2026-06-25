{% extends "layout.html" %}

{% block title %}
    TO-DO List
{% endblock %}

{% block main %}

    <!---Copyright (c) 2021 tcheng10@UIUC for CS411

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.-->

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.css">


    <body>

    <main role="main" class="todo-container extra-bottom">
      <h1 class="mt-5">TO-DO List</h1>
      <p><mark>Organize your tasks</mark></p>
    </main>


    <div class="todo-container">


        <div>
        <button type="button" class="btn btn-outline-info btn-sm" data-bs-toggle="modal" data-bs-target="#task-modal" data-source="New Task">Add Task</button>
        </div>


        <div class="modal fade" id="task-modal" tabindex="-1" aria-labelledby="Label" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="Label">Add a task</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body">
                <div class="input-group mb-3">
                    <span class="input-group-text" id="task-form-display">Task</span>
                    <input type="text" class="form-control" placeholder="Description of task" aria-label="task-name" aria-describedby="basic-addon1">
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button id="submit-task" type="button" class="btn btn-primary">Save changes</button>
            </div>
            </div>
        </div>
        </div>

    </div>


    <div class="todo-container table-responsive">
    <table class="table">
        <thead>
        <tr>
            <th class="task-id">#</th>
            <th class="task">Task Name</th>
            <th class="status">Status</th>
            <th class="update">Edit</th>
            <th class="update">Remove</th>
        </tr>
        </thead>

        <tbody>
        {% for item in items %}
            <tr>
                <td>{{item.id}}</td>
                <td>{{item.task}}</td>

                {% if item.status == "In Progress" %}
                    <td><button type="button" class="btn btn-outline-warning btn-sm state" data-source="{{item.id}}">{{item.status}}</button></td>
                {%endif%}
                {% if item.status == "Todo" %}
                    <td><button type="button" class="btn btn-outline-secondary btn-sm state" data-source="{{item.id}}">{{item.status}}</button></td>
                {%endif%}
                {% if item.status == "Complete" %}
                    <td><button type="button" class="btn btn-outline-success btn-sm state" data-source="{{item.id}}">{{item.status}}</button></td>
                {%endif%}

                <td><button type="button" class="btn btn-outline-info btn-sm" data-bs-toggle="modal" data-bs-target="#task-modal" data-source="{{item.id}}" data-content="{{item.task}}"><i class="fa fa-pen fa-1" aria-hidden="true"></i></button></td>

                <td><button class="btn btn-outline-secondary btn-sm remove" data-source="{{item.id}}" type="button"><i class="fa fa-trash fa-1" aria-hidden="true"></i></button></td>
            </tr>
        {% endfor %}

        </tbody>
    </table>
    </div>


  </body>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
    <script>
        $(document).ready(function () {

        $('#task-modal').on('show.bs.modal', function (event) {
            const button = $(event.relatedTarget)
            const taskID = button.data('source')
            const content = button.data('content')

            const modal = $(this)
            if (taskID === 'New Task') {
                modal.find('.modal-title').text(taskID)
                $('#task-form-display').removeAttr('taskID')
            } else {
                modal.find('.modal-title').text('Edit Task ' + taskID)
                $('#task-form-display').attr('taskID', taskID)
            }

            if (content) {
                modal.find('.form-control').val(content);
            } else {
                modal.find('.form-control').val('');
            }
        })


        $('#submit-task').click(function () {
            const tID = $('#task-form-display').attr('taskID');
            console.log($('#task-modal').find('.form-control').val())
            $.ajax({
                type: 'POST',
                url: tID ? '/edit/' + tID : '/create',
                contentType: 'application/json;charset=UTF-8',
                data: JSON.stringify({
                    'description': $('#task-modal').find('.form-control').val()
                }),
                success: function (res) {
                    console.log(res.response)
                    location.reload();
                },
                error: function () {
                    console.log('Error');
                }
            });
        });

        $('.remove').click(function () {
            const remove = $(this)
            $.ajax({
                type: 'POST',
                url: '/delete/' + remove.data('source'),
                success: function (res) {
                    console.log(res.response)
                    location.reload();
                },
                error: function () {
                    console.log('Error');
                }
            });
        });

        $('.state').click(function () {
            let state = $(this)
            let tID = state.data('source')
            let new_state = "Todo"
            if (state.text() === "In Progress") {
                new_state = "Complete"
            } else if (state.text() === "Complete") {
                new_state = "Todo"
            } else if (state.text() === "Todo") {
                new_state = "In Progress"
            }

            $.ajax({
                type: 'POST',
                url: '/edit/' + tID,
                contentType: 'application/json;charset=UTF-8',
                data: JSON.stringify({
                    'status': new_state
                }),
                success: function (res) {
                    console.log(res)
                    location.reload();
                },
                error: function () {
                    console.log('Error');
                }
            });
        });

    });
    </script>

    </body>
{% endblock %}