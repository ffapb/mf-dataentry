from django.test import TestCase
from .models import Category, Security, SecurityBond, QuotationPlace,Currency,RateListProvider,TradingCategory,Subtype,Nature, TradingCenter, Nationality, DepositPlace, AssetAllocation

# Create your tests here.
class CategoryTests(TestCase):

  def test_display_shows_sources_1(self):
    c1 = Category.objects.create(name='test name', code_leb='l1', code_dub='d1')
    actual = c1.__str__()
    expected = 'test name (LB, AE)'
    self.assertEquals(expected, actual)

  def test_display_shows_sources_2(self):
    c1 = Category.objects.create(name='test name', code_leb='l1', code_dub=None)
    actual = c1.__str__()
    expected = 'test name (LB)'
    self.assertEquals(expected, actual)


class SecurityTests(TestCase):
  
  #def test_save_bond(self,code= 'Test17102017',circular='NULL', designation= 'test17102017', symbol = 'Test17102017',currency = 'LBP', subtype= 'ADVANCES TO CLIENTS', category = 'CIFs', trading_categor = 'Funds', nature = 'Carrier', trading_center = 'IRAQ', nationality = 'CHINA', deposit_place = 'BLOM', quotation_place = 'HONG KONG', asset_allocation = 'Net Hybrid Investments', group_for_ledgers = '4211', general_ledger = '4649', provider_code = 'provcode', provider_ratelist = 'Currency', multiplier_for_online_prices = 1, isin = 'isin', fixing = 'NULL', fix1 = '10:00', fix2 = '11:00', mar_short_position = 11, mar_lng_position = 12, main_short_position = 13, main_lng_position = 14, moody = 'aaa', fitch = 'bbb', s_and_p = 'ccc'):
        
   # if currency.code_leb=='':
    #   raise Exception("Missing currency in leb")
    #if currency.code_dub=='':
     #  raise Exception("Missing currency in dub")                                                                                                                                                                                                                                                                                                                                 
    




    def test_save_bond(self):

        sec= SecurityBond.objects.create(
        code= 'Test17',
        circular='NULL',
        designation= 'test17',
        symbol = 'Test17',
        currency = Currency.objects.create(name='cur', code_leb='l1', code_dub='d1'),
        subtype= Subtype.objects.create(name='sb', code_leb='l2', code_dub='d2'),
        category = Category.objects.create(name='ct', code_leb='l2', code_dub='d3'),
        trading_category = TradingCategory.objects.create(name='tcat', code_leb='l4', code_dub='d4'),
        nature = Nature.objects.create(name='nt', code_leb='l5', code_dub='d5'),
        trading_center = TradingCenter.objects.create(name='trct', code_leb='l6', code_dub='d6'),
        nationality = Nationality.objects.create(name='nlty', code_leb='l7', code_dub='d7'),
        deposit_place = DepositPlace.objects.create(name='Dpp', code_leb='l8', code_dub='d8'),
        quotation_place = QuotationPlace.objects.create(name='QP', code_leb='l9', code_dub='d9'),
        asset_allocation = AssetAllocation.objects.create(name='AsA', code_leb='l10', code_dub='d10'),
        group_for_ledgers = '4211',
        general_ledger = '4649',
        provider_code = 'pro',
        provider_ratelist = RateListProvider.objects.create(name='rlp', code_leb=11, code_dub=11),
        multiplier_for_online_prices = 1,
        isin = 'isi',
        fixing = True,
        fix1 = '10:00',
        fix2 = '11:00',
        mar_short_position = '11',
        mar_lng_position = '12',
        main_short_position ='13',
        main_lng_position = '14',
        moody = 'aaa',
        fitch = 'bbb',
        s_and_p = 'ccc'
        )

       
        actual = sec.checkAllDropdownsOnBothLebDub()
        expected = sec.save()



        self.assertEquals(actual, expected)



    def test_save_bond_2(self):

       sec= SecurityBond.objects.create(
       code= 'Test17',
       circular='NULL',
       designation= 'test17',
       symbol = 'Test17',
       currency = Currency.objects.create(name='cur', code_leb='l1', code_dub='d1'),
       subtype= Subtype.objects.create(name='sb', code_leb='l2', code_dub='d2'),
       category = Category.objects.create(name='ct', code_leb='l2', code_dub='d3'),
       trading_category = TradingCategory.objects.create(name='tcat', code_leb='l4', code_dub='d4'),
       nature = Nature.objects.create(name='nt', code_leb='l5', code_dub='d5'),
       trading_center = TradingCenter.objects.create(name='trct', code_leb='l6', code_dub='d6'),
       nationality = Nationality.objects.create(name='nlty', code_leb='l7', code_dub='d7'),
       deposit_place = DepositPlace.objects.create(name='Dpp', code_leb='l8', code_dub='d8'),
       quotation_place = QuotationPlace.objects.create(name='QP', code_leb='l9', code_dub='d9'),
       asset_allocation = AssetAllocation.objects.create(name='AsA', code_leb='l10', code_dub='d10'),
       group_for_ledgers = '4211',
       general_ledger = '4649',
       provider_code = 'pro',
       provider_ratelist = RateListProvider.objects.create(name='rlp', code_leb=11, code_dub=11),
       multiplier_for_online_prices = 1,
       isin = 'isi',
       fixing = True,
       fix1 = '10:00', 
       fix2 = '11:00',
       mar_short_position = '11',
       mar_lng_position = '12',
       main_short_position ='13',
       main_lng_position = '14',
       moody = 'aaa',
       fitch = 'bbb',
       s_and_p = 'ccc'
       )

       with self.assertRaises(ValueError):
      
        actual = sec.checkAllDropdownsOnBothLebDub()
        expected = sec.save()
      
      

      #self.assertTrue(True)
        self.assertEquals(actual, expected)


