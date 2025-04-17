import itertools
import os
import xml.etree.ElementTree
import xml.etree.ElementTree as ET
from datetime import datetime
import requests

# from random import randint
# import re
#
title_list = {
    '4836_4': 'Шкаф для ванной комнаты',
    '4851_4': 'Трельяж с подсветкой',
    '4850_4': 'Трельяж с подсветкой',
    '4888_4': 'Комод новый',
    '4952_4': 'Комод новый',
    '4872_4': 'Гримерное зеркало',
    '4885_4': 'Стеллаж для рассады',
    '4884_4': 'Стеллаж для рассады',
    '4896_4': 'Открытый модуль для шкафа',
    '4966_4': 'Стол для Рисования Песком с Подсветкой',
    '5004_4': 'Прихожая новая',
    '4915_4': 'Кухня новая',
    '618_4': 'Кухонный пенал',
    '619_4': 'Кухонный пенал',
    '1643_4': 'Кухонный пенал',
    '2194_4': 'Кухонный пенал',
    '3170_4': 'Кухонный пенал',
    '3156_4': 'Кухонный пенал',
    '688_4': 'Кухонный пенал',
    '4363_4': 'Кухонный пенал',
    '4364_4': 'Кухонный пенал',
    '4371_4': 'Кухонный пенал',
    '4404_4': 'Кухонный пенал',
    '4429_4': 'Кухонный пенал',
    '5209_4': 'Диван-кровать',
    '5412_4': 'Кухонный островок',
    '5176_4': 'Кухонный островок',
    '5413_4': 'Кухонный островок',
    # '5092_4': 'Рабочая зона у окна',
}
list_adress = [
    {
        'city': 'Тюменская область, Тюмень',
        'phone': '8 3452 53-11-03',
        'name': 'tumen.xml',
    },
    {
        'city': 'Свердловская область, Екатеринбург',
        'phone': '8 3433 44-66-61',
        'name': 'ekat.xml',
    },
    {
        'city': 'Свердловская область, Екатеринбург',
        'phone': '8 3512 16-30-02',
        'name': 'ekat_new.xml',
    },
    {
        'city': 'Курганская область, Курган',
        'phone': '8 3522 22-73-72',
        'name': 'kurgan.xml',
    },
    {
        'city': 'Челябинская область, Магнитогорск',
        'phone': '8 3512 16-03-12',
        'name': 'magnit.xml',
    },
]
list_all_chel_adress = [
    {
        'city': 'Свердловская область, Екатеринбург',
        'phone': '8 3512 16-44-66',
        'name': '',
        'quantity': 1,
        'id': '3'
    },
    {
        'city': 'Тюменская область, Тюмень',
        'phone': '8 3512 16-44-66',
        'name': '',
        'quantity': 1,
        'id': '4',
    },
    {
        'city': 'Курганская область, Курган',
        'phone': '8 3512 16-44-66',
        'name': '',
        'quantity': 1,
        'id': '2',
    },
    {
        'city': 'Челябинская область, Челябинск, пр-т Победы',
        'phone': '8 3512 16-44-66',
        'name': '',
        'quantity': 1,
        'id': '',
    },
    {
        'city': 'Республика Башкортостан, Уфа',
        'phone': '8 3472 98-03-33',
        'name': '',
        'quantity': 1,
        'id': '123',
    },
    {
        'city': 'Челябинская область, Магнитогорск',
        'phone': '8 3512 16-44-66',
        'name': '',
        'quantity': 1,
        'id': '1',
    },
    {
        'city': 'Челябинская область, Миасс',
        'phone': '8 3513 25-01-05',
        'name': '',
        'quantity': 2,
        'id': '1234',
    },
    {
        'city': 'Челябинская область, Златоустовский г.о., Златоуст',
        'phone': '8 3513 25-01-05',
        'name': '',
        'quantity': 4,
        'id': '12345',
    },
    {
        'city': 'Челябинская область, Чебаркуль',
        'phone': '8 3513 25-01-05',
        'name': '',
        'quantity': 4,
        'id': '123456',
    },
]
list_ekat_tumen = [
    {
        'city': 'Свердловская область, Екатеринбург',
        'phone': '8 3433 44-66-61',
        'name': '',
        'quantity': 1,
        'id': ''
    },
    {
        'city': 'Тюменская область, Тюмень',
        'phone': '8 3452 53-11-03',
        'name': '',
        'quantity': 1,
        'id': '4',
    },
    {
        'city': 'Курганская область, Курган',
        'phone': '8 3512 22-73-72',
        'name': '',
        'quantity': 1,
        'id': '2',
    },
]

list_chel_adres = [
    {
        'city': 'Челябинская область, Челябинск, пр-т Победы',
        'phone': '8 3512 16-44-66',
        'name': '',
        'quantity': 1,
        'id': '',
    },
    {
        'city': 'Республика Башкортостан, Уфа',
        'phone': '8 3472 98-03-33',
        'name': '',
        'quantity': 1,
        'id': '123',
    },
    {
        'city': 'Челябинская область, Магнитогорск',
        'phone': '8 3512 16-44-66',
        'name': '',
        'quantity': 1,
        'id': '1',
    },
    {
        'city': 'Челябинская область, Миасс',
        'phone': '8 3513 25-01-05',
        'name': '',
        'quantity': 2,
        'id': '1234',
    },
    {
        'city': 'Челябинская область, Златоустовский г.о., Златоуст',
        'phone': '8 3513 25-01-05',
        'name': '',
        'quantity': 4,
        'id': '12345',
    },
    {
        'city': 'Челябинская область, Чебаркуль',
        'phone': '8 3513 25-01-05',
        'name': '',
        'quantity': 4,
        'id': '123456',
    },
]

list_one_word_cat = ['Стенка', 'Буфет', 'Шкаф-купе', 'Распашной', 'Детский',
                     'Угловой', 'Детская', 'Кухня', 'Комод', 'Диван', 'Трельяж с подсветкой',
                     'Прихожая', 'Обувница', 'Полка', 'Кухонный', 'Кровать', 'Рабочая',
                     'Стеллаж', 'Шкаф', 'Гостиная', 'Спальня', 'Ель', 'Сосна', 'Елка', 'Угловой модуль',
                     'Вешало', 'Трельяж', 'Двухъярусная', 'Письменный', 'Школьный', 'Компьютерный', 'Обеденная']

list_two_word = {
    'Детский': 'уголок',
    'Распашной': 'шкаф',
    'Угловой': 'шкаф',
    'Детская': 'кухня',
    'Двухъярусная': 'кровать',
    'Кухонный': 'гарнитур',
    'Письменный': 'стол',
    'Школьный': 'уголок',
    'Компьютерный': 'стол',
    'Обеденная': 'зона',
    'Ель': 'новогодняя',
    'Сосна': 'новогодняя',
    'Елка': 'с гирляндой',
    'Рабочая': 'зона у окна',
}

# 2128_4, 2188_4, 2832_4, 3134_4, 3133_4, 2427_4, 4827_4, 3745_4, 3936_4,

goodsType_categor = ['Кухонный гарнитур',
                     'Письменный стол', 'Компьютерный стол', 'Школьный уголок',
                     'Буфет', 'Кухня', 'Гостиная', 'Детский уголок',
                     'Детская кухня']

c1 = ['Двухъярусная кровать', 'Кровать', ]
c2 = ['Трельяж', 'Комод', 'Угловой шкаф', 'Распашной шкаф', 'Обувница', 'Шкаф-купе', 'Вешало',
      'Гостиная', 'Стеллаж', 'Прихожая', 'Стенка']

list_error_title = []
username = 'test_api'
key = 'uaORjeBTmxhsb0WAf6q4CoIbjyg8pqpZwsrTNFpGSt4xJ3Ey7Jh2rANYpIUfUF66RtNkMqNox5UDzokkIceQGvTeheSJDXlbRXC5hNDVykP33rISDrdg1dd0Lrs4L788U4hkaWGOW5zfxbQYVPdRUcRtDdny4oKD13U7DoyBMKFTW43ghEIxK6QIM1YPxljuNA8EdSrhNAsk4DONGywiTn5yXtiHlyYsRsMnqh1dwibPdItBateKWMcoeHLemw4A'
procent_id = ['4954_4', '4948_4', '4947_4', '4949_4']
dont_ip = ['69', '124', '159', '344', '345', '346', '347', '350', '351', '352', '353', '354', '355',
           '2278', '2417', '2671', '2884', '2885', '2886', '3082', '3083', '3084',
           '3087', '3127', '3131', '3136', '3143', '3149', '3150', '3151', '3152', '3153', '3154', '3155',
           '3167', '3168', '3169', '3289', '3343', '3346', '3348', '3354', '3361', '3365', '3367', '3368',
           '3370', '3371', '3383', '3389', '3390', '3391', '3392', '3395', '3396', '3399', '3400', '3401',
           '3407', '3408', '3409', '3410', '3414', '3418', '3419', '3420', '3423', '3427', '3428', '3430',
           '3434', '3435', '3438', '3443', '3444', '3447', '3454', '3460', '3463', '3464', '3465', '3469',
           '3473', '3474', '3475', '3476', '3481', '3486', '3492', '3495', '3503', '3505', '3509', '3511',
           '3514', '3516', '3524', '3525', '3527', '3530', '3533', '3534', '3539', '3540', '3546', '3557',
           '3558', '3560', '3563', '3564', '3570', '3571', '3575', '3577', '3581', '3584', '3588', '3590',
           '3605', '3606', '3607', '3608', '3613', '3614', '3618', '3620', '3621', '3624', '3625', '3630',
           '3633', '3638', '3642', '3643', '3648', '3650', '3652', '3653', '3659', '3661', '3662', '3663',
           '3667', '3669', '3671', '3673', '3679', '3680', '3687', '3688', '3691', '3692', '3693', '3696',
           '3701', '3702', '3705', '3706', '3707', '3710', '3711', '3712', '3713', '3714', '3715', '3722',
           '3723', '3724', '3726', '3731', '3732', '3736', '3741', '3743', '3747', '3749', '3750', '3757',
           '3758', '3759', '3761', '3762', '3764', '3766', '3767', '3768', '3771', '3772', '3774', '3775',
           '3776', '3778', '3781', '3782', '3784', '3789', '3791', '3792', '3797', '3799', '3802', '3807',
           '3812', '3813', '3814', '3816', '3817', '3819', '3820', '3823', '3824', '3825', '3826', '3828',
           '3832', '3833', '3834', '3836', '3839', '3843', '3845', '3847', '3853', '3919', '3920', '3925',
           '3926', '3927', '3929', '3930', '3937', '3941', '3943', '3944', '3945', '3946', '3950', '3951',
           '3953', '3954', '3955', '3964', '3965', '3968', '3969', '3971', '3981', '3982', '3985', '3987', '3991',
           '3997',
           '4000', '4001', '4002', '4004', '4005', '4006', '4008', '4010', '4011', '4013', '4016', '4029',
           '4036', '4037', '4038', '4039', '4040', '4041', '4044', '4045', '4046', '4047', '4048', '4049',
           '4052', '4053', '4054', '4055', '4057', '4060', '4062', '4063', '4064', '4065', '4067', '4068',
           '4071', '4075', '4076', '4077', '4078', '4079', '4080', '4081', '4082', '4086', '4087', '4091',
           '4095', '4098', '4101', '4104', '4105', '4106', '4107', '4108', '4110', '4112', '4113', '4117',
           '4119', '4120', '4121', '4123', '4124', '4125', '4126', '4127', '4128', '4129', '4130', '4132',
           '4135', '4136', '4137', '4138', '4139', '4140', '4141', '4143', '4144', '4145', '4148', '4150',
           '4155', '4156', '4158', '4160', '4165', '4166', '4171', '4172', '4177', '4178', '4181', '4183',
           '4184', '4185', '4186', '4187', '4189', '4190', '4193', '4194', '4196', '4197', '4198', '4199',
           '4200', '4203', '4204', '4205', '4207', '4208', '4209', '4210', '4212', '4213', '4215', '4216',
           '4217', '4219', '4222', '4223', '4224', '4226', '4228', '4229', '4231', '4235', '4236', '4238',
           '4240', '4241', '4242', '4243', '4244', '4245', '4246', '4248', '4250', '4253', '4256', '4257',
           '4258', '4259', '4261', '4262', '4263', '4264', '4265', '4268', '4269', '4270', '4272', '4274',
           '4275', '4276', '4280', '4281', '4282', '4284', '4285', '4287', '4288', '4289', '4290', '4292',
           '4293', '4294', '4295', '4296', '4297', '4299', '4300', '4302', '4303', '4304', '4305', '4306',
           '4313', '4314', '4315', '4316', '4326', '4327', '4328', '4329', '4330', '4331', '4332', '4333',
           '4334', '4335', '4336', '4337', '4338', '4339', '4340', '4341', '4342', '4345', '4346', '4347',
           '4348', '4350', '4351', '4352', '4353', '4354', '4355', '4356', '4357', '4358', '4359', '4360',
           '4362', '4372', '4373', '4374', '4375', '4376', '4377', '4378', '4379', '4380', '4381', '4382',
           '4385', '4386', '4387', '4388', '4389', '4390', '4391', '4392', '4393', '4394', '4395', '4396',
           '4397', '4399', '4400', '4406', '4412', '4413', '4414', '4415', '4416', '4417', '4418', '4419',
           '4420', '4422', '4423', '4424', '4426', '4430', '4431', '4440', '4441', '4442', '4443', '4444',
           '4445', '4454', '4456', '4457', '4458', '4459', '4460', '4461', '4462', '4463', '4464', '4465',
           '4466', '4467', '4469', '4470', '4471', '4472', '4473', '4474', '4475', '4476', '4477', '4478',
           '4479', '4480', '4481', '4482', '4483', '4484', '4485', '4486', '4487', '4488', '4489', '4490',
           '4491', '4492', '4493', '4495', '4496', '4497', '4498', '4499', '4500', '4501', '4502', '4503',
           '4504', '4505', '4506', '4507', '4508', '4509', '4510', '4511', '4512', '4514', '4515', '4516',
           '4519', '4524', '4528', '4529', '4530', '4531', '4532', '4533', '4535', '4545', '4550', '4551',
           '4552', '4553', '4554', '4555', '4556', '4557', '4558', '4559', '4560', '4561', '4563', '4564',
           '4566', '4567', '4568', '4569', '4570', '4571', '4572', '4573', '4574', '4575', '4576', '4577',
           '4578', '4580', '4581', '4584', '4585', '4587', '4594', '4596', '4597', '4598', '4599', '4600',
           '4601', '4604', '4608', '4609', '4610', '4611', '4612', '4613', '4614', '4615', '4616', '4617',
           '4618', '4619', '4620', '4621', '4622', '4624', '4625', '4627', '4628', '4629', '4630', '4631',
           '4632', '4633', '4634', '4635', '4636', '4643', '4644', '4647', '4648', '4649', '4650', '4651',
           '4652', '4653', '4654', '4661', '4662', '4663', '4664', '4665', '4666', '4668', '4669', '4672',
           '4673', '4674', '4675', '4676', '4677', '4678', '4679', '4680', '4681', '4683', '4684', '4685',
           '4686', '4687', '4688', '4689', '4690', '4691', '4692', '4693', '4694', '4695', '4696', '4697',
           '4698', '4699', '4700', '4701', '4703', '4705', '4707', '4709', '4787', '4788', '4789', '4790',
           '4791', '4792', '4793', '4794', '4796', '4797', '4798', '4800', '4801', '4802', '4803', '4805',
           '4806', '4807', '4808', '4809', '4810', '4811', '4812', '4813', '4814', '4815', '4816', '4817',
           '4818', '4819', '4820', '4821', '4822', '4825', '4829', '4830', '4833', '4834', '4835', '4837',
           '4841', '4842', '4843', '4844', '4845', '4846', '4847', '4849', '4852', '4853', '4854', '4855',
           '4856', '4863', '4866', '4867', '4868', '4869', '4870', '4871', '4873', '4874', '4875', '4877',
           '4878', '4889', '4897', '4902', '4903', '4904', '4905', '4907', '4908', '4910', '4911', '4918',
           '4919', '4920', '4921', '4922', '4923', '4924', '4925', '4926', '4927', '4928', '4929', '4930',
           '4931', '4932', '4934', '4935', '4936', '4937', '4938', '4939', '4940', '4945', '4955', '4960',
           '4964', '4965', '4967', '4971', '4974', '4982', '4984', '4985', '4986', '4987', '4988', '4989',
           '4990', '4992', '4996', '4999', '5014', '5019', '5020', '5022', '5023', '5024', '5027', '5031',
           '5032', '5047', '5048', '5053', '5057', '5073', '5074', '5075', '5077', '5078', '5079', '5084',
           '5086', '5090', '5116', '5117', '5127', '5128', '5129', '5130', '5131', '5132', '5133', '5134',
           '5135', '5136', '5152', '5153', '5154', '5157', '5158', '5163', '5182', '5183', '5184', '5185',
           '5199', '5200', '5217', '5218', '5219', '5220', '5221', '5222', '5223', '5224', '5226', '5229', '5231',
           '5232', '5233', '5238', '5239', '5240', '5244', '5245', '5246', '5247', '5248', '5249', '5251',
           '5252', '5253', '5254', '5255', '5257', '5258', '5259', '5260', '5261', '5263', '5265', '5267',
           '5271', '5274', '5277', '5278', '5279', '5284', '5285', '5286', '5287', '5288', '5289', '5290',
           '5291', '5292', '5296', '5297', '5298', '5299', '5300', '5301', '5302', '5303', '5306', '5307',
           '5308', '5310', '5312', '5313', '5317', '5319', '5320', '5321', '5322', '5323']

dont_img = ['catalog/new-color-kuhnius/stoleshnica.jpg', 'catalog/new-color-kuhnius/kuhnkatkorp.jpg',
            'catalog/new-color-kuhnius/kuhnbazkat.jpg', 'catalog/new-color-kuhnius/kuhn1kat.jpg',
            'catalog/new-color-kuhnius/kuhn3kat.jpg', 'catalog/new-color-kuhnius/kuhn2kat.jpg',
            'catalog/- Color/colors_free.jpg', 'data/11_skaf/03.jpg', 'data/11_skaf/04.jpg', 'data/11_skaf/05.jpg',
            'data/11_skaf/08.jpg', 'data/11_skaf/09.jpg', 'data/11_skaf/10.jpg', 'data/00_2014_12/moika_naklad_800.jpg',
            'data/poddon1.jpg', 'data/poddon2.jpg', '""', 'data/11_skaf/07.jpg', 'catalog/Polki/polka1sentyabrya.jpg',
            'data/00_2014_12/moika_naklad_500.jpg', 'data/00_2014_12/moika_naklad_600.jpg', 'data/11_skaf/11.jpg',
            'data/00_2014_12/moika.jpg', 'data/vreznaya-1.jpg', 'data/vreznaya-2.jpg',
            'data/01_kuhni/03_kombi/water_02.jpg', 'data/01_kuhni/03_kombi/water_03.jpg',
            'catalog/05_divan/colorchzvet/Cvetdivana-1.jpg', 'catalog/05_divan/colorchzvet/Cvetdivana-2.jpg',
            'catalog/05_divan/colorchzvet/Cvetdivana-3.jpg', 'data/1831715361.jpg',
            'data/01_kuhni/kuhni_new/kuh_laim2(white-viola).jpg', 'catalog/-%20Color/all/dubvotan.jpg',
            'catalog/-%20Color/all/sonoma.jpg', '']


# list_ror = []
#
# def rfntujh(title):
#     t = title
#     #print(f'{t} =  {title}')
#     if title in list_one_word_cat:
#         #print('qwer  ', title)
#         if title in list_two_word.keys():
#             title = title + ' ' + str(list_two_word[title])
#             return title
#         else:
#             return title
#     else:
#         title = title.split('-', 1)[0]
#         if title in list_one_word_cat:
#             if title in list_two_word.keys():
#                 title = title + ' ' + str(list_two_word[title])
#                 return title
#             else:
#                 return title
#         else:
#             title = title.split(',', 1)[0]
#             if title in list_one_word_cat:
#                 if title in list_two_word.keys():
#                     title = title + ' ' + str(list_two_word[title])
#                     return title
#                 else:
#                     return title
#             else:
#                 title = title.split(' ', 1)
#                 title = title[0]
#                 if title in list_one_word_cat:
#                     if title in list_two_word.keys():
#                         title = title + ' ' + str(list_two_word[title])
#                         return title
#                     else:
#                         return title
#                 else:
#                     list_error_title.append(title)
#
# date = open('avitofeed_108.xml', "r", encoding="utf-8")
# #print(date)
# parser = ET.XMLParser(encoding="utf-8")
# tree = ET.parse(source=date, parser=parser)
# root = tree.getroot()
#
# count = len(root)
# list1 = []
# i = 0
# list_root = []
#
# for el in root.iter('Ad'):
#     s = None
#     a = el.find('Id')
#     list_ror.append(el)
#     t = el.find('Title')
#     first, _, rest = t.text.partition(" ")
#     title = rfntujh(first)
#     t.text = title
#     list1.append(title)
#     list_root.append(el)
#
#     goodstype = el.find('GoodsType')
#     gt = 'Шкафы и комоды'
#     if goodstype.text == gt:
#         goodstype.text = 'Шкафы, комоды и стеллажи'
#
#     s = el.find('Condition')
#     print(s)
#     if s != None:
#         s.text = 'Новое'
#     else:
#         s = xml.etree.ElementTree.SubElement(el, 'Condition')
#         s.text = 'Новое'
#
#     b = el.find('Description')
#     b.text = '<![CDATA[' + b.text + ']]>'
#     i = i + 1
#     print(f'Проверенно {i} из {count}')
#
# print('*-' * 20)
#
# # list_root1 = list_root
# #
# # list_root_good = []
# #
# # te = True
# # step = 0
# # while te:
# #     step += 1
# #     print('step = ', step)
# #     if len(list_root_good) == len(list_root1) or len(list_root) == 0:
# #         te = False
# #
# #     for i in list(set(list_root)):
# #         er = 0
# #         t_i = i.find('Title').text
# #         print('i = ', t_i)
# #         for j in list_root:
# #             t_j = j.find('Title').text
# #             print('j = ', t_j)
# #             if er < 5:
# #                 if t_j == t_i:
# #                     print('i = ', i.find('Title').text, ' j = ', j.find('Title').text)
# #                     list_root_good.append(j)
# #                     list_root.remove(j)
# #                     print(er)
# #                     print('-' * 50)
# #                     print(list_root_good)
# #                     print('*' * 50)
# #                     er = er + 1
# #             else:
# #                 break
# #
# # print('compl m = ', len(list_root_good), ' compl n = ', len(list_root1))
# # print('step final = ', step)
# # list_root_good = xml.etree.ElementTree.Element(list_root_good)
# # root.append(list_root_good)
# #root.remove()
# #root.append(list_root_good)
#
# print(f'Ошибки: {list_error_title}')
# tree.write('xml/prob1.xml', encoding='utf-8')

# list_ob = []
# list_stel = []
# list_kux_gar = []
# list_trel = []
# list_prix = []
# list_vesh = []
# list_sten = []
# list_ugl_shk = []
# list_rasp_shk = []
# list_polk = []
# list_kuxn = []


# ['Обувница', 'Стеллаж', 'Кухонный гарнитур', 'Трельяж',
#  'Прихожая', 'Вешало', 'Стенка', 'Угловой шкаф',
#  'Распашной шкаф', 'Полка', 'Кухня', 'Спальня',
#  'Детская кухня', 'Шкаф-купе', 'Детский уголок',
#  'Кровать', 'Буфет', 'Комод', 'Гостиная',
#  'Двухъярусная кровать']


def open_file(file):
    with open(file, "r", encoding='utf-8') as f:
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.parse(source=f, parser=parser)
        root = tree.getroot()
        f.close()
    return root


def title_edit(title):
    t = title
    if title in list_one_word_cat:
        if title in list_two_word.keys():
            title = title + ' ' + str(list_two_word[title])
            return title
        else:
            return title
    else:
        title = title.split('-', 1)[0]
        if title in list_one_word_cat:
            if title in list_two_word.keys():
                title = title + ' ' + str(list_two_word[title])
                return title
            else:
                return title
        else:
            title = title.split(',', 1)[0]
            if title in list_one_word_cat:
                if title in list_two_word.keys():
                    title = title + ' ' + str(list_two_word[title])
                    return title
                else:
                    return title
            else:
                title = title.split(' ', 1)
                title = title[0]
                if title in list_one_word_cat:
                    if title in list_two_word.keys():
                        title = title + ' ' + str(list_two_word[title])
                        return title
                    else:
                        return title
                else:
                    list_error_title.append(title)


def response_site():
    login = requests.post('https://mebel-vsem74.ru/index.php?route=api/login', data={'username': username, 'key': key})
    api_token = login.json()['api_token']
    json_all_products = requests.post(
        'https://mebel-vsem74.ru/index.php?route=api/custom/products&api_token=' + api_token)
    # print(json_all_products.json())
    all_products = json_all_products.json()['success']['products']
    all_images = json_all_products.json()['success']['images']
    return all_products, all_images


def ads_update(root):
    contexts = list()
    check_id = list()
    response, all_images = response_site()
    i = 0
    for ad in root.iter('Ad'):
        id, goodsSubType, adStatus, allowEmail, managerName, contactPhone = None, None, None, None, None, None
        address, category, title, goodsType, condition, adType, description = None, None, None, None, None, None, None
        price, images, kitchenType, price_1, length, baseMaterial, length_1 = None, None, None, None, None, None, None,
        out_wear, dresserType, cabinetType, foldingMechanism, furnitureShape, width = None, None, None, None, None, None
        tabletopMaterial, height, width_1, shelvingType, video, upholsteryMaterial = None, None, None, None, None, None
        heightRegulation, doorsMaterial, kitchenShape, worktopIncluded, depthByWorktop = None, None, None, None, None
        priceType, worktopMaterial, furnitureAdditions, furnitureFrame, tableType = None, None, None, None, None
        diningFurnitureSet, canBeDisassembled, interiorSubType, productType, furnitureType = None, None, None, None, None
        worktopColor, sleepingPlaceWidth, sleepingPlaceLength, lengthForDelivery = None, None, None, None
        widthForDelivery, heightForDelivery = None, None
        colorName = True
        furnitureSet = []
        response_images = []
        furnitureAdditions = []
        i += 1
        id = ad.find('Id').text
        if id in check_id:
            continue
        else:
            check_id.append(id)
        # print(id)
        if id.split('_')[0] in response.keys() and id.split('_')[0] not in dont_ip:
            id_product = response[id.split('_')[0]]
            print(id)
            # print(id_product['product_id'])
            adStatus = ad.find('AdStatus').text
            allowEmail = ad.find('AllowEmail').text
            managerName = ad.find('ManagerName').text
            contactPhone = ad.find('ContactPhone').text
            address = ad.find('Address').text
            category = ad.find('Category').text
            title = ad.find('Title').text
            # if 'Комод' in title:
            #     continue
            print(title)
            description = ad.find('Description').text
            if id in title_list.keys():
                title = title_list[id]
            else:
                first, _, rest = title.partition(" ")
                title = title_edit(first)
            # print('123', title)
            try:
                goodsSubType = ad.find('GoodsSubType').text
            except:
                goodsSubType = None
            if 'Компьютерный' in title or 'Рабочая зона у окна' in title:
                goodsType = 'Компьютерные столы и кресла'
                goodsSubType = 'Столы'
            elif 'Полка' in title:
                goodsType = 'Шкафы, комоды и стеллажи'
            elif 'Школьный' in title or 'Письменный' in title:
                goodsType = 'Столы и стулья'
                goodsSubType = 'Столы'
                canBeDisassembled = 'Нет'
            elif 'Обеденная зона' in title:
                goodsType = 'Столы и стулья'
                goodsSubType = 'Обеденная группа'
                diningFurnitureSet = ['Стол', 'Табурет']
                foldingMechanism = 'Нет'
                furnitureShape = 'Квадратный'
            else:
                goodsType = ad.find('GoodsType').text
                if goodsType == 'Шкафы и комоды':
                    goodsType = 'Шкафы, комоды и стеллажи'
                if 'Кухонные гарнитуры' == goodsType:
                    goodsSubType = 'Кухни'
                    kitchenType = 'Готовая'
                    doorsMaterial = 'ЛДСП'
                    worktopIncluded = 'Есть'
                    depthByWorktop = '60'
                    priceType = 'за всё'
                    worktopMaterial = 'ЛДСП'
                    worktopColor = 'Другой'

            if 'Кровати, диваны и кресла' == goodsType:
                goodsSubType = 'Кровати'
                if 'Спальня' in title:
                    goodsSubType = 'Спальные гарнитуры'
                    if 'Кровать' in description or 'кровать' in description:
                        furnitureSet.append('Кровать')
                        if '800х1900' in description or '1900х800' in description or '800x1900' in description or '1900x800' in description:
                            length_1 = '190'
                            width_1 = '80'
                            height = '30'
                            sleepingPlaceWidth = '80'
                            sleepingPlaceLength = '190'
                        if '1400х1900' in description or '1900х1400' in description or '1400x1900' in description or '1900x1400' in description:
                            length_1 = '190'
                            width_1 = '140'
                            height = '30'
                            sleepingPlaceWidth = '140'
                            sleepingPlaceLength = '190'
                        if '1200х1900' in description or '1900х1200' in description or '1200x1900' in description or '1900x1200' in description:
                            length_1 = '190'
                            width_1 = '120'
                            height = '30'
                            sleepingPlaceWidth = '120'
                            sleepingPlaceLength = '190'
                    if 'Комод' in description or 'комод' in description:
                        furnitureSet.append('Комод')
                    if 'Шкаф' in description or 'Шкаф-купе' in description or 'Распашной шкаф' in description or \
                            'Угловой шкаф' in description or 'шкаф' in description or 'Купе' in description or \
                            'купе' in description:
                        furnitureSet.append('Шкаф')
                    if 'Тумба' in description or 'тумба' in description or 'тумбочки' in description or \
                            'тумбочка' in description or 'Тумбы' in description or 'тумбы' in description:
                        furnitureSet.append('Прикроватная тумба')
                    if 'Трюмо' in description or 'трюмо' in description or 'Трельяж' in description or \
                            'трельяж' in description or 'Трюм' in description or 'трюм' in description:
                        furnitureSet.append('Туалетный стол')
                    if 'настенное зеркало' in description:
                        furnitureSet.append('Зеркало')
                if 'Диван' in title:
                    goodsSubType = 'Диваны'
                    foldingMechanism = 'Есть'
                    upholsteryMaterial = 'Другой'
                    colorName = False
                    if id in ['3936_4', '3745_4', '4513_4', '5203_4', '5202_4', '5201_4', '4962_4', '5209_4', '3934_4',
                              '5416_4', '5419_4', '2830_4', '5237_4', '3754_4', '3798_4', '4804_4', '4909_4', '4962_4',
                              '5201_4', '5202_4', '5236_4', '5366_4', '5114_4', '5124_4', '5125_4', '5126_4', '3821_4',
                              '3934_4', '5416_4', '5419_4', '5423_4', '5424_4', '5425_4', '5426_4', '5427_4']:
                        furnitureShape = "Прямой"
                    else:
                        furnitureShape = 'Угловой'
            elif 'Шкафы, комоды и стеллажи' == goodsType:
                if 'Шкаф-купе' in title or 'Распашной шкаф' in title or 'Угловой шкаф' in title:
                    goodsSubType = 'Шкафы и буфеты'
                    cabinetType = 'Шкаф'
                elif 'Комод' in title:
                    goodsSubType = 'Комоды и тумбы'
                    dresserType = 'Комод'
                elif 'Трельяж' in title:
                    goodsSubType = 'Комоды и тумбы'
                    dresserType = 'Другой'
                elif 'Стеллаж' in title:
                    goodsSubType = 'Стеллажи и этажерки'
                    shelvingType = 'Стеллаж'
                elif 'Полка' in title:
                    goodsSubType = 'Полки'
                elif 'Буфет' in title:
                    cabinetType = 'Буфет'
                elif 'Обувница' in title or 'Вешало' in title or 'Прихожая' in title:
                    goodsSubType = 'Прихожие и обувницы'
                    if 'Прихожая' in title:
                        out_wear = 'Прихожая'
                    if 'Обувница' in title:
                        out_wear = 'Обувница'
                    else:
                        out_wear = 'Другой'
                else:
                    goodsSubType = 'Другое'
            elif 'Кухонные гарнитуры' == goodsType:
                goodsSubType = 'Кухни'
                kitchenType = 'Готовая'
                doorsMaterial = 'ЛДСП'

            if 'Двухъярусная кровать' in title:
                furnitureType = 'Двухъярусная'
                furnitureFrame = 'ЛДСП'
            elif 'Спальня' in title:
                furnitureType = 'Двуспальная'
            elif 'Письменный' in title or 'Школьный' in title:
                tableType = 'Письменный'
                furnitureShape = 'Прямоугольный'
                foldingMechanism = 'Нет'
                tabletopMaterial = 'ЛДСП'
                baseMaterial = 'ЛДСП'
            elif 'Компьютерный' in title or 'Рабочая зона у окна' in title:
                tableType = 'Компьютерный'
                heightRegulation = 'Нет'
                furnitureShape = 'Прямоугольный'
                foldingMechanism = 'Нет'
                tabletopMaterial = 'ЛДСП'
                baseMaterial = 'ЛДСП'
            else:
                furnitureType = None
                tableType = None
            adType = ad.find('AdType').text
            if 'Шкаф для ванной комнаты' in title:
                category = 'Ремонт и строительство'
                goodsType = 'Сантехника, водоснабжение и сауна'
                goodsSubType = 'Мебель для ванной'
                productType = 'Шкафы и комоды'
            if 'Кухня' in title or 'Кухонный гарнитур' in title:
                if 'Угловой' in description or 'Мойка 05' in description:
                    kitchenShape = 'Угловая'
                else:
                    kitchenShape = 'Прямая'
                if 'Тумба под мойку' in description or '+ мойка 50см' in description or 'Тумба под раковину' in description:
                    furnitureAdditions.append('Шкаф под мойку')
                if 'Кухонный стол под духовой шкаф' in description:
                    furnitureAdditions.append('Шкаф под духовку')
                if 'Кухонный пенал' in description:
                    furnitureAdditions.append('Пенал')
                if 'Навесной шкаф' in description:
                    furnitureAdditions.append('Навесные шкафы')
                if 'выдвижным ящиком' in description:
                    furnitureAdditions.append('Шкаф с ящиками')
            if 'Сосна' in title or 'Ель' in title or 'Елка' in title:
                print('1')
                goodsType = 'Предметы интерьера, искусство'
                goodsSubType = 'Новогодние украшения'
                interiorSubType = 'Искусственные ёлки'
            if 'Буфет' in title:
                goodsType = 'Кухонные гарнитуры'
                goodsSubType = 'Другое'
                kitchenShape = 'Прямая'
            if 'Гостиная' in title:
                goodsType = 'Шкафы, комоды и стеллажи'
                goodsSubType = 'Гарнитуры и комплекты'
                furnitureSet = ['Шкаф', 'Тумба под ТВ', 'Комод', 'Стол']
            if 'Кухонный островок' in title:
                goodsSubType = 'Другое'
                kitchenShape = 'Прямая'
            # if 'Рабочая зона у окна' in title:
            #     goodsSubType = 'Другое'
            # price = ad.find('Price').text
            if id_product['special']:
                # if 'Диван' in title or id in procent_id:
                #     price_1 = id_product['special']
                #     price = price_1.split('.')[0]
                #     price = int(round(int(price) + (int(price)/100*11), -1))
                # else:
                price_1 = id_product['special']
                price = price_1.split('.')[0]
                price = int(price)
                # if 'Диван' in title:
                #     if id in ['4962_4', '5201_4', '5202_4']:
                #         price = int(round(int(price) + (int(price) / 100 * 11), -1))
                #     else:
                #         price = int(price)
                # else:
                #     price = int(round(int(price) + (int(price) / 100 * 11), -1))
            if id_product['length'] and id_product['length'] != '0.00000000':
                length = str(id_product['length'])
                length = int(length.split('.')[0])
                if length > 0:
                    length = int(length / 10)
            if id_product['width'] and id_product['width'] != '0.00000000':
                width = str(id_product['width'])
                width = int(width.split('.')[0])
                if width > 0:
                    width = int(width / 10)
            if id_product['height'] and id_product['height'] != '0.00000000':
                height = str(id_product['height'])
                height = int(height.split('.')[0])
                if height > 0:
                    height = int(height / 10)
            if 'Кровать' in title:
                furnitureFrame = 'ЛДСП'
                if width:
                    if width >= 120:
                        furnitureType = 'Двуспальная'
                    else:
                        furnitureType = 'Односпальная'
            if 'Школьный уголок' in title or 'Письменный стол' in title:
                lengthForDelivery = length
                widthForDelivery = width
                heightForDelivery = height
            if 'Письменный стол' in title or 'Школьный уголок' in title or 'Двухъярусная кровать' in title \
                    or 'Кровать' in title or 'Кухонный островок' in title:
                if id_product['length'] and id_product['length'] != '0.00000000':
                    length_1 = str(id_product['length'])
                    length_1 = int(length_1.split('.')[0])
                    if length_1 > 0:
                        length_1 = int(length_1 / 10)
            if 'Письменный стол' in title or 'Школьный уголок' in title or 'Кровать' in title \
                    or 'Двухъярусная кровать' in title or 'Кухонный островок' in title:
                if id_product['width'] and id_product['width'] != '0.00000000':
                    width_1 = str(id_product['width'])
                    width_1 = int(width_1.split('.')[0])
                    if width_1 > 0:
                        width_1 = int(width_1 / 10)
            # images = ad.find('Images')
            # images = list(map(lambda x: '"' + x.attrib['url'] + '"', images))
            if id_product['image']:
                img_text = '"https://mebel-vsem74.ru/image/' + id_product['image'] + '"'
                response_images.append(img_text)
            for image in all_images:
                if len(response_images) < 10:
                    if image["image"] in dont_img:
                        continue
                    else:
                        if image['product_id'] == id.split('_')[0]:
                            img_text = '"https://mebel-vsem74.ru/image/' + image['image'] + '"'
                            response_images.append(img_text)
                else:
                    break
            # if id == '5009_4':
            #     if '"https://mebel-vsem74.ru/image/catalog/Dopdlyashkafa76.png"' not in response_images:
            #         response_images.append('"https://mebel-vsem74.ru/image/catalog/Dopdlyashkafa76.png"')
            # elif id == '5010_4':
            #     if '"https://mebel-vsem74.ru/image/catalog/Dopdlyashkafa77.png"' not in response_images:
            #         response_images.append('"https://mebel-vsem74.ru/image/catalog/Dopdlyashkafa77-1.jpg"')
            # if id == '4901_4':
            #     if '"https://mebel-vsem74.ru/image/catalog/Dopdlyashkafa63.png"' not in response_images:
            #         response_images.append('"https://mebel-vsem74.ru/image/catalog/Dopdlyashkafa63-1.jpg"')
            if id == '5044_4' or id == '5043_4' or id == '5045_4' or id == '5046_4':
                if '"https://mebel-vsem74.ru/image/catalog/Dvernieruchki.jpg"' in response_images:
                    response_images.remove('"https://mebel-vsem74.ru/image/catalog/Dvernieruchki.jpg"')
            #     кухня антрацит-11
            if id == '5059_4':
                for qwea in range(len(response_images)):
                    if response_images[
                        qwea] == '"https://mebel-vsem74.ru/image/catalog/03_kyhnya/Antracit/Antracit11.jpg"':
                        response_images[
                            qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/kuhnyaantracit11-3.jpg"'
            #     кухня астра-7
            if id == '152_4':
                # print(response_images)
                for qwea in range(len(response_images)):
                    if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/03_kyhnya/new/Kuhnyaastra7.jpg"':
                        response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/kuhnyaastr-7.jpg"' #     кухня астра-7

            #     кухня антрацит-5
            # if id == '4946_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/03_kyhnya/Antracit/antracit-5/Antracit5.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Antracit-5.jpg"'
            #     print(response_images)
            #     кухня антрацит-4
            # if id == '4915_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/03_kyhnya/Antracit/Antracit4.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/KuhnyaAntracit-4Dostavka.jpg"'
            #     print(response_images)
            #   Диван 913 угловой
            # if id == '5206_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/05_divan/new/divan913.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Divan913.jpg"'
            #     print(response_images)
            #   Комод 75
            # if id == '1762_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/10_komods/new/075/kom75-1.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Komod75.jpg"'
            #     print(response_images)
            #   Кровать 58
            # if id == '1669_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/02_krovati/new/krovat58.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Krovat58.jpg"'
            #     print(response_images)
            #   Кровать 78
            # if id == '1766_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/02_krovati/new/krovat78(2).jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Krovat78.jpg"'
            #     print(response_images)
            #   Прихожая пр-33
            # if id == '1538_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/06_prihoj/prihozhaya_pr_33_enge_bd.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/PrihozhayaPR-33.jpg"'
            #     print(response_images)
            #   Распашной шкаф 01
            # if id == '411_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/04_shkaf/Raspashnojshkai01.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Raspashnojshkaf01.jpg"'
            #     print(response_images)
            #   Распашной шкаф 551
            # if id == '4876_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/04_shkaf/Raspashnojshkaf55spolkami.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Raspashnojshkaf551.jpg"'
            #     print(response_images)
            #   Распашной шкаф 56
            # if id == '4879_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/04_shkaf/Raspashnojshkaf56.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Raspashnojshkaf56+obscheeshkafi.jpg"'
            #     print(response_images)
            #   Стенка-10
            # if id == '245_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/data/07_stenki/new_stenki/wall_10.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Stenka-10.jpg"'
            #     print(response_images)
            #   Диван 765
            # if id == '3745_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/05_divan/new/divan765.png"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/transobschee.jpg"'
            #   кухня антрацит-2
            # if id == '5112_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/03_kyhnya/Antracit/antracit-2/Antracit2.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Antracit-2.jpg"'
            #   Кухня дуб вотан-2
            # if id == '4913_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/03_kyhnya/Dubvotan/002/Dubvotan2.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Dubvotan-2.jpg"'
            #   Кухня дуб вотан-3
            # if id == '5111_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/03_kyhnya/Dubvotan/KuhnyaDubvotan3.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Dubvotan-3.jpg"'
            #   Кухня фиджи 12 угловая
            # if id == '1185_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/data/fidgi-12(1.7x1.4).jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Fidzhi-12uglovaya.jpg"'
            #   Кухня инга-3
            # if id == '163_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/data/01_kuhni/kuhni_new/kuh_inga3.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Inga-3.jpg"'
            #   буфет 08
            # if id == '5314_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/03_kyhnya/Bufet/008/Bufet8.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Kuhonnijbufet.jpg"'
            #   кухня маренго-1
            # if id == '5044_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/03_kyhnya/Marengo/Kuhnyamarengo-1.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Marengo-1.jpg"'
            #   кухня маренго-2
            # if id == '5043_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/03_kyhnya/Marengo/Kuhnyamarengo-2.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Marengo-2.jpg"'
            #   кухня мария-2
            # if id == '4179_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/catalog/03_kyhnya/kuhn-mariya-2.jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Mariya-2.jpg"'
            #   кухня милан-14
            # if id == '1208_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[qwea] == '"https://mebel-vsem74.ru/image/data/milan-14(1.5).jpg"':
            #             response_images[qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Milan-14.jpg"'
            #   кухня венге + белый дуб-5
            # if id == '1221_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[
            #             qwea] == '"https://mebel-vsem74.ru/image/data/01_kuhni/kuhni_new/kuh_veng-bd5.jpg"':
            #             response_images[
            #                 qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Venge+BelijDub-5-1.jpg"'
            #   кухня венге + белый дуб
            # if id == '734_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[
            #             qwea] == '"https://mebel-vsem74.ru/image/catalog/03_kyhnya/vbd-2002.jpg"':
            #             response_images[
            #                 qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/Venge+BelijDub.jpg"'
            #   кухня яна венге + белый дуб
            # if id == '143_4':
            #     for qwea in range(len(response_images)):
            #         if response_images[
            #             qwea] == '"https://mebel-vsem74.ru/image/catalog/03_kyhnya/new/KuhnyaYAna-900.jpg"':
            #             response_images[
            #                 qwea] = '"https://mebel-vsem74.ru/image/catalog/Fotodlyaavito-dostavka/YAnaCvetVenge-BelijDub.jpg"'
            # #
            # if id == '':
            #     for qwea in range(len(response_images)):
            #         if response_images[
            #             qwea] == '""':
            #             response_images[
            #                 qwea] = '""'
            # if 'Кухня' in title or 'Кухонный гарнитур' in title:
            #     description = '<>' + description
            images = response_images
            video = ad.find('VideoURL')
            try:
                video = video.text
            except:
                video = None
            context = {
                'id': id,
                'title': title,
                'adStatus': adStatus,
                'allowEmail': allowEmail,
                'managerName': managerName,
                'contactPhone': contactPhone,
                'length': length,
                'length_1': length_1,
                'furnitureSet': furnitureSet,
                'width': width,
                'width_1': width_1,
                'height': height,
                'address': address,
                'colorName': colorName,
                'interiorSubType': interiorSubType,
                'furnitureFrame': furnitureFrame,
                'lengthForDelivery': lengthForDelivery,
                'widthForDelivery': widthForDelivery,
                'heightForDelivery': heightForDelivery,
                'category': category,
                'sleepingPlaceWidth': sleepingPlaceWidth,
                'sleepingPlaceLength': sleepingPlaceLength,
                'goodsType': goodsType,
                'productType': productType,
                'furnitureType': furnitureType,
                'diningFurnitureSet': diningFurnitureSet,
                'depthByWorktop': depthByWorktop,
                'worktopIncluded': worktopIncluded,
                'canBeDisassembled': canBeDisassembled,
                'kitchenShape': kitchenShape,
                'doorsMaterial': doorsMaterial,
                'heightRegulation': heightRegulation,
                'shelvingType': shelvingType,
                'worktopMaterial': worktopMaterial,
                'baseMaterial': baseMaterial,
                'tabletopMaterial': tabletopMaterial,
                'furnitureShape': furnitureShape,
                'foldingMechanism': foldingMechanism,
                'worktopColor': worktopColor,
                'out_wear': out_wear,
                'dresserType': dresserType,
                'tableType': tableType,
                'priceType': priceType,
                'upholsteryMaterial': upholsteryMaterial,
                'cabinetType': cabinetType,
                'kitchenType': kitchenType,
                'goodsSubType': goodsSubType,
                'adType': adType,
                'description': description,
                'furnitureAdditions': furnitureAdditions,
                'price': price,
                'images': images,
                'video': video,
            }
            contexts.append(context)

    return contexts


def write_text(context, i):
    wtc = f'<WorktopColor>{context["worktopColor"]}</WorktopColor>' if context['worktopColor'] else ''
    ptp = f'<ProductType>{context["productType"]}</ProductType>' if context['productType'] else ''
    ist = f'<InteriorSubType>{context["interiorSubType"]}</InteriorSubType>' if context[
        'interiorSubType'] else ''  # interiorSubType
    cbd = f'<CanBeDisassembled>{context["canBeDisassembled"]}</CanBeDisassembled>' if context[
        'canBeDisassembled'] else ''
    ff = f'<FurnitureFrame><Option>{context["furnitureFrame"]}</Option></FurnitureFrame>' if context[
        'furnitureFrame'] else ''
    r = f'<GoodsSubType>{context["goodsSubType"]}</GoodsSubType>' if context['goodsSubType'] else ''
    y = f'<FurnitureType>{context["furnitureType"]}</FurnitureType>' if context['furnitureType'] else ''
    t = f'<TableType>{context["tableType"]}</TableType>' if context['tableType'] else ''
    k = f'<KitchenType>{context["kitchenType"]}</KitchenType>' if context['kitchenType'] else ''
    kh = f'<KitchenShape>{context["kitchenShape"]}</KitchenShape>' if context['kitchenShape'] else ''
    w = f'<WorktopIncluded>{context["worktopIncluded"]}</WorktopIncluded>' if context['worktopIncluded'] else ''
    dw = f'<DepthByWorktop>{context["depthByWorktop"]}</DepthByWorktop>' if context['depthByWorktop'] else ''
    pt = f'<PriceType>{context["priceType"]}</PriceType>' if context['priceType'] else ''
    u = f'<UpholsteryMaterial>{context["upholsteryMaterial"]}</UpholsteryMaterial>' if context[
        'upholsteryMaterial'] else ''
    wm = f'<WorktopMaterial>{context["worktopMaterial"]}</WorktopMaterial>' if context['worktopMaterial'] else ''
    h = f'<HeightRegulation>{context["heightRegulation"]}</HeightRegulation>' if context["heightRegulation"] else ''
    shelving_type = f'<ShelvingType>{context["shelvingType"]}</ShelvingType>' if context["shelvingType"] else ''
    base_material = f'<BaseMaterial>{context["baseMaterial"]}</BaseMaterial>' if context['baseMaterial'] else ''
    tabletop_material = f'<TabletopMaterial>{context["tabletopMaterial"]}</TabletopMaterial>' if context[
        'tabletopMaterial'] else ''
    furniture_shape = f'<FurnitureShape>{context["furnitureShape"]}</FurnitureShape>' if context[
        'furnitureShape'] else ''
    folding_mechanism = f'<FoldingMechanism>{context["foldingMechanism"]}</FoldingMechanism>' if context[
        'foldingMechanism'] else ''
    out_wear = f'<OutwearDresserType>{context["out_wear"]}</OutwearDresserType>' if context["out_wear"] else ''
    dresser_type = f'<DresserType>{context["dresserType"]}</DresserType>' if context['dresserType'] else ''
    width = f'<Width>{context["length"]}</Width>' if context['length'] and not context['length_1'] else ''
    length = f'<Length>{context["length_1"]}</Length>' if context['length_1'] else ''
    width_1 = f'<Width>{context["width_1"]}</Width>' if context['width_1'] else ''
    height = f'<Height>{context["height"]}</Height>' if context['height'] else ''
    depth = f'<Depth>{context["width"]}</Depth>' if context['width'] and not context['width_1'] else ''
    cabinetType = f'<CabinetType>{context["cabinetType"]}</CabinetType>' if context["cabinetType"] else ''
    color = f'<Color>Другой</Color>'
    dfs = f'<DiningFurnitureSet><Option>{"</Option><Option>".join(context["diningFurnitureSet"])}' \
          '</Option></DiningFurnitureSet>' if context['diningFurnitureSet'] else ''
    fa = f'<FurnitureAdditions><Option>{"</Option><Option>".join(context["furnitureAdditions"])}' \
         f'</Option></FurnitureAdditions>' if len(context["furnitureAdditions"]) > 0 else ''
    v = f'<VideoURL>{context["video"]}</VideoURL>' if context['video'] else ''
    material = f'<Material><Option>ЛДСП</Option></Material>'
    color_all = f'<ColorName>Венге/Белый Дуб/Белый/Серый</ColorName>' if context['colorName'] \
        else '<ColorName>Серый/Белый/Бежевый</ColorName>'
    d = f'<DoorsMaterial><Option>{context["doorsMaterial"]}</Option></DoorsMaterial>' if context[
        'doorsMaterial'] else ''
    delivery = f'<Delivery><Option>Свой курьер</Option></Delivery>'
    prepayment_amount = f'<PrepaymentAmount>0</PrepaymentAmount>'
    variability = f'<Variability>Несколько вариантов</Variability>'
    fS = f'<FurnitureSet><Option>{"</Option><Option>".join(context["furnitureSet"])}' \
         '</Option></FurnitureSet>' if context['furnitureSet'] else ''
    sPL = f'<SleepingPlaceLength>{context["sleepingPlaceLength"]}</SleepingPlaceLength>' if context[
        'sleepingPlaceLength'] else ''
    sPW = f'<SleepingPlaceWidth>{context["sleepingPlaceWidth"]}</SleepingPlaceWidth>' if context[
        'sleepingPlaceWidth'] else ''
    lfd = f'<LengthForDelivery>{context["lengthForDelivery"]}</LengthForDelivery>' if context[
        'lengthForDelivery'] else ''
    wfd = f'<WidthForDelivery>{context["widthForDelivery"]}</WidthForDelivery>' if context[
        'widthForDelivery'] else ''
    hfd = f'<HeightForDelivery>{context["heightForDelivery"]}</HeightForDelivery>' if context[
        'heightForDelivery'] else ''
    message_to_buyer = f'<MessageToBuyer>Здравствуйте! Напишите нужный размер, вариант и цвет. Если есть примеры желаемого, отправьте их тоже.</MessageToBuyer>'
    s = f'<Ad>' \
        f'<Id>{context["id"]}</Id>' \
        f'<AdStatus>{context["adStatus"]}</AdStatus>' \
        f'<AllowEmail>{context["allowEmail"]}</AllowEmail>' \
        f'<ManagerName>{context["managerName"]}</ManagerName>' \
        f'<ContactPhone>{i["phone"]}</ContactPhone>' \
        f'<Address>{i["city"]}</Address>' \
        f'<Category>{context["category"]}</Category>' \
        f'<GoodsType>{context["goodsType"]}</GoodsType>' \
        f'{r}' \
        f'{delivery}' \
        f'{prepayment_amount}' \
        f'{variability}' \
        f'{message_to_buyer}' \
        f'{dresser_type}' \
        f'{out_wear}' \
        f'{cabinetType}' \
        f'{furniture_shape}' \
        f'{folding_mechanism}' \
        f'{tabletop_material}' \
        f'{base_material}' \
        f'{shelving_type}' \
        f'{y}' \
        f'{t}' \
        f'{h}' \
        f'{u}' \
        f'{d}' \
        f'{ist}' \
        f'{kh}' \
        f'{w}' \
        f'{k}' \
        f'{dw}' \
        f'{ptp}' \
        f'{wm}' \
        f'{ff}' \
        f'{pt}' \
        f'{dfs}' \
        f'{color_all}' \
        f'{color}' \
        f'{wtc}' \
        f'{material}' \
        f'{width}' \
        f'{width_1}' \
        f'{depth}' \
        f'{height}' \
        f'{length}' \
        f'{fa}' \
        f'{cbd}' \
        f'{fS}' \
        f'{sPL}' \
        f'{sPW}' \
        f'{lfd}' \
        f'{wfd}' \
        f'{hfd}' \
        f'<Condition>Новое</Condition>' \
        f'<Availability>В наличии</Availability>' \
        f'<Title>{context["title"]}</Title>' \
        f'<Color>Другой</Color>' \
        f'<Stock>100</Stock>' \
        f'<AdType>Товар произведён мной</AdType>' \
        f'<Description><![CDATA[{context["description"]}]]></Description>' \
        f'<Price>{context["price"]}</Price>' \
        f'<Images>' \
        f'<Image url={"/><Image url=".join(context["images"])}/>' \
        f'</Images>' \
        f'{v}' \
        f'</Ad>'
    return s


def write_ad(contexts):
    time = datetime.now()
    time = str(str(time.year) + '-' + str(time.month) + '-' + str(time.day))
    parent = 'Z:/IT отдел/Толя/xml/avito/'
    path = os.path.join(parent, 'готово ' + time)
    file_name = 'готово ' + time
    # print(path)
    try:
        os.mkdir(path)
    except:
        print('Уже создан!')
    for i in list_adress:
        file = str(parent + str(file_name) + '/' + i['name'])
        with open(file, "w", encoding="utf-8") as f:
            s = '<Ads formatVersion="3" target="Avito.ru">'
            f.write(s)
            f.close()
        with open(file, "a", encoding='utf-8') as f:
            for context in contexts:
                s = write_text(context, i)
                f.write(s)
            f.write('</Ads>')
        f.close()
    # print('end')
    # print(time)


def sorts(contexts):
    ads = []
    tmp = {}
    for ad in contexts:
        if ad['title'] not in tmp.keys():
            tmp[ad['title']] = [ad]
        else:
            tmp[ad['title']].append(ad)
    result = [ad for name, ad in tmp.items()]
    while True:
        if len(result) <= 0:
            break
        for i in result:
            if len(i) > 0:
                ads.append(i[0])
                i.pop(0)
            else:
                result.remove(i)
            # print('i Осталось: ', len(i))
        # print('result Осталось: ', len(result))
    # print(result)

    return ads


def write_chel_ad(contexts):
    time = datetime.now()
    time = str(str(time.year) + '-' + str(time.month) + '-' + str(time.day))
    parent = 'Z:/IT отдел/Толя/xml/avito/'
    path = os.path.join(parent, 'готово ' + time)
    file_name = 'готово ' + time
    # print(path)
    # if path:
    #     os.mkdir(path)
    file = str(parent + str(file_name) + '/' + 'chel_chel_obl_ufa3.xml')
    with open(file, "w", encoding="utf-8") as f:
        s = '<Ads formatVersion="3" target="Avito.ru">'
        f.write(s)
        f.close()
    with open(file, "a", encoding='utf-8') as f:
        for context in contexts:
            for i in list_chel_adres:
                id = f'{context["id"]}{i["id"]}'
                wtc = f'<WorktopColor>{context["worktopColor"]}</WorktopColor>' if context['worktopColor'] else ''
                ptp = f'<ProductType>{context["productType"]}</ProductType>' if context['productType'] else ''
                ist = f'<InteriorSubType>{context["interiorSubType"]}</InteriorSubType>' if context[
                    'interiorSubType'] else ''
                cbd = f'<CanBeDisassembled>{context["canBeDisassembled"]}</CanBeDisassembled>' if context[
                    'canBeDisassembled'] else ''
                dfs = f'<DiningFurnitureSet><Option>{"</Option><Option>".join(context["diningFurnitureSet"])}' \
                      '</Option></DiningFurnitureSet>' if context['diningFurnitureSet'] else ''
                ff = f'<FurnitureFrame><Option>{context["furnitureFrame"]}</Option></FurnitureFrame>' if context[
                    'furnitureFrame'] else ''
                r = f'<GoodsSubType>{context["goodsSubType"]}</GoodsSubType>' if context['goodsSubType'] else ''
                y = f'<FurnitureType>{context["furnitureType"]}</FurnitureType>' if context['furnitureType'] else ''
                t = f'<TableType>{context["tableType"]}</TableType>' if context['tableType'] else ''
                k = f'<KitchenType>{context["kitchenType"]}</KitchenType>' if context['kitchenType'] else ''
                wm = f'<WorktopMaterial>{context["worktopMaterial"]}</WorktopMaterial>' if context[
                    'worktopMaterial'] else ''
                dw = f'<DepthByWorktop>{context["depthByWorktop"]}</DepthByWorktop>' if context[
                    'depthByWorktop'] else ''
                pt = f'<PriceType>{context["priceType"]}</PriceType>' if context['priceType'] else ''
                w = f'<WorktopIncluded>{context["worktopIncluded"]}</WorktopIncluded>' if context[
                    'worktopIncluded'] else ''
                kh = f'<KitchenShape>{context["kitchenShape"]}</KitchenShape>' if context['kitchenShape'] else ''
                u = f'<UpholsteryMaterial>{context["upholsteryMaterial"]}</UpholsteryMaterial>' if context[
                    'upholsteryMaterial'] else ''
                h = f'<HeightRegulation>{context["heightRegulation"]}</HeightRegulation>' if context[
                    "heightRegulation"] else ''
                shelving_type = f'<ShelvingType>{context["shelvingType"]}</ShelvingType>' if context[
                    "shelvingType"] else ''
                base_material = f'<BaseMaterial>{context["baseMaterial"]}</BaseMaterial>' if context[
                    'baseMaterial'] else ''
                tabletop_material = f'<TabletopMaterial>{context["tabletopMaterial"]}</TabletopMaterial>' if context[
                    'tabletopMaterial'] else ''
                furniture_shape = f'<FurnitureShape>{context["furnitureShape"]}</FurnitureShape>' if context[
                    'furnitureShape'] else ''
                folding_mechanism = f'<FoldingMechanism>{context["foldingMechanism"]}</FoldingMechanism>' if context[
                    'foldingMechanism'] else ''
                out_wear = f'<OutwearDresserType>{context["out_wear"]}</OutwearDresserType>' if context[
                    "out_wear"] else ''
                dresser_type = f'<DresserType>{context["dresserType"]}</DresserType>' if context['dresserType'] else ''
                width = f'<Width>{context["length"]}</Width>' if context['length'] and not context['length_1'] else ''
                length = f'<Length>{context["length_1"]}</Length>' if context['length_1'] else ''
                width_1 = f'<Width>{context["width_1"]}</Width>' if context['width_1'] else ''
                height = f'<Height>{context["height"]}</Height>' if context['height'] else ''
                depth = f'<Depth>{context["width"]}</Depth>' if context['width'] and not context['width_1'] else ''
                cabinetType = f'<CabinetType>{context["cabinetType"]}</CabinetType>' if context["cabinetType"] else ''
                color = f'<Color>Другой</Color>'
                fa = f'<FurnitureAdditions><Option>{"</Option><Option>".join(context["furnitureAdditions"])}' \
                     f'</Option></FurnitureAdditions>' if len(context["furnitureAdditions"]) > 0 else ''
                material = f'<Material><Option>ЛДСП</Option></Material>'
                v = f'<VideoURL>{context["video"]}</VideoURL>' if context['video'] else ''
                color_all = f'<ColorName>Венге/Белый Дуб/Белый/Серый</ColorName>' if context['colorName'] \
                    else '<ColorName>Серый/Белый/Бежевый</ColorName>'
                d = f'<DoorsMaterial><Option>{context["doorsMaterial"]}</Option></DoorsMaterial>' if context[
                    'doorsMaterial'] else ''
                delivery = f'<Delivery><Option>Свой курьер</Option></Delivery>'
                prepayment_amount = f'<PrepaymentAmount>0</PrepaymentAmount>'
                variability = f'<Variability>Несколько вариантов</Variability>'
                fS = f'<FurnitureSet><Option>{"</Option><Option>".join(context["furnitureSet"])}' \
                     '</Option></FurnitureSet>' if context['furnitureSet'] else ''
                sPL = f'<SleepingPlaceLength>{context["sleepingPlaceLength"]}</SleepingPlaceLength>' if context[
                    'sleepingPlaceLength'] else ''
                sPW = f'<SleepingPlaceWidth>{context["sleepingPlaceWidth"]}</SleepingPlaceWidth>' if context[
                    'sleepingPlaceWidth'] else ''
                lfd = f'<LengthForDelivery>{context["lengthForDelivery"]}</LengthForDelivery>' if context[
                    'lengthForDelivery'] else ''
                wfd = f'<WidthForDelivery>{context["widthForDelivery"]}</WidthForDelivery>' if context[
                    'widthForDelivery'] else ''
                hfd = f'<HeightForDelivery>{context["heightForDelivery"]}</HeightForDelivery>' if context[
                    'heightForDelivery'] else ''
                message_to_buyer = f'<MessageToBuyer>Здравствуйте! Напишите нужный размер, вариант и цвет. Если есть примеры желаемого, отправьте их тоже.</MessageToBuyer>'
                preparation_time = f'<PreparationTime>14</PreparationTime>'
                s = f'<Ad>' \
                    f'<Id>{id}</Id>' \
                    f'<AdStatus>{context["adStatus"]}</AdStatus>' \
                    f'<AllowEmail>{context["allowEmail"]}</AllowEmail>' \
                    f'<ManagerName>{context["managerName"]}</ManagerName>' \
                    f'<ContactPhone>{i["phone"]}</ContactPhone>' \
                    f'<Address>{i["city"]}</Address>' \
                    f'<Category>{context["category"]}</Category>' \
                    f'<GoodsType>{context["goodsType"]}</GoodsType>' \
                    f'{r}' \
                    f'{message_to_buyer}' \
                    f'{delivery}' \
                    f'{prepayment_amount}' \
                    f'{variability}' \
                    f'{preparation_time}' \
                    f'{dresser_type}' \
                    f'{out_wear}' \
                    f'{cabinetType}' \
                    f'{furniture_shape}' \
                    f'{folding_mechanism}' \
                    f'{tabletop_material}' \
                    f'{base_material}' \
                    f'{shelving_type}' \
                    f'{y}' \
                    f'{t}' \
                    f'{u}' \
                    f'{h}' \
                    f'{d}' \
                    f'{kh}' \
                    f'{w}' \
                    f'{ist}' \
                    f'{k}' \
                    f'{dw}' \
                    f'{ptp}' \
                    f'{wm}' \
                    f'{ff}' \
                    f'{pt}' \
                    f'{dfs}' \
                    f'{color_all}' \
                    f'{color}' \
                    f'{wtc}' \
                    f'{material}' \
                    f'{width}' \
                    f'{width_1}' \
                    f'{depth}' \
                    f'{height}' \
                    f'{length}' \
                    f'{fa}' \
                    f'{cbd}' \
                    f'{fS}' \
                    f'{sPL}' \
                    f'{sPW}' \
                    f'{lfd}' \
                    f'{wfd}' \
                    f'{hfd}' \
                    f'<Condition>Новое</Condition>' \
                    f'<Availability>В наличии</Availability>' \
                    f'<Title>{context["title"]}</Title>' \
                    f'<Color>Другой</Color>' \
                    f'<Stock>100</Stock>' \
                    f'<AdType>Товар произведён мной</AdType>' \
                    f'<Description><![CDATA[{context["description"]}]]></Description>' \
                    f'<Price>{context["price"]}</Price>' \
                    f'<Images>' \
                    f'<Image url={"/><Image url=".join(context["images"])}/>' \
                    f'</Images>' \
                    f'{v}' \
                    f'</Ad>'
                f.write(s)
        f.write('</Ads>')
    f.close()
    # print('end')
    # print(time)


def write_ekat_tumen(contexts):
    time = datetime.now()
    time = str(str(time.year) + '-' + str(time.month) + '-' + str(time.day))
    parent = 'Z:/IT отдел/Толя/xml/avito/'
    path = os.path.join(parent, 'готово ' + time)
    file_name = 'готово ' + time
    # print(path)
    # if path:
    #     os.mkdir(path)
    file = str(parent + str(file_name) + '/' + 'ekat_new2.xml')
    with open(file, "w", encoding="utf-8") as f:
        s = '<Ads formatVersion="3" target="Avito.ru">'
        f.write(s)
        f.close()
    with open(file, "a", encoding='utf-8') as f:
        for context in contexts:
            for i in list_ekat_tumen:
                id = f'{context["id"]}{i["id"]}'
                wtc = f'<WorktopColor>{context["worktopColor"]}</WorktopColor>' if context['worktopColor'] else ''
                ptp = f'<ProductType>{context["productType"]}</ProductType' if context['productType'] else ''
                ist = f'<InteriorSubType>{context["interiorSubType"]}</InteriorSubType>' if context[
                    'interiorSubType'] else ''
                cbd = f'<CanBeDisassembled>{context["canBeDisassembled"]}</CanBeDisassembled>' if context[
                    'canBeDisassembled'] else ''
                dfs = f'<DiningFurnitureSet><Option>{"</Option><Option>".join(context["diningFurnitureSet"])}' \
                      '</Option></DiningFurnitureSet>' if context['diningFurnitureSet'] else ''
                ff = f'<FurnitureFrame><Option>{context["furnitureFrame"]}</Option></FurnitureFrame>' if context[
                    'furnitureFrame'] else ''
                r = f'<GoodsSubType>{context["goodsSubType"]}</GoodsSubType>' if context['goodsSubType'] else ''
                y = f'<FurnitureType>{context["furnitureType"]}</FurnitureType>' if context['furnitureType'] else ''
                t = f'<TableType>{context["tableType"]}</TableType>' if context['tableType'] else ''
                k = f'<KitchenType>{context["kitchenType"]}</KitchenType>' if context['kitchenType'] else ''
                pt = f'<PriceType>{context["priceType"]}</PriceType>' if context['priceType'] else ''
                dw = f'<DepthByWorktop>{context["depthByWorktop"]}</DepthByWorktop>' if context[
                    'depthByWorktop'] else ''
                kh = f'<KitchenShape>{context["kitchenShape"]}</KitchenShape>' if context['kitchenShape'] else ''
                wm = f'<WorktopMaterial>{context["worktopMaterial"]}</WorktopMaterial>' if context[
                    'worktopMaterial'] else ''
                w = f'<WorktopIncluded>{context["worktopIncluded"]}</WorktopIncluded>' if context[
                    'worktopIncluded'] else ''
                u = f'<UpholsteryMaterial>{context["upholsteryMaterial"]}</UpholsteryMaterial>' if context[
                    'upholsteryMaterial'] else ''
                h = f'<HeightRegulation>{context["heightRegulation"]}</HeightRegulation>' if context[
                    "heightRegulation"] else ''
                shelving_type = f'<ShelvingType>{context["shelvingType"]}</ShelvingType>' if context[
                    "shelvingType"] else ''
                base_material = f'<BaseMaterial>{context["baseMaterial"]}</BaseMaterial>' if context[
                    'baseMaterial'] else ''
                tabletop_material = f'<TabletopMaterial>{context["tabletopMaterial"]}</TabletopMaterial>' if context[
                    'tabletopMaterial'] else ''
                furniture_shape = f'<FurnitureShape>{context["furnitureShape"]}</FurnitureShape>' if context[
                    'furnitureShape'] else ''
                folding_mechanism = f'<FoldingMechanism>{context["foldingMechanism"]}</FoldingMechanism>' if context[
                    'foldingMechanism'] else ''
                out_wear = f'<OutwearDresserType>{context["out_wear"]}</OutwearDresserType>' if context[
                    "out_wear"] else ''
                dresser_type = f'<DresserType>{context["dresserType"]}</DresserType>' if context['dresserType'] else ''
                width = f'<Width>{context["length"]}</Width>' if context['length'] and not context['length_1'] else ''
                length = f'<Length>{context["length_1"]}</Length>' if context['length_1'] else ''
                width_1 = f'<Width>{context["width_1"]}</Width>' if context['width_1'] else ''
                height = f'<Height>{context["height"]}</Height>' if context['height'] else ''
                depth = f'<Depth>{context["width"]}</Depth>' if context['width'] and not context['width_1'] else ''
                cabinetType = f'<CabinetType>{context["cabinetType"]}</CabinetType>' if context["cabinetType"] else ''
                color = f'<Color>Другой</Color>'
                fa = f'<FurnitureAdditions><Option>{"</Option><Option>".join(context["furnitureAdditions"])}' \
                     f'</Option></FurnitureAdditions>' if len(context["furnitureAdditions"]) > 0 else ''
                material = f'<Material><Option>ЛДСП</Option></Material>'
                v = f'<VideoURL>{context["video"]}</VideoURL>' if context['video'] else ''
                color_all = f'<ColorName>Венге/Белый Дуб/Белый/Серый</ColorName>' if context['colorName'] \
                    else '<ColorName>Серый/Белый/Бежевый</ColorName>'
                d = f'<DoorsMaterial><Option>{context["doorsMaterial"]}</Option></DoorsMaterial>' if context[
                    'doorsMaterial'] else ''
                delivery = f'<Delivery><Option>Свой курьер</Option></Delivery>'
                prepayment_amount = f'<PrepaymentAmount>0</PrepaymentAmount>'
                variability = f'<Variability>Несколько вариантов</Variability>'
                fS = f'<FurnitureSet><Option>{"</Option><Option>".join(context["furnitureSet"])}' \
                     '</Option></FurnitureSet>' if context['furnitureSet'] else ''
                sPL = f'<SleepingPlaceLength>{context["sleepingPlaceLength"]}</SleepingPlaceLength>' if context[
                    'sleepingPlaceLength'] else ''
                sPW = f'<SleepingPlaceWidth>{context["sleepingPlaceWidth"]}</SleepingPlaceWidth>' if context[
                    'sleepingPlaceWidth'] else ''
                lfd = f'<LengthForDelivery>{context["lengthForDelivery"]}</LengthForDelivery>' if context[
                    'lengthForDelivery'] else ''
                wfd = f'<WidthForDelivery>{context["widthForDelivery"]}</WidthForDelivery>' if context[
                    'widthForDelivery'] else ''
                hfd = f'<HeightForDelivery>{context["heightForDelivery"]}</HeightForDelivery>' if context[
                    'heightForDelivery'] else ''
                message_to_buyer = f'<MessageToBuyer>Здравствуйте! Напишите нужный размер, вариант и цвет. Если есть примеры желаемого, отправьте их тоже.</MessageToBuyer>'
                preparation_time = f'<PreparationTime>14</PreparationTime>'
                s = f'<Ad>' \
                    f'<Id>{id}</Id>' \
                    f'<AdStatus>{context["adStatus"]}</AdStatus>' \
                    f'<AllowEmail>{context["allowEmail"]}</AllowEmail>' \
                    f'<ManagerName>{context["managerName"]}</ManagerName>' \
                    f'<ContactPhone>{i["phone"]}</ContactPhone>' \
                    f'<Address>{i["city"]}</Address>' \
                    f'<Category>{context["category"]}</Category>' \
                    f'<GoodsType>{context["goodsType"]}</GoodsType>' \
                    f'{message_to_buyer}' \
                    f'{delivery}' \
                    f'{prepayment_amount}' \
                    f'{variability}' \
                    f'{preparation_time}' \
                    f'{r}' \
                    f'{dresser_type}' \
                    f'{out_wear}' \
                    f'{cabinetType}' \
                    f'{furniture_shape}' \
                    f'{folding_mechanism}' \
                    f'{tabletop_material}' \
                    f'{base_material}' \
                    f'{shelving_type}' \
                    f'{y}' \
                    f'{t}' \
                    f'{u}' \
                    f'{h}' \
                    f'{d}' \
                    f'{kh}' \
                    f'{w}' \
                    f'{dw}' \
                    f'{ptp}' \
                    f'{wm}' \
                    f'{k}' \
                    f'{ist}' \
                    f'{ff}' \
                    f'{pt}' \
                    f'{dfs}' \
                    f'{color_all}' \
                    f'{color}' \
                    f'{wtc}' \
                    f'{material}' \
                    f'{width}' \
                    f'{width_1}' \
                    f'{depth}' \
                    f'{height}' \
                    f'{length}' \
                    f'{fa}' \
                    f'{cbd}' \
                    f'{fS}' \
                    f'{sPL}' \
                    f'{sPW}' \
                    f'{lfd}' \
                    f'{wfd}' \
                    f'{hfd}' \
                    f'<Condition>Новое</Condition>' \
                    f'<Availability>В наличии</Availability>' \
                    f'<Title>{context["title"]}</Title>' \
                    f'<Color>Другой</Color>' \
                    f'<Stock>100</Stock>' \
                    f'<AdType>Товар произведён мной</AdType>' \
                    f'<Description><![CDATA[{context["description"]}]]></Description>' \
                    f'<Price>{context["price"]}</Price>' \
                    f'<Images>' \
                    f'<Image url={"/><Image url=".join(context["images"])}/>' \
                    f'</Images>' \
                    f'{v}' \
                    f'</Ad>'
                f.write(s)
        f.write('</Ads>')
    f.close()
    # print('end')
    # print(time)


def write_all_chel_ad(contexts):
    time = datetime.now()
    time = str(str(time.year) + '-' + str(time.month) + '-' + str(time.day))
    parent = 'Z:/IT отдел/Толя/xml/avito/'
    path = os.path.join(parent, 'готово ' + time)
    file_name = 'готово ' + time
    # print(path)
    # if path:
    #     os.mkdir(path)
    file = str(parent + str(file_name) + '/' + 'all_chel3.xml')
    with open(file, "w", encoding="utf-8") as f:
        s = '<Ads formatVersion="3" target="Avito.ru">'
        f.write(s)
        f.close()
    with open(file, "a", encoding='utf-8') as f:
        for context in contexts:
            for i in list_all_chel_adress:
                id = f'{context["id"]}{i["id"]}'
                wtc = f'<WorktopColor>{context["worktopColor"]}</WorktopColor>' if context['worktopColor'] else ''
                ptp = f'<ProductType>{context["productType"]}</ProductType>' if context["productType"] else ''
                ist = f'<InteriorSubType>{context["interiorSubType"]}</InteriorSubType>' if context[
                    'interiorSubType'] else ''
                cbd = f'<CanBeDisassembled>{context["canBeDisassembled"]}</CanBeDisassembled>' if context[
                    'canBeDisassembled'] else ''
                dfs = f'<DiningFurnitureSet><Option>{"</Option><Option>".join(context["diningFurnitureSet"])}' \
                      '</Option></DiningFurnitureSet>' if context['diningFurnitureSet'] else ''
                ff = f'<FurnitureFrame><Option>{context["furnitureFrame"]}</Option></FurnitureFrame>' if context[
                    'furnitureFrame'] else ''
                r = f'<GoodsSubType>{context["goodsSubType"]}</GoodsSubType>' if context['goodsSubType'] else ''
                y = f'<FurnitureType>{context["furnitureType"]}</FurnitureType>' if context['furnitureType'] else ''
                t = f'<TableType>{context["tableType"]}</TableType>' if context['tableType'] else ''
                k = f'<KitchenType>{context["kitchenType"]}</KitchenType>' if context['kitchenType'] else ''
                wm = f'<WorktopMaterial>{context["worktopMaterial"]}</WorktopMaterial>' if context[
                    'worktopMaterial'] else ''
                dw = f'<DepthByWorktop>{context["depthByWorktop"]}</DepthByWorktop>' if context[
                    'depthByWorktop'] else ''
                pt = f'<PriceType>{context["priceType"]}</PriceType>' if context['priceType'] else ''
                w = f'<WorktopIncluded>{context["worktopIncluded"]}</WorktopIncluded>' if context[
                    'worktopIncluded'] else ''
                kh = f'<KitchenShape>{context["kitchenShape"]}</KitchenShape>' if context['kitchenShape'] else ''
                u = f'<UpholsteryMaterial>{context["upholsteryMaterial"]}</UpholsteryMaterial>' if context[
                    'upholsteryMaterial'] else ''
                h = f'<HeightRegulation>{context["heightRegulation"]}</HeightRegulation>' if context[
                    "heightRegulation"] else ''
                shelving_type = f'<ShelvingType>{context["shelvingType"]}</ShelvingType>' if context[
                    "shelvingType"] else ''
                base_material = f'<BaseMaterial>{context["baseMaterial"]}</BaseMaterial>' if context[
                    'baseMaterial'] else ''
                tabletop_material = f'<TabletopMaterial>{context["tabletopMaterial"]}</TabletopMaterial>' if context[
                    'tabletopMaterial'] else ''
                furniture_shape = f'<FurnitureShape>{context["furnitureShape"]}</FurnitureShape>' if context[
                    'furnitureShape'] else ''
                folding_mechanism = f'<FoldingMechanism>{context["foldingMechanism"]}</FoldingMechanism>' if context[
                    'foldingMechanism'] else ''
                out_wear = f'<OutwearDresserType>{context["out_wear"]}</OutwearDresserType>' if context[
                    "out_wear"] else ''
                dresser_type = f'<DresserType>{context["dresserType"]}</DresserType>' if context['dresserType'] else ''
                width = f'<Width>{context["length"]}</Width>' if context['length'] and not context['length_1'] else ''
                length = f'<Length>{context["length_1"]}</Length>' if context['length_1'] else ''
                width_1 = f'<Width>{context["width_1"]}</Width>' if context['width_1'] else ''
                height = f'<Height>{context["height"]}</Height>' if context['height'] else ''
                depth = f'<Depth>{context["width"]}</Depth>' if context['width'] and not context['width_1'] else ''
                cabinetType = f'<CabinetType>{context["cabinetType"]}</CabinetType>' if context["cabinetType"] else ''
                color = f'<Color>Другой</Color>'
                fa = f'<FurnitureAdditions><Option>{"</Option><Option>".join(context["furnitureAdditions"])}' \
                     f'</Option></FurnitureAdditions>' if len(context["furnitureAdditions"]) > 0 else ''
                material = f'<Material><Option>ЛДСП</Option></Material>'
                v = f'<VideoURL>{context["video"]}</VideoURL>' if context['video'] else ''
                color_all = f'<ColorName>Венге/Белый Дуб/Белый/Серый</ColorName>' if context['colorName'] \
                    else '<ColorName>Серый/Белый/Бежевый</ColorName>'
                d = f'<DoorsMaterial><Option>{context["doorsMaterial"]}</Option></DoorsMaterial>' if context[
                    'doorsMaterial'] else ''
                delivery = f'<Delivery><Option>Свой курьер</Option></Delivery>'
                prepayment_amount = f'<PrepaymentAmount>0</PrepaymentAmount>'
                variability = f'<Variability>Несколько вариантов</Variability>'
                fS = f'<FurnitureSet><Option>{"</Option><Option>".join(context["furnitureSet"])}' \
                     '</Option></FurnitureSet>' if context['furnitureSet'] else ''
                sPL = f'<SleepingPlaceLength>{context["sleepingPlaceLength"]}</SleepingPlaceLength>' if context[
                    'sleepingPlaceLength'] else ''
                sPW = f'<SleepingPlaceWidth>{context["sleepingPlaceWidth"]}</SleepingPlaceWidth>' if context[
                    'sleepingPlaceWidth'] else ''
                lfd = f'<LengthForDelivery>{context["lengthForDelivery"]}</LengthForDelivery>' if context[
                    'lengthForDelivery'] else ''
                wfd = f'<WidthForDelivery>{context["widthForDelivery"]}</WidthForDelivery>' if context[
                    'widthForDelivery'] else ''
                hfd = f'<HeightForDelivery>{context["heightForDelivery"]}</HeightForDelivery>' if context[
                    'heightForDelivery'] else ''
                message_to_buyer = f'<MessageToBuyer>Здравствуйте! Напишите нужный размер, вариант и цвет. Если есть примеры желаемого, отправьте их тоже.</MessageToBuyer>'
                preparation_time = f'<PreparationTime>14</PreparationTime>'
                s = f'<Ad>' \
                    f'<Id>{id}</Id>' \
                    f'<AdStatus>{context["adStatus"]}</AdStatus>' \
                    f'<AllowEmail>{context["allowEmail"]}</AllowEmail>' \
                    f'<ManagerName>{context["managerName"]}</ManagerName>' \
                    f'<ContactPhone>{i["phone"]}</ContactPhone>' \
                    f'<Address>{i["city"]}</Address>' \
                    f'<Category>{context["category"]}</Category>' \
                    f'<GoodsType>{context["goodsType"]}</GoodsType>' \
                    f'{r}' \
                    f'{message_to_buyer}' \
                    f'{delivery}' \
                    f'{prepayment_amount}' \
                    f'{variability}' \
                    f'{preparation_time}' \
                    f'{dresser_type}' \
                    f'{out_wear}' \
                    f'{cabinetType}' \
                    f'{furniture_shape}' \
                    f'{folding_mechanism}' \
                    f'{tabletop_material}' \
                    f'{base_material}' \
                    f'{shelving_type}' \
                    f'{y}' \
                    f'{t}' \
                    f'{u}' \
                    f'{h}' \
                    f'{d}' \
                    f'{kh}' \
                    f'{w}' \
                    f'{k}' \
                    f'{dw}' \
                    f'{ptp}' \
                    f'{wm}' \
                    f'{ist}' \
                    f'{ff}' \
                    f'{pt}' \
                    f'{dfs}' \
                    f'{color_all}' \
                    f'{color}' \
                    f'{wtc}' \
                    f'{material}' \
                    f'{width}' \
                    f'{width_1}' \
                    f'{depth}' \
                    f'{height}' \
                    f'{length}' \
                    f'{fa}' \
                    f'{cbd}' \
                    f'{fS}' \
                    f'{sPL}' \
                    f'{sPW}' \
                    f'{lfd}' \
                    f'{wfd}' \
                    f'{hfd}' \
                    f'<Condition>Новое</Condition>' \
                    f'<Availability>В наличии</Availability>' \
                    f'<Title>{context["title"]}</Title>' \
                    f'<Color>Другой</Color>' \
                    f'<Stock>100</Stock>' \
                    f'<AdType>Товар произведён мной</AdType>' \
                    f'<Description><![CDATA[{context["description"]}]]></Description>' \
                    f'<Price>{context["price"]}</Price>' \
                    f'<Images>' \
                    f'<Image url={"/><Image url=".join(context["images"])}/>' \
                    f'</Images>' \
                    f'{v}' \
                    f'</Ad>'
                f.write(s)
        f.write('</Ads>')
    f.close()
    # print('end')
    # print(time)


def main():
    # file_name = str(input('Введите имя файла: '))
    # file_name = 'avitofeed_108 (2).xml'
    file_name = 'ekat.xml'
    root = open_file(file_name)
    contexts = ads_update(root)
    contexts = sorts(contexts)
    write_ad(contexts)
    write_chel_ad(contexts)
    write_ekat_tumen(contexts)
    write_all_chel_ad(contexts)
    print(f'len contexts: {len(contexts)}')
    print('error', list_error_title)


if __name__ == '__main__':
    main()

# avitofeed_108.xml

# image/catalog/10_komods/QR_komod/155.png
