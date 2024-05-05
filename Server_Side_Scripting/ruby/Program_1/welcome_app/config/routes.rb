Rails.application.routes.draw do
  root 'welcome#index'  # This sets the root path to the index action of WelcomeController
  get '/welcome/greet', to: 'welcome#greet', as: 'welcome_greet'
end