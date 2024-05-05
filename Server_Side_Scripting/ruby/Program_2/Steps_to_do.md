## Book Application

This is a Rails application for managing book details using a scaffold for BookDetail.

### Getting Started

1. Create a new Rails application named `book`:

    ```bash
    rails new book
    ```

2. Navigate to the newly created directory:

    ```bash
    cd book
    ```

3. Generate the scaffold for BookDetail:

    ```bash
    rails generate scaffold BookDetail Book_Name:string Author:string Price:decimal Mail_ID:string
    ```

4. Create the database:

    ```bash
    rake db:create
    ```

5. Migrate the database:

    ```bash
    rake db:migrate
    ```

### Code Modifications

#### `app/views/book_details/_book_detail.html.erb`

```erb
<div id="<%= dom_id book_detail %>">
  <p>
    <strong>Book name:</strong>
    <%= book_detail.Book_Name %>
  </p>

  <p>
    <strong>Author:</strong>
    <%= book_detail.Author %>
  </p>

  <p>
    <strong>Price:</strong>
    <%= book_detail.Price %>
  </p>

  <p>
    <strong>Mail id:</strong>
    <%= book_detail.Mail_ID %>
  </p>
</div>
```

#### `app/views/book_details/edit.html.erb`

```erb
<h1>Editing book detail</h1>

<%= render "form", book_detail: @book_detail %>

<br>

<div>
  <%= link_to "Show", @book_detail %> |
  <%= link_to "Back", book_details_path %>
</div>
```

#### `app/views/book_details/index.html.erb`

```erb
<p style="color: green"><%= notice %></p>

<h1>Book details</h1>

<div id="book_details">
  <% @book_details.each do |book_detail| %>
    <%= render book_detail %>
    <p>
      <%= link_to "Show", book_detail %>
    </p>
  <% end %>
</div>

<%= link_to "New", new_book_detail_path %>
```

#### `app/views/book_details/new.html.erb`

```erb
<h1>New book detail</h1>

<%= render "form", book_detail: @book_detail %>

<br>

<div>
  <%= link_to "Back", book_details_path %>
</div>
```

#### `app/views/book_details/show.html.erb`

```erb
<p style="color: green"><%= notice %></p>

<%= render @book_detail %>

<div>
  <%= link_to "Edit", edit_book_detail_path(@book_detail) %> |
  <%= link_to "Back", book_details_path %>

  <%= button_to "Delete", @book_detail, method: :delete %>
</div>
```

#### `config/routes.rb`

```ruby
Rails.application.routes.draw do
  resources :book_details
  get "up" => "rails/health#show", as: :rails_health_check

  root "book_details#index"
end
```

### Running the Application

1. Start the Rails server:

    ```bash
    rails server
    ```

2. Browse the page at [http://127.0.0.1:3000](http://127.0.0.1:3000).
