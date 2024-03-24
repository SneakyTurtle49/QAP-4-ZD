//description: this part of the code contains all the calculations and prompts so the user can input
//information into the terminal and will print the results there as well
//author: Zac Davidge
//date: 3/22/2024

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const prompt = (query) => new Promise((resolve) => rl.question(query, resolve));

async function createMotelCustomer() {

  //prompt for customer details

  const name = await prompt("Enter customer's name: ");
  const birthDate = await prompt("Enter customer's birth date (YYYY-MM-DD): ");
  const gender = await prompt("Enter customer's gender: ");
  const roomPreferences = await prompt("Enter room preferences (comma-separated): ").then(input => input.split(', '));
  const paymentMethod = await prompt("Enter payment method: ");
  const street = await prompt("Enter mailing address street: ");
  const city = await prompt("Enter mailing address city: ");
  const province = await prompt("Enter mailing address province: ");
  const zip = await prompt("Enter mailing address zip code: ");
  const phoneNumber = await prompt("Enter phone number: ");
  const checkInDate = await prompt("Enter check-in date (YYYY-MM-DD): ");
  const checkOutDate = await prompt("Enter check-out date (YYYY-MM-DD): ");
  
  rl.close();

  //Return an object with methods for calculations and description

  return {
    name,
    birthDate,
    gender,
    roomPreferences,
    paymentMethod,
    mailingAddress: { street, city, province, zip },
    phoneNumber,
    checkInDate,
    checkOutDate,
    calculateAge: function() {
      const today = new Date();
      const birthDate = new Date(this.birthDate);
      let age = today.getFullYear() - birthDate.getFullYear();
      const monthDiff = today.getMonth() - birthDate.getMonth();
      if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
      }
      return age;
    },
    calculateStayDuration: function() {
      const checkInDate = new Date(this.checkInDate);
      const checkOutDate = new Date(this.checkOutDate);
      const timeDiff = checkOutDate.getTime() - checkInDate.getTime();
      const days = Math.ceil(timeDiff / (1000 * 3600 * 24));
      return days;
    },
    customerDescription: function() {
      return `
        Customer Name: ${this.name}
        Age: ${this.calculateAge()}
        Gender: ${this.gender}
        Room Preferences: ${this.roomPreferences.join(", ")}
        Payment Method: ${this.paymentMethod}
        Mailing Address: ${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.province} ${this.mailingAddress.zip}
        Phone Number: ${this.phoneNumber}
        Check-In Date: ${this.checkInDate}
        Check-Out Date: ${this.checkOutDate}
        Stay Duration: ${this.calculateStayDuration()} days
      `;
    }
  };
}

async function main() {
  const motelCustomer = await createMotelCustomer();
  console.log(motelCustomer.customerDescription());
}

main();
