class CreateBookDetails < ActiveRecord::Migration[7.1]
  def change
    create_table :book_details do |t|
      t.string :Book_Name
      t.string :Author
      t.decimal :Price
      t.string :Mail_ID

      t.timestamps
    end
  end
end
