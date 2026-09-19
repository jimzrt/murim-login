<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0489.txt",
      "sha256": "91b127ceed17dc9c305af026fdd59401f1dca397fd1b9914d4121133e1888b7c",
      "bytes": 13126
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a2661366486ceaaeba4decef43f4dcbc8e1a9a0940ae604f6d6d8dbd1b0a5ab3",
      "bytes": 3480
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "091872ee1af46ab31e88c89b679ad60a8de31bfe72ee7c6fb0fbaa824ea1e456",
      "bytes": 155813
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8cec17f6bd6017be95652a53b7752b6cf21824b8fc337d69d3250503d65351c6",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "4b643bcc64a86f13cadd65c60e4c1d94e426fde222f861dc7b50f5d1dfec563a",
      "bytes": 1547
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "be5bcee05a31549cecd19b9aed491c770bb9df6aadc1f4f7dff5fe00b35befec",
      "bytes": 855
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0d6cef49b0e30a240b8b7d8a8f091792176d3591c1c9e5c7e0fc265ebea7d898",
      "bytes": 152065
    }
  ],
  "estimated_tokens": 9873
}
-->

# Durable State Update — Chapter 489

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 489. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 489. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 489,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 489,
    "continuity_sources": [489],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The functionally crippled Gate continues leaking faint mana; its residual mana is mutating local life, and the Water God Dragon has absorbed all of that mana.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, have been captured in the Gate's entrance waterways; the remaining population is unknown, and the fish fight and kill one another.",
    "Dongting Lake is calm again after the Water God Dragon's mutated rampage nearly overturned it with thunder and waves.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Jeok trusts Taekyung more deeply than anyone else, despite interpreting Taekyung's attempted explanation of his origin as a drawn-out declaration that he wanted to die.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history, while concealing that identity behind his young medical-apprentice persona.",
    "Mungyeong intends to teach Taekyung secret martial arts after Jeok asked him to look after and instruct Taekyung."
  ],
  "continuity_sources": [
    488,
    487
  ],
  "open_questions": [
    "What lies beyond the exposed Gate, why has it lost most of its functions, and how far has its residual mana's mutation spread?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What secret martial arts will Mungyeong teach Taekyung, and why has he chosen to begin teaching him now?"
  ],
  "safe_through": 488,
  "temporary_decisions": [
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 독문 무공 as secret martial arts, and 비급 as martial arts manual.",
    "Render 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, and 기막 as qi curtain."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 제자     | **Disciple**                                 |
| 퀘스트              | **Quest**                      |
| 레이드     | **raid**              |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 486
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 488
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 488
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance who has asked him to look after and instruct Jin Taekyung, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃489화



독문 무공.

그 단어를 들은 순간, 빡대가리라는 네 글자는 이미 뇌리에서 깨끗이 지워졌다.

잠시 눈을 깜빡이던 나는 더듬거리는 목소리로 물었다.

“독문…… 무공이요? 저한테 독문 무공을 가르쳐 주신다고요?”

무림인에게 있어 독문 무공은 목숨만큼, 아니 목숨보다 더 중요한 것이다.

무협 소설에서도 비급 하나 얻겠다고 부나방처럼 달려드는 놈들이 사방천지에 널려 있었으니까.

게다가 막상 무림을 겪어 보니 그보다 더했으면 더했지, 절대 덜하진 않다는 걸 알게 됐다.

‘그런데 독문 무공을 알려 줘? 그것도 살성씩이나 되는 엄청난 고수가?’

직접 들었는데도 믿지 못할 이야기다. 아니, 그전에 커다란 물음표가 따라붙었다.

“왜요?”

의문이 가득 담긴 질문에, 문경의 매끈한 미간에 깊은 골이 파였다.

“뭐가 말이냐?”

“아니, 저한테 갑자기 왜 이러세요.”

“설마 했는데 화왕, 그 늙은이가 정말로 아무런 언질도 안 해 준 모양이군.”

“그렇다면 혹시…….”

“그래. 네 녀석의 짐작이 맞다. 화왕이…….”

“저 이적합니까? 열화문에서 살성문, 뭐 그렇게 소속 바뀐 거예요?”

“…….”

살생 마려운 표정으로 나를 바라보던 문경이 한숨처럼 말을 이었다.

“화왕이 직접 찾아와 부탁했다. 네게 무공을 가르쳐 달라고.”

“예?”

문파 간 트레이드가 아니라 다행이긴 한데, 이건 이것대로 믿지 못할 이야기다.

나는 미심쩍은 눈초리로 문경을 바라보았다.

“무어냐, 그 눈빛은?”

“아무리 생각해도 거짓말 같아서요.”

“거짓말?”

“첫째. 우리 노야는 성질이 더럽고 자존심이 강해서 누구한테 뭔가를 부탁할 분이 아닙니다.”

서늘한 한기가 맴돌던 문경의 얼굴 위로 훈훈한 온기가 스쳤다.

“흠, 제법 정확하게 파악하고 있군. 계속해 봐라.”

“둘째. 그 부탁을 받은 사람도 우리 노야 만큼이나 성질이 더럽고 자존심이 강해서, 자신의 독문 무공을 순순히 가르쳐 줄 사람이 아닙니다.”

“……!”

“어쨌든 말씀드린 두 가지 이유로, 저는 목에 칼이 들어와도 못 믿겠습니다.”

“그래. 그렇단 말이지.”

나직하게 중얼거리던 문경이 차갑게 식은 눈동자로 나를 응시했다.

“목에 칼이 들어간다면 믿겠다는 소리. 잘 들었다.”

그 순간, 문경의 소매 끄트머리에서 뭔가가 반짝거렸다. 슬그머니 모습을 드러낸 소검(小劍)을 확인한 나는 슬그머니 말을 바꿨다.

“믿음이 확 가네요.”

“갑자기?”

“사실 처음부터 굳게 믿고 있었습니다.”

“미친놈, 인성에 문제 있나?”

“악!”

“……미쳐도 단단히 미친놈이로군.”

아, 그냥 죽이고 싶다. 표정에 딱 그렇게 쓰여 있다.

갈등 어린 눈빛으로 잠시 소검을 만지작거리던 문경이 불쑥 입을 열었다.

“생각해 보면 썩 틀린 말은 아니지.”

“예?”

“첫째. 네 녀석의 말대로 화왕은 성질이 더럽고 자존심이 강한 사람이 맞다. 하지만 제자에 관한 문제에서만큼은 예외인 것 같더군.”

“……!”

“어차피 이렇게 말해 봤자 정식 제자가 아니라고 바득바득 우기겠지만 어쨌든. 화왕은 네 녀석을 아낀다. 그것도 무척이나.”

음.

무슨 말을 해야 할지 모르겠다. 왠지 모르게 가슴 한구석이 간질거리기도 하고, 목이 메어 오는 것 같기도 하고. 그냥, 그렇다.

굳게 입을 다문 나를 향해, 문경이 건조한 목소리로 말을 이었다.

“둘째. 나 역시 그리 부드러운 성정의 소유자는 아니다. 그렇지만 충분한 이유가 있다면 내 독문 무공을 네 녀석 같은 미친놈에게도 가르쳐 줄 의향이 있지.”

“미친놈인데도요?”

“그 미친놈이, 앞으로도 이어질 암천의 행보에 큰 걸림돌이 될 테니까.”

조용한 목소리가 밤공기를 타고 퍼져 나간다. 문경은 잔잔하게 흐르는 동정호의 강물을 응시하며 말을 이었다.

“나는 반평생 이상을 무림인으로 살았다. 아니, 살수로 살았지. 그건 내가 원한 삶이 아니라 처음부터 주어진 삶이었다. 그렇기에 내가 걸어온 길은 피와 시신으로 뒤덮인 혈로(血路)였다.”

살성. 고금제일의 살수를 칭하는 별호는 하루아침에 얻어진 것이 아니다. 그는 죽이고, 죽이고, 또 죽이다가 마침내 모두가 인정하고 두려워할 수밖에 없는 위치에 올랐다.

하지만 누구나 각자의 사정은 있기 마련이다.

그리고 이 세상에는 내가 아는 것보다, 감춰져 있는 것들이 더 많다. 눈앞의 문경은 그런 삶을 살아왔을 것이다.

뜻 모를 감정이 뒤섞인 눈으로 어둠 너머를 바라보던 문경이 나직하게 말을 이었다.

“이미 코앞에 들이닥친 거대한 전란에 조금이라도 도움이 될 수 있다면, 네놈에게 무공을 전수하는 것도 썩 나쁘진 않을 것 같다는 생각이 들더군. 그뿐이다.”

대수롭지 않게 말하지만 결코 쉬운 결정은 아니었을 것이다.

남의 것을 받는 건 쉽지만, 자신의 것을 내놓는 건 어려운 법.

정마대전을 겪었던 사람들이 지금의 문경처럼 생각하고 행동했다면 지금쯤 천하의 무림인 중 절반은 구파일방의 무공을 익혔을 테니까. 그런 의미에서 문경이 새삼 새롭게 보였다.

“그게…… 대의(大意)라는 부르는 겁니까?”

“대의?”

“다른 사람들을 위해 결정하신 거잖아요. 다른 이를 위해 스스로를 희생하는 것. 그걸 대의라고 부르지 않습니까.”

내 말을 들은 문경이 고개를 가로저었다.

“대의는 나 같은 자가 입에 올릴 수 있는 말이 아니다. 한때나마 생존을 위해 다른 이를 죽였던 살수가 대의라니, 낯간지럽기 짝이 없군.”

“전에 노야께서 그러셨습니다. 살성은 죽일 놈들만 죽인다고. 그래서 제법 괜찮은 살수라고.”

“검 한 자루를 만들기 위해서는 수백 번 두드리고, 담금질을 거쳐야 한다. 나 역시 다르지 않았지. 살성이 되기 이전에, 살귀(殺鬼)라 불리던 시절이 있었다. 그것이 내가 대의를 논할 수 없는 이유다.”

“그렇다면…….”

나는 문경을 똑바로 응시하며 말을 이었다.

“살성이 아니라, 신의로서의 대의라면 어떻습니까?”

“……!”

호리호리한 신형이 덜컥 굳는다. 잔잔하기 그지없는 동정호의 강물과는 반대로, 문경의 눈동자에는 파문이 일고 있었다.

그리고 잠시 후. 깊게 가라앉은 목소리가 짧은 침묵을 깨트렸다.

“신의라……. 언제나 그 별호가 마음에 들지 않았지.”

“어째서입니까?”

“신의라 불린다고 해서 내 과거가 지워지진 않으니까. 내 과거가 알려진다면, 그들이 욕하고 두려워하리라는 것을 아니까.”

“하지만 사람들을 살리셨죠. 헤아릴 수도 없을 만큼. 그들은 고마움을 잊지 않을 겁니다.”

한참의 시간이 흐른 뒤에도 문경의 대답은 돌아오지 않았다.

어떤 생각에 잠긴 채 말없이 강물만 바라보던 그는, 문득 나를 향해 고개를 홱 돌렸다.

“헉, 깜짝이야. 왜 그러세요?”

“감히 내게 주제넘은 말을 한 네놈을 어찌할까, 생각했다.”

“……보통은 이걸 위로라고 하지 않습니까?”

“위로? 네깟놈이 나를?”

서늘한 눈빛에 오장육부가 시원해질 지경이다.

그래, 시벌. 열화신룡이고 나발이고 살성한테는 네깟놈이지.

여기서 괜히 말대꾸라도 했다가 역풍을 맞는 것보다는, 말을 돌리는 게 장수의 비결일 거다.

“이야, 달 한번 밝다.”

곧바로 딴청을 피우는 내 모습에 문경의 눈썹이 꿈틀거렸다.

“어쩌다 이야기가 여기까지 흘렀는지 모르겠군. 앞으로는 쓸데없는 언행을 삼가도록.”

“바람도 시원하고.”

“어깨 위도 시원하게 해 줄까?”

“……방금 하신 말씀, 명심하겠습니다.”

스윽.

반쯤 튀어나와 있던 소검이 다시 소매 속으로 모습을 감췄다.

언제 그랬냐는 듯 다시 건조하고 딱딱한 표정으로 돌아온 문경이 입을 열었다.

“해서 묻겠는데, 네놈은 어찌할 생각이냐?”

“뭘 말입니까?”

“멍청한 건지 귀가 어두운 건지 모르겠군. 내게 무공을 사사하는 것 말이다.”

“……멍청한 게 아니라, 저한테 선택권을 주실 줄 몰라서 그런 건데요?”

“싫다는 놈을 뭐가 아쉬워서 억지로 붙들고 가르치겠느냐?.”

그게 맞는 말이긴 한데, 비정상인 사람의 입에서 저런 정상적인 말이 나오니 엄청 낯설다.

물론 이 생각을 입 밖으로 꺼내진 않았다.

그랬다가는 문경이 몸소 내 영혼을 육신에서 끄집어내려 할 테니까.

“그래서 대답은?”

문경의 재촉에 나는 뒤통수를 긁적였다.

‘살성의 독문 무공이라…….’

당연히 탐이 난다.

사람마다 개개인에게 맞는 무공이 있고 맞지 않다면 오히려 독이 되는 경우도 있지만, 이 경우는 천하에서도 손꼽히는 초절정 고수인 살성의 독문 무공 아닌가.

그의 무공에 녹아든 심득을 절반, 아니 반의반이라도 이해하고 내 것으로 만들 수 있다면 내 경지도 한층 진일보할 수 있을 것 같았다.

다만 한 가지 걸리는 점이 있다면…….

“아무래도 화왕이 마음에 걸리는 모양이군.”

“……혹시 독심술이라도 익히셨습니까?”

“독심술이 무슨 소용이냐. 네놈은 생각이 표정에 다 드러난다.”

문경이 한심하다는 눈빛으로 나를 바라보며 말을 이었다.

“제대로 된 무림인이라면 마음을 감출 줄도 알아야 하는 법. 화왕도 어지간하군. 이런 기초적인 것도 안 가르쳐 줬다니.”

“방금 하셨던 말씀, 취소하시죠.”

눈살을 찌푸린 내 모습에, 문경의 눈빛이 깊게 가라앉았다.

“내 말이 틀렸느냐?”

“예. 입은 삐뚤어져도 말은 바로 해야 하는 것 아니겠습니까.”

“네놈이 감히…….”

“안 가르친 게 아니라 못 가르친 겁니다. 노야는 저보다 더 표정을 못 감추시는 분인데, 어떻게 모르는 걸 가르칩니까?”

“……상상 그 이상이군.”

한숨을 내쉰 문경이 고개를 절레절레 저었다.

“어쨌건 화왕에 관해서는 너무 신경 쓸 것 없다. 화왕이 직접 부탁한 일이기도 하고, 나 역시 너 같은 녀석과 사승(師承) 관계를 맺을 생각은 추호도 없으니까.”

“아, 예.”

거, 아무리 그래도 그렇지. 너 같은 녀석이라니.

듣고 있자니 살짝 마음에 스크래치가 가긴 하는데, 그래도 문경의 단언을 듣자 한결 마음이 편안해진다.

‘그런데 왠지 모르게 노야를 배신하는 것 같은 이 기분은 뭐지?’

적천강이 직접 부탁까지 한 일이고, 앞으로의 험난한 전투를 생각하면 도움이 되는 일이다.

전후 사정을 생각해 보면 아무 문제도 없는 일인데 왜 이런 찝찝함이 드는지, 알다가도 모르겠다.

말도 안 하고 사라진 적천강을 생각하며 입맛을 다시던 나는 마침내 고개를 끄덕였다.

“알겠습니다.”

“확실히 고민하고 대답해라. 시작은 네 선택이지만, 끝내는 것은 다르다.”

“예? 그 말씀은…….”

“오직 내가 판단에 따라 움직여야 한다. 하지만 네 녀석이 이 수련을 끝마친다면, 지금까지와는 다른 무림인이 되어 있겠지.”

뭐지, 이거.

무공을 사사할 상대가 상대이니만큼 어느 정도 예상은 했지만, 왠지 모르게 등골이 서늘해진다.

마른침을 꿀꺽 삼킨 내 귓가에, 문경의 딱딱한 목소리와 함께 익숙한 종소리가 울려 퍼졌다.

“네놈은 상당한 경지를 이룩한 무인이지만, 무인과 무림인은 다르다. 아직도 반쪽짜리에 불과한 널 진짜 무림인으로 만들어 주지.”

띠링.



- 돌발 퀘스트, [가짜 무림인]이 생성되었습니다!



[가짜 무림인]을 수락하시겠습니까?

악   /   N



“…….”

아니, 왜 선택지에 Y 대신 악이 있는 건데.

어이없는 눈빛으로 퀘스트 창을 바라보던 나는, 의식할 새도 없이 작게 중얼거리고 말았다.

“악?”

띠링.



- 퀘스트가 수락되었습니다. 악!



“……아.”

돌아 버리겠네.
```

## Final English reading copy

```markdown
# Chapter 489

Secret martial arts.

The moment I heard those words, the four syllables *fucking blockhead* were wiped clean from my mind.

After blinking for a moment, I asked in a faltering voice,

“Secret… martial arts? You’re saying you’ll teach me your secret martial arts?”

To a martial artist, secret martial arts were as important as life itself—no, more important than life.

Even in martial arts novels, there were countless people who threw themselves at danger like moths to a flame just to obtain a single martial arts manual.

And after experiencing the Murim firsthand, I learned that reality was no different. If anything, it was worse.

*But he’s offering to teach me his secret martial arts? And he’s an incredible master on the level of the Slaughter Saint?*

Even though I had heard it directly from him, I couldn’t believe it. No, even before that, one huge question mark had appeared.

“Why?”

At my question, which was filled with doubt, a deep furrow formed between Mungyeong’s smooth brows.

“What do you mean?”

“No, I mean, why are you suddenly acting like this toward me?”

“I suspected as much, but it seems that the Fire King, that old man, really didn’t give you any heads-up.”

“In that case, could it be…”

“That’s right. Your guess is correct. The Fire King…”

“Am I being transferred? Did my affiliation change from the Fire Gate Clan to the Slaughter Saint Clan or something?”

“…”

Mungyeong stared at me with an expression that made it clear he wanted to kill someone, then continued with a sigh.

“The Fire King came to me personally and asked me to teach you martial arts.”

“What?”

It was a relief that this wasn’t a sect-to-sect trade, but it was still an unbelievable story in its own way.

I looked at Mungyeong suspiciously.

“What is that look?”

“It sounds like a lie no matter how I think about it.”

“A lie?”

“First. Our Old Master has a foul temper and a strong sense of pride. He isn’t the kind of person who asks someone else for anything.”

A warm glow passed over Mungyeong’s face, which had previously been surrounded by a chilly aura.

“Hm. You’ve assessed him rather accurately. Continue.”

“Second. The person he asked is just as foul-tempered and prideful as our Old Master. He isn’t the kind of person who would willingly teach someone his secret martial arts.”

“…”

“In any case, for those two reasons, I wouldn’t believe it even with a knife pressed to my throat.”

“I see. So that’s how it is.”

Mungyeong muttered softly, then stared at me with eyes gone cold.

“If a knife were pressed to your throat, you’d believe me. I heard you clearly.”

At that moment, something glinted from the end of Mungyeong’s sleeve. When I saw a short sword slowly emerge, I quietly changed my words.

“I completely believe you now.”

“Suddenly?”

“Actually, I believed you firmly from the very beginning.”

“You’re a fucking lunatic. Is something wrong with your character?”

“Gah!”

“Even by lunatic standards, you’re completely insane.”

*Ah, he really wants to kill me.*

His expression said exactly that.

Mungyeong toyed with the short sword for a moment, his eyes conflicted, then abruptly spoke.

“Come to think of it, what you said isn’t entirely wrong.”

“What?”

“First. As you said, the Fire King does have a foul temper and a strong sense of pride. But he seems to be an exception when it comes to matters concerning his Disciple.”

“…”

“Of course, even if I say that, he’ll stubbornly insist that you aren’t his formal Disciple. Regardless, the Fire King cares about you. Very much.”

Hmm.

I didn’t know what to say. For some reason, a corner of my chest felt ticklish, and my throat felt tight.

It was just… like that.

As I kept my mouth firmly shut, Mungyeong continued in a dry voice.

“Second. I’m not exactly a man of gentle temperament either. But if there is sufficient reason, I’m willing to teach my secret martial arts even to a lunatic like you.”

“Even though I’m a lunatic?”

“Because that lunatic will become a major obstacle to Dark Heaven’s actions from this point forward.”

His quiet voice spread through the night air. Mungyeong continued while gazing at the gently flowing waters of Dongting Lake.

“I have lived as a martial artist for more than half my life. No, I lived as an assassin. It was not a life I chose. It was the life I was given from the beginning. That is why the path I walked was a bloodstained road covered in blood and corpses.”

The Slaughter Saint—the sobriquet given to the greatest assassin in history—had not been earned overnight. He had killed, killed, and killed again until he reached a position everyone had no choice but to acknowledge and fear.

But everyone had their own circumstances.

And in this world, there were more things hidden than I knew.

Mungyeong, standing before me, had probably lived such a life.

His eyes filled with emotions I couldn’t decipher, Mungyeong gazed beyond the darkness and continued quietly.

“If passing on my martial arts to you can be of even the slightest help in the great war already at our doorstep, then it doesn’t seem like such a bad idea. That is all.”

He spoke as though it were nothing important, but it could not have been an easy decision.

It was easy to receive something that belonged to someone else. Giving away something of your own was difficult.

If the people who had fought in the Great Faction War had thought and acted as Mungyeong did now, half the martial artists in the world would have learned the martial arts of the Nine Sects and One Gang by now.

In that sense, Mungyeong seemed different from before.

“Is that… what you call a great cause?”

“A great cause?”

“You made that decision for other people. Sacrificing yourself for someone else. Isn’t that what a great cause means?”

Mungyeong shook his head.

“A great cause is not something a man like me can speak of. An assassin who once killed others for the sake of survival speaking of a great cause? The very thought makes me cringe.”

“The Old Master told me before that the Slaughter Saint only kills people who deserve to die. He said you were a pretty decent assassin.”

“To make a single sword, you must hammer it hundreds of times and put it through the tempering process. I was no different. Before I became the Slaughter Saint, there was a time when I was called the Killing Ghost. That is why I cannot discuss a great cause.”

“In that case…”

I looked Mungyeong straight in the eye and continued.

“What about a great cause as the Divine Physician, rather than as the Slaughter Saint?”

“…”

His slender body suddenly went rigid.

Unlike the utterly calm waters of Dongting Lake, ripples spread through Mungyeong’s eyes.

A moment later, a deep, sunken voice broke the brief silence.

“The Divine Physician… I never liked that sobriquet.”

“Why not?”

“Being called the Divine Physician does not erase my past. Because I know that if my past were revealed, people would curse me and fear me.”

“But you saved people. Countless people. They won’t forget their gratitude.”

A long time passed, but Mungyeong did not answer.

He remained lost in thought, silently staring at the river, then suddenly whipped his head around to face me.

“Gasp! You scared me. What’s wrong?”

“I was thinking about what to do with you for daring to say something so presumptuous to me.”

“Isn’t this normally called comforting someone?”

“Comforting me? You?”

His icy gaze made my insides feel refreshed.

Yeah, fuck. To hell with the Blazing Flame Divine Dragon—to the Slaughter Saint, I was still just *you*.

Rather than talk back and get hit by the backlash, changing the subject was probably the secret to longevity.

“Wow, the moon is bright tonight.”

Mungyeong’s eyebrow twitched as I immediately pretended nothing had happened.

“I don’t know how the conversation ended up here. From now on, refrain from useless words and actions.”

“The breeze is nice and cool, too.”

“Want me to cool off everything above your shoulders too?”

“…I’ll keep what you just said in mind.”

*Shhk.*

The short sword, which had been half-drawn, slipped back into his sleeve.

Mungyeong returned to his usual dry, stiff expression, as though nothing had happened, and opened his mouth.

“So I’ll ask you. What do you intend to do?”

“About what?”

“I can’t tell whether you’re stupid or hard of hearing. I mean studying martial arts under me.”

“…I’m not stupid. I just didn’t know you would give me a choice.”

“Why would I force someone who doesn’t want to learn to stay and teach him?”

He had a point, but hearing such a perfectly normal statement from the mouth of an abnormal person felt incredibly strange.

Of course, I didn’t say that aloud.

If I did, Mungyeong would personally drag my soul out of my body.

“So? What is your answer?”

At Mungyeong’s urging, I scratched the back of my head.

*The Slaughter Saint’s secret martial arts…*

Of course I wanted them.

Everyone had martial arts suited to them, and if a martial art did not suit someone, it could become poison instead. But this was the secret martial art of the Slaughter Saint, a Supreme Peak master counted among the greatest in the world.

If I could understand even half—or a quarter—of the insights embedded in his martial arts and make them my own, I felt that my realm could advance another step.

There was only one thing bothering me.

“It seems the Fire King is weighing on your mind.”

“Have you learned mind-reading or something?”

“What use would mind-reading be? Every thought you have is written plainly on your face.”

Mungyeong looked at me as though I were utterly hopeless and continued.

“A proper martial artist must know how to conceal his feelings. The Fire King is quite something. To think he failed to teach you even something this basic.”

“Take back what you just said.”

At my frown, Mungyeong’s gaze sank deeply.

“Was I wrong?”

“Yes. Even if your mouth is crooked, shouldn’t you speak the truth correctly?”

“You dare…”

“He didn’t fail to teach me. He couldn’t teach me. The Old Master is even worse at hiding his expressions than I am. How could he teach me something he doesn’t know?”

“…You’re beyond my imagination.”

Mungyeong sighed and shook his head.

“In any case, don’t worry too much about the Fire King. This is something he personally asked me to do, and I have no intention whatsoever of entering into a Master-Disciple relationship with someone like you.”

“Ah. Right.”

Come on. Even so, *someone like you*?

It stung a little to hear him say it, but his firm declaration still made me feel much more at ease.

*But why do I feel like I’m betraying the Old Master?*

Jeok Cheongang himself had asked Mungyeong to do this, and considering the difficult battles ahead, it was something that would help me.

Looking at the circumstances, there was no problem at all. So why did I feel so uncomfortable?

Thinking of Jeok Cheongang, who had disappeared without saying a word, I smacked my lips and finally nodded.

“All right.”

“Think carefully before you answer. Beginning is your choice, but ending it is different.”

“What? What does that mean?”

“I alone will decide how you move. But if you complete this training, you will become a martial artist unlike the one you have been until now.”

What was this?

I had expected something like this to a certain extent, considering who I would be studying under, but for some reason, a chill ran down my spine.

As I swallowed dryly, a familiar chime rang in my ears alongside Mungyeong’s hard voice.

“You may be a martial artist of considerable skill, but a martial artist and a Murim martial artist are not the same thing. You’re still only half-formed. I’ll turn you into a true Murim martial artist.”

*Ding.*

> **System**
>
> - Sudden Quest, **Fake Murim Martial Artist**, has been generated!
>
> **Will you accept Fake Murim Martial Artist?**
>
> **Agh** / **N**

“…”

Why was there an Agh instead of a Y in the choices?

I stared at the Quest window with an incredulous expression, then muttered without even realizing it.

“Agh?”

*Ding.*

> **System**
>
> - Quest accepted. **Agh!**

“…Ah.”

This was driving me crazy.
```
