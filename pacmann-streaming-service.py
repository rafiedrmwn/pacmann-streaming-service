# import the library
from tabulate import tabulate

# input data/dummy data here as dict
user_data = {
    'rafie_d': ['Basic plan', 14, 'rafie-149328'],
    'bret_di': ['Premium plan', 12, 'bret-24932'],
    'tuma_tumtum': ['Basic plan', 10, 'tuma-39410'],
    'marsha_a': ['Standard plan', 13, 'marsha-12309'],
    'tikiww': ['Standard plan', 15, 'tikiw-gembul'],
    'bo_cil': ['Basic plan', 19, 'bocil-kecil']
}

#create class User to give the solution
class User:
  # check the benefit:
  def check_benefit(self):
    # create the headers
    headers = ['Basic Plan', 'Standard Plan', 'Premium Plan', 'Benefit']

    # put the data
    tables = [
             ['Yes', 'Yes', 'Yes', "Stream"],
             ['Yes', 'Yes', 'Yes', "Download"],
             ['Yes', 'Yes', 'Yes', "SD Quality"],
             ['', 'Yes', 'Yes', "HD Quality"],
             ['', '', 'Yes', "UHD Quality"],
             [1, 2, 4, "Number of Devices"],
             ["3rd party Movie only", "Basic Plan Content + Sports", "Standard Plan + PacFlix Original Series", "Type of Contents"],
             [120_000, 160_000, 200_000, "Price"]
        ]

    print(tabulate(tables, headers, tablefmt='github'))

  # check current plan from existing users
  def check_plan(self, username):
    self.username = username
    if self.username in user_data:
      current_plan = user_data[self.username][0]
      duration_plan = user_data[self.username][1]

      print(f'Username: {self.username}')
      print(f'Current Plan: {current_plan}')
      print(f'Duration Plan: {duration_plan}')

    else:
      raise Exception('Input username correctly')

  # check upgrade plan discount based on statement before
  def upgrade_plan(self, username, new_plan):
    self.username = username
    self.new_plan = new_plan

    # class atributes
    DISCOUNT_UPGRADE = 0.05
    STANDARD_PRICE = 160000
    PREMIUM_PRICE = 200000
    BASIC_PRICE = 120000

    for keys, values, in user_data.items():
      if self.username == keys:

        # get the current plan and duration data
        current_plan = values[0]
        duration_plan = values[1]

        if new_plan != current_plan and duration_plan > 12:
          if new_plan == 'Standard plan':
            total_payout = STANDARD_PRICE - (STANDARD_PRICE * DISCOUNT_UPGRADE)
          if new_plan == 'Premium plan':
            total_payout = PREMIUM_PRICE - (PREMIUM_PRICE * DISCOUNT_UPGRADE)
          if new_plan == 'Basic plan':
            total_payout = BASIC_PRICE - (BASIC_PRICE * DISCOUNT_UPGRADE)

          return total_payout
        found = True
        break
      else:
        found = False

    if found == False:
      raise Exception('Input username correctly')
    
    
# create new class NewUser to give the solution
class NewUser:
  # create empty list to store the generated referral code
  get_generated_code = []
  # create list for the list of plan
  get_plan = []
  unique_plan = set()
  for values in user_data.values():
    unique_plan.add(values[0])
    get_plan = list(unique_plan)

  # generate the referral code and append it to the empty list
  def generate_code(self):
    for values in user_data.values():
      get_code = values[2]
      self.get_generated_code.append(get_code)

  # get the discount for new user when they put the referral that is matched with the current user
  def new_user_discount(self, username, new_plan, referral):
    self.username = username
    self.new_plan = new_plan
    self.referral = referral

    # the class atributes
    DISCOUNT_REFERRAL = 0.04
    STANDARD_PRICE = 160000
    PREMIUM_PRICE = 200000
    BASIC_PRICE = 120000

    if referral in self.get_generated_code and new_plan in self.get_plan:
      if new_plan == 'Standard plan':
        total_payout = STANDARD_PRICE - (STANDARD_PRICE * DISCOUNT_REFERRAL)
      if new_plan == 'Premium plan':
        total_payout = PREMIUM_PRICE - (PREMIUM_PRICE * DISCOUNT_REFERRAL)
      if new_plan == 'Basic plan':
        total_payout = BASIC_PRICE - (BASIC_PRICE * DISCOUNT_REFERRAL)

      return total_payout

    if referral not in self.get_generated_code and new_plan in self.get_plan:
      if new_plan == 'Standard plan':
        total_payout = STANDARD_PRICE
      if new_plan == 'Premium plan':
        total_payout = PREMIUM_PRICE
      if new_plan == 'Basic plan':
        total_payout = BASIC_PRICE

      return total_payout
    else:
      raise Exception('Input data correctly')