## Welcome App

This is a simple Rails application that greets users based on the input username.

### Getting Started

1. Create a new Rails application:

    ```bash
    rails new welcome_app
    ```

2. Navigate to the newly created directory:

    ```bash
    cd welcome_app
    ```

3. Create necessary folders and files:

    - Create a new folder `welcome_username` inside `app/controllers`.
    - Inside `welcome_username`, create a file named `welcome_controller.rb`.
    - Create a folder `views/welcome`.
    - Inside `views/welcome`, create two files: `index.html.erb` and `greet.html.erb`.
    - Modify the `routes.rb` file.

### Controller

Create a new controller `welcome_controller.rb`:

```ruby
# app/controllers/welcome_username/welcome_controller.rb

class WelcomeController < ApplicationController
  def index
  end

  def greet
    @username = params[:username]
  end 
end
```

### Views

#### `index.html.erb`

```erb
<!-- app/views/welcome/index.html.erb -->

<h1>Welcome to the Welcome username app!</h1>
<%= form_tag welcome_greet_path, method: :get do %>
  <%= label_tag :username, "Enter your name:" %>
  <%= text_field_tag :username %>
  <%= submit_tag "GO" %>
<% end %>
```

#### `greet.html.erb`

```erb
<!-- app/views/welcome/greet.html.erb -->

<h1>Hello! <%= @username %></h1>
<p>Thank you for using the welcome username app</p>
```

### Routes

Modify the `routes.rb` file to include the routes:

```ruby
# config/routes.rb

Rails.application.routes.draw do
  root 'welcome#index'
  get '/welcome/greet', to: 'welcome#greet', as: 'welcome_greet'
end
```

### Running the Application

Start the Rails server:

```bash
rails server
```

Access the application in your browser at `http://localhost:3000`.

### Notes

- Make sure you replace `welcome_username` with your desired username throughout the codebase.
