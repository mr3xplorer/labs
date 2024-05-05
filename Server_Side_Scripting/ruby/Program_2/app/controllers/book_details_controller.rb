class BookDetailsController < ApplicationController
  before_action :set_book_detail, only: %i[ show edit update destroy ]

  # GET /book_details or /book_details.json
  def index
    @book_details = BookDetail.all
  end

  # GET /book_details/1 or /book_details/1.json
  def show
  end

  # GET /book_details/new
  def new
    @book_detail = BookDetail.new
  end

  # GET /book_details/1/edit
  def edit
  end

  # POST /book_details or /book_details.json
  def create
    @book_detail = BookDetail.new(book_detail_params)

    respond_to do |format|
      if @book_detail.save
        format.html { redirect_to book_detail_url(@book_detail), notice: "Book detail was successfully created." }
        format.json { render :show, status: :created, location: @book_detail }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @book_detail.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /book_details/1 or /book_details/1.json
  def update
    respond_to do |format|
      if @book_detail.update(book_detail_params)
        format.html { redirect_to book_detail_url(@book_detail), notice: "Book detail was successfully updated." }
        format.json { render :show, status: :ok, location: @book_detail }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @book_detail.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /book_details/1 or /book_details/1.json
  def destroy
    @book_detail.destroy!

    respond_to do |format|
      format.html { redirect_to book_details_url, notice: "Book detail was successfully delete." }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_book_detail
      @book_detail = BookDetail.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def book_detail_params
      params.require(:book_detail).permit(:Book_Name, :Author, :Price, :Mail_ID)
    end
end
