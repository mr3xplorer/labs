Rails.application.routes.draw do
  resources :book_details
  get "up" => "rails/health#show", as: :rails_health_check
   root "book_details#index"
end
