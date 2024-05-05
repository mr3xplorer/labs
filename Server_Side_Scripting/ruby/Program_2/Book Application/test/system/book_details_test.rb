require "application_system_test_case"

class BookDetailsTest < ApplicationSystemTestCase
  setup do
    @book_detail = book_details(:one)
  end

  test "visiting the index" do
    visit book_details_url
    assert_selector "h1", text: "Book details"
  end

  test "should create book detail" do
    visit book_details_url
    click_on "New book detail"

    fill_in "Author", with: @book_detail.Author
    fill_in "Book name", with: @book_detail.Book_Name
    fill_in "Mail id", with: @book_detail.Mail_ID
    fill_in "Price", with: @book_detail.Price
    click_on "Create Book detail"

    assert_text "Book detail was successfully created"
    click_on "Back"
  end

  test "should update Book detail" do
    visit book_detail_url(@book_detail)
    click_on "Edit this book detail", match: :first

    fill_in "Author", with: @book_detail.Author
    fill_in "Book name", with: @book_detail.Book_Name
    fill_in "Mail id", with: @book_detail.Mail_ID
    fill_in "Price", with: @book_detail.Price
    click_on "Update Book detail"

    assert_text "Book detail was successfully updated"
    click_on "Back"
  end

  test "should destroy Book detail" do
    visit book_detail_url(@book_detail)
    click_on "Destroy this book detail", match: :first

    assert_text "Book detail was successfully destroyed"
  end
end
