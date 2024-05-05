json.extract! book_detail, :id, :Book_Name, :Author, :Price, :Mail_ID, :created_at, :updated_at
json.url book_detail_url(book_detail, format: :json)
