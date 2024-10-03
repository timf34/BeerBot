# BeerBot

<table>
  <tr>
    <td><img src="assets/BeerBotMascot.png" alt="BeerBot Mascot" width="250"/></td>
    <td><img src="assets/ExampleWhatsAppMessage.png" alt="WhatsApp Message Example" width="250"/></td>
  </tr>
</table>

**BeerBot**, your personal pint poet and pub-inviting Python bot!

## Contributions 

Please add more pubs! 

A headless version would be great too. 

## Installation

1. Clone this repository.
2. Install the required packages with `pip install -r requirements.txt`.
3. Follow automation instructions below. 

### Automating BeerBot with Task Scheduler (Windows)

To run BeerBot automatically, you can use the Task Scheduler in Windows with the `windows_scheduler.bat` script. 

1. Replace the path to this project with your local path in the `windows_scheduler.bat` script.
2. Open Task Scheduler
3. In the right hand panel, select "Create Basic Task" and give it a name.
4. Choose the frequency and time you want the task to run.
5. Choose "Start a program", select the `windows_scheduler.bat` script and "Finish".

However else you might choose to automate it, the script currently needs access to the browser (no headless mode yet). 