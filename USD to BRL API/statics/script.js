// script.js
document.addEventListener('DOMContentLoaded', () => {
   const exchangeRateElement = document.getElementById('exchangeRate');
   const refreshButton = document.getElementById('refreshButton');
 
   refreshButton.addEventListener('click', async () => {
      console.log('Button clicked');
      try {
        const response = await fetch('/get_exchange_rate');
        const data = await response.json();
        console.log('Data received:', data);
        exchangeRateElement.textContent = data.exchangeRate;
      } catch (error) {
        console.error('Fetch error:', error);
      } 
   });  
 });
 