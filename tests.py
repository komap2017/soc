import unittest
from soc import check_phrase_for_girl, check_phrase_for_city


class Testing(unittest.TestCase):
    def test_check(self):
        self.assertEqual(check_phrase_for_girl('ДС/Москва, 21, парень.'), False)
        self.assertEqual(check_phrase_for_girl('1. Дс, 17, кун'), False)
        self.assertEqual(check_phrase_for_girl('1. Подмосковье, 27, М (могу погулять по ДС в какую-нибудь суббоотку)'),
                         False)
        self.assertEqual(check_phrase_for_girl('Кун, скоро 20, дс.'), False)
        self.assertEqual(check_phrase_for_girl('овердроч со скайпом прямо сейчас'), False)
        self.assertEqual(check_phrase_for_girl('1. Минск, 19, М'), False)
        self.assertEqual(check_phrase_for_girl('20, тян, мск. скучно сидеть дома. угостите кто-нибудь мороюенным'), True)
        self.assertEqual(check_phrase_for_girl('Тян, 20 лет'), True)
        self.assertEqual(check_phrase_for_girl('Я хочу играть. Мне плевать кто ты- девочка,'
                                               ' мальчик, трансгендерный флюидный хуесос. Отношения и секс-это лава, '
                                               'сквиртую от своих потг. Единственное, что важно- '
                                               'ты играешь в овервоч и '
                                               'вытащишь меня из бронзового рака в мастера. Я буду учиться, сенпай. '
                                               'В идеале, ты говоришь на английском (джаст фо практис). '
                                               'Лучше бы ты была телочкой. '
                                               'Хочу подружку-задротку(будем няшиться с тобой в лунных колодцах на ваниле).  '
                                               'С меня ахуенные истории. Шутка, я не говорю во время игры. '
                                               'Тян. 19. Арстотцка. '
                                               '@Golovalluvazuahui'), True)
        self.assertEqual(check_phrase_for_girl('Познакомлюсь с парнем старше 25 @tg8888'), True)
        self.assertEqual(check_phrase_for_girl('ПоцbIк из Мацквы, 20 раз тянули за уши.'), False)
        self.assertEqual(check_phrase_for_girl('Познакомлюсь с парнем старше 25'), True)
        self.assertEqual(check_phrase_for_girl('Хуеносец, 25. Всё проебано, пфф, классика.'), False)
        self.assertEqual(check_phrase_for_girl('ДС  20 ж'), True)
        self.assertEqual(check_phrase_for_girl('ж, 18, ленобл'), True)
        self.assertEqual(check_phrase_for_girl('1. Санкт-Петербург, Питер, ДС-2 / 21 год / мужской'), False)
        self.assertEqual(check_phrase_for_girl('1. Санкт-Петербург.  Женский'), True)
        self.assertEqual(check_phrase_for_girl('1. Сарапул (или Ижевск)'), False)
        self.assertEqual(check_phrase_for_girl('Тебе надоела жизнь, хочется поговорить?'), False)
        self.assertEqual(check_phrase_for_girl('Ж,19.'), True)
        self.assertEqual(check_phrase_for_girl('Тня. 24'), True)
        self.assertEqual(check_phrase_for_girl('Тян,дс'), True)
        self.assertEqual(check_phrase_for_girl('1) Женщина, 23, Москва'), True)
        self.assertEqual(check_phrase_for_girl('1.18,ж.'), True)
        self.assertEqual(check_phrase_for_girl('1.тян,18'), True)
        self.assertEqual(check_phrase_for_girl('Рок-тяночка 25 лет ищет доброго и интересного куника 25-35 лет.'
                                               'На фото я снимаюсь в клипе любимой группы ^-^'), True)
        self.assertEqual(check_phrase_for_girl('Т-тян, 18 лет, не всрата (оч даже мила), из ДС. Ищу куна из ДС до 20'
                         'лвла (если ты би/пан, то кульно). О себе расскажу в телеге - @sadirtop'), True)
        self.assertEqual(check_phrase_for_girl('Так хочется парня.... 24+ худые, несамодостаточные  неадекватные карланы мимо'), True)
        self.assertEqual(check_phrase_for_girl('тнус, 20+ СПБ'), True)
        self.assertEqual(check_phrase_for_girl('девочка, 17 лет, приезжаю на день в дс завтра'), True)
        self.assertEqual(check_phrase_for_girl('1. До недавнего времени была девушкой, Краков, 18 годиков.'), True)
        self.assertEqual(check_phrase_for_girl('меня зовут Арина'), True)
        self.assertEqual(check_phrase_for_girl('О себе: молодая особа женского пола.'), True)
        self.assertEqual(check_phrase_for_girl('Алиса, 16 лет, Москва'), True)
        self.assertEqual(check_phrase_for_girl('Хочу пообщаться с каким нибудь котиком. Киса, 18 лет.'), True)
        self.assertEqual(check_phrase_for_girl('Настена (оч люблю, когда так называют)'), True)
        self.assertEqual(check_phrase_for_girl('приветик, что мне не спится. Расскажешь сказку на ночь 19летней девушке? '), True)
        self.assertEqual(check_phrase_for_girl('1. Тянучка, 20 лвл, Новосибирск'), True)
        self.assertEqual(check_phrase_for_girl('Девчуля, 19,Санкт-Петербург'), True)
        self.assertEqual(check_phrase_for_girl('18, тянозавр, место обитания значения не имеет'
                                               '— все равно не пересечемся. '
                                               'Ониме, пустой треп, кулстори (не такие уж и кул) из ирл'
                                               'и не только. Возможно, на одну ночь,'
                                               'а мб и дольше. Все это неважно, просто хочу иногда'
                                               'с кем-то говорить.'), True)
        self.assertEqual(check_phrase_for_girl('Тянка, 17 лет с: '), True)
        self.assertEqual(check_phrase_for_girl('Дс, 17 lvl, тянучка'), True)
        self.assertEqual(check_phrase_for_girl('Добрейший вечерочек всем жителям ЗАО'
                                               'Москвы. Хотел пройтись сегодня и нагулять'
                                               'сон - да все друзья посливались как пуссиплейеры.'
                                               'Поэтому необычное предложение всем, кто тоже не против вот так внезапно'
                                               'прямо сейчас побродить по любимому Фили'
                                               '(для тян, которые опасаются, что я маньячина'
                                               'честно обещаю ходить только по освещенным улицам,'
                                               'где есть народ).'), False)
        self.assertEqual(check_phrase_for_girl('Как известно, тян в интернетах нет, а если '
                                               'и есть одна, то напишет она точно не мне, тут же '
                                               'столько кунов и ДС-2 куда лучше меня. Но тем не менее, я тоже намерен '
                                               'попытать счастье. Не то, чтобы я в свои 25 верил в чудеса, но бывают'
                                               ' же счастливые совпадения! Итак, я обычный двощер из Питера,'
                                               ' безработный, есть проблемы с лишним весом, короче '
                                               'всё как вы любите. Угощу свободную девушку '
                                               'шавермой на следующей неделе, а пока '
                                               'пообщаемся в Сети?'), False)
        self.assertEqual(check_phrase_for_girl('Расстался со своей тян, очень подавленное состояние.'), False)
        self.assertEqual(check_phrase_for_girl('Познакомлюсь с годной тян- би) можно и с '
                                               'кунами любящими укуриться и поржать с чего'
                                               ' нибудь запредельно неадекватного)'), False)
        self.assertEqual(check_phrase_for_girl('Ищу похожую на себя тян, которая сможет дарить свою любовь и заботу. Взамен буду отдавать то же самое.'), False)
        self.assertEqual(check_phrase_for_girl('М,24, ищу тян с которой можно лампово поболтать за чашкой чая в кафе или погулять и сходить на каток.Без отношений.ТГ-Assumption1993'), False)
        self.assertEqual(check_phrase_for_girl('Ищу необщительную занудную быдло-хикку-тян для общения в реале, ДС. Без друзей-тусовок, с большим количеством свободного времени, но только не няшечку, увлекающуюся игрулечками и анимой, а попроще, без компьютерных околобордовских интересов.'), False)
        self.assertEqual(check_phrase_for_girl('Дс. М24. Приглашаю 1 тян на посмотреть warcraft, с каким нибудь продолжением'), False)
        self.assertEqual(check_phrase_for_girl('ДС, Нужна тян >17'), False)
        self.assertEqual(check_phrase_for_girl('1. Не тян, 22, Одесса'), False)
        self.assertEqual(check_phrase_for_girl('Эх, как же хочется сочненькую, загорелую, не очень скромную, развратную в душе, с сиськами, небольшими ступнями, темными волосами, недотраханную шлюшку, без парня или ебыря, одновременно мечтающую о партнере, чтобы зашел к ней в вагину и прочие отверстия своим твердым горячим елдаком, но ничего не порвал по возможности, дабы вместе с ним изолироваться от неприятного социума и предаваться безудержному грубому сексу...'), False)
        self.assertEqual(check_phrase_for_girl('Самка, 18, Пушкино, Ивантеевка, Щелково'), True)
        self.assertEqual(check_phrase_for_girl('Две лоли, ищем кого-нибудь поболтать и поиграть в GM'), True)
        self.assertEqual(check_phrase_for_girl('Tyan 18 lvl'), True)
        self.assertEqual(check_phrase_for_girl('Меня зовут Александра и я с Иркутска, ищу кунца или друзей '), True)
        self.assertEqual(check_phrase_for_girl('вжух и я нашла куна из киева'), True)
        self.assertEqual(check_phrase_for_girl('пожалуйста напиши мне я 22 летняя bbw'), True)
        self.assertEqual(check_phrase_for_girl('1. Около Караганда (Казахстан), 16, female.'), True)
        self.assertEqual(check_phrase_for_girl('Пухлоняша ищет жильё в дс'), True)
        self.assertEqual(check_phrase_for_girl('Срочно! Разыскиваются 2 чувака (чувак и его друг) для увеселения в злачных заведениях с двумя тянями в Питере сегодня вечером'), True)
        self.assertEqual(check_phrase_for_girl('Компания тянучек в данный момент пьет шампанское и ищет приятного ирл собеседника до вечера. Москва, СВАО'), True)
        self.assertEqual(check_phrase_for_girl('1. Анкетку прикрепила, сделала буквально за 3 минуты'), True)
        self.assertEqual(check_phrase_for_girl('17, дс, тянЫЫЫ'), True)
        self.assertEqual(check_phrase_for_girl('1. Козочка молоденькая 14 лет'), True)
        self.assertEqual(check_phrase_for_girl('Прив, ищу тян, мне 17. Интересов не так много, но может найдем что-то общее, кис:з Напиши мне, сам стесняюсь<3'), False)
        self.assertEqual(check_phrase_for_girl('16-летняя гёрлза из Украины. '), True)
        self.assertEqual(check_phrase_for_girl('Кто-нибудь может одолжить страницу, желательно заброшенную/ненужную вам? Не насовсем.  Буду очень признательна.'), True)
        self.assertEqual(check_phrase_for_girl('Молодая девятнадцати лет хочет зависти себе друзей. Спредложениями обращаться по адресу: Большая Пирожная улица, дом 15, корпус Ы. Звонить три с половиной раза.'), True)
        self.assertEqual(check_phrase_for_girl('Ищу себе семпая, чтобы мило общаться :3 Город не важен, все равно в августе куда-нибудь поеду, может найду как раз куда. Лвл 19, увлечений огромное множество, все стандартно. Мой вконтач: '), True)
        self.assertEqual(check_phrase_for_girl('Хочется, чтобы меня немножко пожурили, погладили по голове и сказали что-то ласковое :3'), True)
        self.assertEqual(check_phrase_for_girl('23, тиан, изгаиль'), True)
        self.assertEqual(check_phrase_for_girl('Спустя пол года я снова пришел в соц, чтобы найти тян-друга.'), False)
        self.assertEqual(check_phrase_for_girl('Обладаю вагиной и не в состоянии контролировать свои порывы вниманиеблядства (дико извиняюсь) 19 ДС'), True)
        self.assertEqual(check_phrase_for_girl('.украинский, около 20, барышня'), True)
        self.assertEqual(check_phrase_for_girl('1. телка, остальное неважно'), True)
        self.assertEqual(check_phrase_for_girl('Тебе тоже надоели эти унылые анкеты одна за другой? Ты ищешь беседы с уверенным, полноценным человеком, а не нытиком-который устал сам от себя. Тогда пиши мне! Я тян и умею разжечь интерес в диалоге, но только если ты тоже не сидишь овощем (исключительно 22+). '), True)
        self.assertEqual(check_phrase_for_girl('1. Несовершеннолетняя коза'), True)
        self.assertEqual(check_phrase_for_girl('Киевский анон ищет тян для общения и прогулок. Не всрат, работаю, часто убиваю время просмотром сериалов, аним. Немного конфоблядь, зато могу поддержать любой разговор и со мной не скучно. Вообщем, лето то оно кончается, ищу с кем можно было бы выбраться на выходные погулять в парке или сходить на разные мероприятия коих в Киеве полно. '), False)
        self.assertEqual(check_phrase_for_girl('Тянок, та, которая может в увлекательную беседу и порадовать глаз. Приветствую и тянов, и кунов. Интересует голосач как имитация живого общения, но можно и текстом. Исключительно 22-23+, без нытья, заморочек и стеснения. Сама не хикке-домосед, приветствую таких же'), True)
        self.assertEqual(check_phrase_for_girl('Когда мне было семь лет, я мечтала о том, чтобы купить второе ведро для мусора и ящик для '), True)
        self.assertEqual(check_phrase_for_girl('Тиан. Ищу тебя. Обычно отвечаю на анкетки, но тут лень, и захотелось, чтобы кто-то ответил мне. Хочу поболтать, но если усну во время переписки (я устала), не обижайся.'), True)
        self.assertEqual(check_phrase_for_girl('Новосибирск. Ищу красивого куна для секса (окей, для friendship with benefits). Будьте честны с собой: посмотрите в зеркало на своё лицо и тело, если там дохуя лишнего жира, маленькие невыразительные глазки, кривой нос, впалая грудь, жуткий прикус, или ещё какая-то хуйня, то не надо мне писать. Возраст от 21 до 28, европейская внешность, сочетание карих глаз с тёмными волосами и смугловатой кожей тоже не приемлю.'), True)
        self.assertEqual(check_phrase_for_girl('Жируха (примерно как '), True)
        self.assertEqual(check_phrase_for_girl('нравится учить жизни? счиаешь себя мудрым? Ну так помоги пожалуйства маленькой 17 летней девочке, которая стоит на распутье и не знает, что ей делать '), True)
        self.assertEqual(check_phrase_for_girl('1. Саратовы, 18, жинка'), True)
        self.assertEqual(check_phrase_for_girl('если вы не верите, то проходите мимо, это ваше право! привет, мен зовут елизавета мне 24 года я из ижевска, устраиваюсь на след неделе на новую работу, нет денег на еду и продукты, прошу вас помогите мне деньгами,у меня завтра день рождения, и нет денег ни на что(( очень грустно . 500 или 1000 рублей смогут очень помочь!! перечислите на карту сбербанк 4276680012376842,виртом не занимаюсь и голые фото не высылаю, надеюсь на человеческую доброту! \я могу подтвердить свою личность пишите мне в вибер 7+951191(5884)'), True)
        self.assertEqual(check_phrase_for_girl('Престарелый аутист, ДС-2, познакомлюсь с тян 21+ для вдохновения.'), False)
        self.assertEqual(check_phrase_for_girl('дс 21 всратая нят.'), True)
        self.assertEqual(check_phrase_for_girl('Жируха (примерно как '), True)
        self.assertEqual(check_phrase_for_girl('Ладно, двач, я поняла шо нужно быть проще и все такоэ. Короче. Ищу тню для прогулок, общения и (возможно) дружбы. Дс. Я добрая, отходчивая, смешная ('), True)
        self.assertEqual(check_phrase_for_girl('Двум тянам очень нужно вписаться в ДС-2 в ночь с 11 на 12 июля!Накормим вкусняшками, расскажем истории, можно выпить) Будем очень благодарны, хуй сость не будем:3'), True)
        self.assertEqual(check_phrase_for_girl('Барышня пообщается с кем-нибудь в интернетиках. О себе - в беседе.'), True)
        self.assertEqual(check_phrase_for_girl('Не знаю, как начать. Знаю, что нужно как обычно. Но я очень подвержена влиянием аниме. Это так странно. Посмотрев одно, я немного грущу, завтра все пройдет, потому что мне на работу, а там нет времени грустить, то хочется спать, то читать, а то и работать нужно. Но о чем я... '), True)
        self.assertEqual(check_phrase_for_girl('Як мене всё заибало и оч приятно после сего понимать что больше некуда идти за утешением кроме как на эту помойку рандома. Короче пиши если ты действительно альфа претендующий на переворот игры, наркотики и тантра вот чем мы будем заниматься. Я действительно охуевшая королевишна способная на многое так что омегам не стоит тратить свою бессмысленность на меня идите лучше выпилитесь. @kukusiki Город дс2 но мне кажется что будь я с другой вселенной маятник бы не покачнулся.'), True)
        self.assertEqual(check_phrase_for_girl('Я оказалась в Москве, города не знаю. Если у кого-нибудь есть желание этой ночью где-нибудь засесть где-нибудь или что-то в этом роде, то прошу, напишите мне в телегу.'), True)
        self.assertEqual(check_phrase_for_girl('Male ищу Female сходить на выставку Искусства Японии в Кремле на этих выходных.'), False)
        self.assertEqual(check_phrase_for_girl('тяна с дс. 20 годиков. ищу с кем поговорить и возможно выкатиться погулять.'), True)
        self.assertEqual(check_phrase_for_girl('Дорогой друг, если ты делаешь пошароебиться по ДС несмотря на погоду, то пиши же скорее, пока у меня не села мобила! :)'), True)
        self.assertEqual(check_phrase_for_girl('я знаю только, кем я была, когда встала сегодня утром, но я думаю, что с тех пор мне пришлось не раз измениться. '), True)
        self.assertEqual(check_phrase_for_girl('Года четыре назад постил сюда анкетку на "просто поболтать", откликнулась тянка со сложной судьбой, пару дней лампово попереписывались.'), False)
        self.assertEqual(check_phrase_for_girl('1. мамка человека, дс и около, 17. '), True)
        self.assertEqual(check_phrase_for_girl('здорова я настюха пишите если скучно а то мне тоже скучно тг @xxxjustkidding '), True)
        self.assertEqual(check_phrase_for_girl('Не_ламповая почти тиан ищет собеседника на ночь. '), True)
        self.assertEqual(check_phrase_for_girl('Пообщаться ирл с не всратым, взрослым кунчиком ^^'), True)
        self.assertEqual(check_phrase_for_girl('Я понял жизнь. Всем тян нужные плохие парни. Так вот, тянучки, эксклюзивно для вас, я плох во всём, срочно пишите мне и send noods. А ещё вам котика няшного на пикче'), False)
        self.assertEqual(check_phrase_for_girl('Немолодая жируха-яойщица ищет кого-то обсудить сёдзё-мангу и вообще мангу, а также визуальные новеллы путём неспешного обмена письмами по электронной почте. Если количество прочитанной манги у меня ещё более-менее какое-то, то визуальные новеллы я читаю пока довольно мало, штук десять мб наберётся. И да, среди прочитанного есть Бесконечное простигосподи лето.'), True)
        self.assertEqual(check_phrase_for_girl('Застряла в аэропорту Берлина часов на 15, готова поговорить с вами о любой хуете~'), True)
        self.assertEqual(check_phrase_for_girl('Алина, 16, Могилев. '), False)
        self.assertEqual(check_phrase_for_girl('Ищу тян или куна, который споет мне в скайпе. Ухожу завтра в армию. Можно просто попиздеть, я с бухлом и в скайпе конфа из двух с половиной человек.'), False)
        self.assertEqual(check_phrase_for_girl('Привет. Я девушка, 25 лет. Здесь за избавлением от своих страхов и приобретением друзей, которым смогу помочь сама и которые смогут помочь мне совместными прогулками, времяпровождением. '), True)
        self.assertEqual(check_phrase_for_girl('1. Дева'), True)










    def test_city(self):
        self.assertEqual(check_phrase_for_city('Дс'), True)
        self.assertEqual(check_phrase_for_city('ДС'), True)
        self.assertEqual(check_phrase_for_city('1. 18; неважно, но вообще обитаю в подДСье;'), True)
        self.assertEqual(check_phrase_for_city('Тян, 23+, ДС-2. '), False)
        self.assertEqual(check_phrase_for_city('180 км от ДС, 21, тян'), True)
        self.assertEqual(check_phrase_for_city('ДС, 23, Ж'), True)
        self.assertEqual(check_phrase_for_city('Дс, 22, тян/девушка'), True)
        self.assertEqual(check_phrase_for_city('1. Это все не так важно, но вообще Мск, тян, 19'), True)
        self.assertEqual(check_phrase_for_city('Возможно с БДСМ уклоном. Тянка свитчик (может сделать куни'), False)
        self.assertEqual(check_phrase_for_city('Тян, Подмосковье, уже можно.'), True)
        self.assertEqual(check_phrase_for_city('Тян 23 дыэс'), True)
        self.assertEqual(check_phrase_for_city('МО, всратая тян,17лвл.'), True)
        self.assertEqual(check_phrase_for_city('Московская обл,тян,18'), True)
        self.assertEqual(check_phrase_for_city('Москоу, тян, 21'), True)
        self.assertEqual(check_phrase_for_city('1. Подмосковье. Ж 22.'), True)
        self.assertEqual(check_phrase_for_city('Девушка 20 лет ищет интересного молодого человека для общения по почте'), False)
        self.assertEqual(check_phrase_for_city('Омск тян 20'), False)
        self.assertEqual(check_phrase_for_city('id278818486 Тян, 19 лет. Хочу поговорить с кем-нибудь прямо сейчас.'), False)
        self.assertEqual(check_phrase_for_city('23 дс1 Ищу кто не прочь выпить, сходить на гиг. Вообще как товремя. я кун. проебан, но не всрат. Интересуют фильмы. японские мультики для слабоумных. игоры. телега @edwardradical что-то мне не очень хорошо.'), True)
        self.assertEqual(check_phrase_for_city('Есть кто с Бибирево или близлежащих районов? Свистит хата до 7 30 утра, далее на работу, телега @skywokerjam Кун 23,  урод, алко и вещ-ва приветствую.'), True)
        self.assertEqual(check_phrase_for_city('Околомосква, 23, м. Привычек вредных не имею. Ростом немного больше 180. Рабствую программистом с утра до вечера, поэтому свободен только по выходным. Ищу тян. Люблю фрайдейс — хочешь поесть нахаляву? Ну пошли, пока праздники не кончились. Но пообщаемся сначала. Телеграм: @telesav'), True)
        self.assertEqual(check_phrase_for_city('27 лвл околоДС кун, ищу тян на западе Москвы, чтоб подселиться к ней, ибо заебало из области на работу катать)))  скидываться на квартплату, хавчик, поёбывать - готов) подтянутый, адекватный. тележка @Orbital Cookie'), True)
        self.assertEqual(check_phrase_for_city('• Jolie fille; • Moscou; • 22. @jenetyu'), True)
        self.assertEqual(check_phrase_for_city('Дэфолтушка, мэ двадцать. Вольного общения с любым аноном. @found_a_mental если ты средне-всратая тян из районов дсни, лампово угарнём ирл.'), True)
        self.assertEqual(check_phrase_for_city('ПодДС, Химки  20 мин от м. Планерная ,  а сильно это важно? , кун Второй игрок пройти древний ААА-тайтл или порубить в аркаду Диван, телек, приставка и пицца – все есть @AM_XD'), True)


if __name__ == '__main__':
    unittest.main()
