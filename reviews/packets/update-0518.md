<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0518.txt",
      "sha256": "2681b1efcd403bfd1f58dc9fc7d23472bff2ff5c50fc03928e73d460b8904da0",
      "bytes": 13829
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ed2149454c7635157c0275899af7c147a6b768701c8019a04d14c7b6abf840cd",
      "bytes": 4414
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e575723bf81759bbc4e94f3f3a1d5d6b0e99ceffcd08e2fe1e1e20fbff12c673",
      "bytes": 165203
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3c566d56752a9c1c93654bd85077cac3dca1a9599cd1a6f173c580b549cec330",
      "bytes": 1630
    },
    {
      "path": "characters/Unnamed.md",
      "sha256": "a824ca4086a254bb4bc0b767671d1f927536da5a85772d19678615b483f9cb28",
      "bytes": 750
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f0eeea838827542b68db72ad422e6d5879396f37918c6c0a7e2a686c6c414560",
      "bytes": 156461
    }
  ],
  "estimated_tokens": 10700
}
-->

# Durable State Update — Chapter 518

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 518. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 518. Profile updates may replace only one
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
  "chapter": 518,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 518,
    "continuity_sources": [518],
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
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has entered a new realm and achieved Returned to Youth.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; Mu Song and five Water Dragon Stronghold subordinates know he is exceptionally powerful but not that he is the Slaughter Saint.",
    "Mungyeong is training Taekyung to refine the stability and precision of the violent internal energy produced by the Fire Gate Divine Technique through Rising on Duckweed, Crossing Water.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "The New Murim Alliance has been publicly announced from Mount Song and will be founded in three days; major orthodox and unorthodox factions, eccentric experts, and distant great families are gathering in Henan, while the Yangtze River Channel League, Green Forest Alliance, North Sea Ice Palace, and Nanman Beast Palace remain uncertain in their positions.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Unnamed, Hong Dao's practical Disciple, endured three months in Repentance Cave, achieved enlightenment, received Shaolin's Great Restoration Pill, and is now a scarred Supreme Peak master and Jung Ho's young Martial Uncle; Shaolin's new Abbot, his eldest Senior Brother, wants to meet Taekyung.",
    "The Black Dragon Demon Gate is an ancient unorthodox faction that once belonged to the Demonic Cult's Twelve Branches and now ranks among the Central Plains' strongest unorthodox powers.",
    "Jin Taekyung completed Stage 2 of Fake Murim Practitioner, achieved Single Reed Crossing the River, improved his internal-energy control and attributes, gained 50 bonus points and substantial EXP, and leveled up.",
    "Taekyung experienced a nightmare involving a familiar-feeling red gaze, oppressive fear, and a gigantic snake in a swamp; its source and significance are unknown."
  ],
  "continuity_sources": [
    517,
    516
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the Nanman Beast Palace, North Sea Ice Palace, Yangtze River Channel League, and Green Forest Alliance support, ignore, or oppose the New Murim Alliance?",
    "What is the source of the familiar red gaze and oppressive presence Taekyung encountered in his nightmare?"
  ],
  "safe_through": 517,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, 갠지스강 as Ganges River, and 대환단 as Great Restoration Pill.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain sa-eo for 사어, shark for 상어, Old Master for 노야, this old man/I for 노부, Shark Water-Ski Team for 수상스키단, and swift ship for 쾌조선.",
    "Render 정호 as Jung Ho, 사마표 as Sama Pyo, 흑룡도 as Black Dragon Saber, 대초자곤 as two-section staff, 시주 as Benefactor, 계율원주 as Discipline Hall Master, 십이지파 as Twelve Branches of the Demonic Cult, 모용세가 as Murong Family, 요녕 as Liaoning, and 진돗개 하나 as Jindotgae One."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남궁세가   | **Nangong Family**               |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 대사      | **Master** for a senior Buddhist monk                           |
| 무명 | **Unnamed** | Dharma name given by Hong Dao; literally means having no name. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 은자 | **silver nyang** | Silver currency unit. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 화주 | **strong liquor** | Liquor stored and consumed by the dark-path swordsmen. |
| 아미타불 | **Amitabha** | Buddhist invocation spoken by the unidentified arriving group. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 검왕 | **Sword King** | Short form for the Azure Sky Sword King, Nangong Cheon. |
| 여아홍 | **Yeoahong** | Traditional Chinese rice wine; literally Daughter's Red. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 장제자 | **Senior Disciple** | The Seafaring King's designated successor. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 혈곤 | **Blood Cudgel** | Sobriquet of Do Sangho. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 무명 | 적천강 | junior_monk_to_legendary_martial_master | Great Hero Jeok Cheongang | formal-deferential | Identifies Jeok by the title Fire King and the honorific 대협. |

## Listed compact profiles

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 517
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Unnamed.md

# Unnamed (무명)

- **Safe through:** Chapter 517
- **Aliases:** None
- **Role:** Unnamed is a young Shaolin monk and practical Disciple of the late Hong Dao who achieved enlightenment after three months of treatment and training in Repentance Cave, becoming a Supreme Peak master and Jung Ho's young Martial Uncle.
- **Personality:** Naturally timid and introverted, but unable to control himself once angered.
- **Voice:** His current voice is rough, formal, and polite, punctuated by Buddhist invocations.
- **Relationships:** Hong Dao was his Master; Jung Ho is his Martial Nephew; he carries Hong Dao's will and recognizes the Morning Star whom Hong Dao intended him to find.

## Korean source

```text
＃518화



술이 거나하게 오른 중년인이 손을 번쩍 치켜들었다.

“주인장, 여기 화주(火酒) 한 병 주게!”

“오리구이도!”

“이런 소인배들을 봤나. 무림맹 창설이라는 중대사를 앞두고 화주에 오리구이가 뭔가? 하남에 왔으니 두강주(杜康酒) 정도는 마셔 줘야지!”

“오오. 우리야 좋지만, 자네 너무 무리하는 것 아닌가?”

“괜찮네. 어차피 나눠서 내는 거니까.”

“……제정신이 아니군. 화주로 바꿔.”

숭산 인근 대로변에 있는 객잔은 수많은 사람으로 북적였다. 물론 그중 대다수를 차지하는 부류는 바로 무림인이었다.

아직 풋내기로 보이는 낭인부터 적게는 십 년, 길게는 수십 년 동안 풍진 강호를 주유한 노강호들까지.

이 자리에 모인 그들은 목적도, 나이도, 성별도 달랐다.

그리고 늘 사람이 모이는 곳에는 분쟁이 일어나는 법이다. 술이 거나하게 취한 무림인들이 한자리에 모였다면 더더욱 그랬다.

“잠깐, 네놈은……!”

“오호, 소하문(溯河門)의 장제자 아니신가. 그때 잘린 손가락은 여전하고?”

“놈! 죽을 자리를 찾아왔구나!”

천하가 아무리 넓다지만, 외나무다리에서도 만나는 것이 원수인 법.

이처럼 복잡한 은원(恩怨) 관계에 얽힌 이들의 우연한 만남에는 꼭 칼부림이 뒤따랐다.

차차창! 서걱!

예리한 병장기가 서로를 향해 휘둘러지고 핏물이 튄다. 눈앞에서 벌어지는 치열한 공방에 주변의 무림인들이 함성을 내질렀다.

“와아아아!”

“싸움이다!”

“소하문의 장제자에게 은자 한 냥!”

“그럼 난 장충도(長蟲刀)에게 두 냥 걸지!”

원래 가장 재미있는 게 남의 집 불구경과 싸움 구경이라고 했다.

무림과는 별 연관이 없는 극소수의 사람들은 질색하는 표정으로 슬금슬금 몸을 피했지만, 정, 사, 마를 떠나 싸움이라면 환장한다는 무림인들은 거리낌 없이 소리를 지르고 박수를 쳤다.

그리고 이처럼 혼란스러운 상황 속에서, 지금 막 객잔의 낡은 문을 열고 들어온 중년인의 존재를 눈치챈 이들은 거의 없었다.

차차창! 쾅!

와아아아!

객잔의 중앙에서는 한창 치열한 싸움이 벌어지고 있었지만, 중년인은 시선 한 번 주지 않고 주인장에게 은자 한 냥을 튕겼다.

“화주 두 병에 오리구이 한 마리. 바깥이 잘 보이는 자리로 내와라. 아, 오리는 바짝 구워서.”

“저어, 대협.”

“응?”

중년인을 맞이한 주인장이 허리를 굽실거렸다.

“죄송하지만 지금 마땅한 자리가 없습니다.”

“자리가 없어?”

“예. 보시다시피 워낙 무림의 영웅들께서 많이 찾아오시는 바람에.”

주위를 둘러보던 중년인이 문득 고개를 들어 위를 바라보았다. 계단으로 이어진 층간에는 몇몇 얼굴이 아래를 내려다보고 있었다.

“저 위에는 자리가 있을 것 같은데.”

“아, 송구한 말씀이지만 이 층에는 다른 분들이…….”

“저기가 좋겠군.”

“자, 잠시만 기다려주십시오. 대협, 대협!”

주인장의 간절한 외침에도 중년인은 아랑곳하지 않았다.

성큼성큼 계단을 걸어 올라간 그는, 순간 쏟아지는 날카로운 시선들을 무시하며 중얼거렸다.

“훨씬 낫군. 조용하고.”

객잔의 이 층은 보다 신분이 높은 이들을 위한 자리였다.

일 층과는 고작 계단 스무 개 정도의 차이였으나, 요란 법석한 아래층과는 달리 진중한 분위기가 감돌았고 탁자에 자리한 이들 역시 삼류 무림인과는 거리가 멀었다.

“대, 대협! 거긴 올라가시면 안 됩니다!”

뒤쫓아온 주인장의 외침에 두런두런 이어지던 작은 목소리들이 뚝 끊겼다.

계단과 가장 가까운 탁자에 앉아 있던 반백의 장년인이 눈살을 찌푸리며 입을 열었다.

“시끄럽군. 무슨 일인가?”

“죄, 죄송합니다. 대협. 이 호걸분께서 자리를 착각하시고 그만…….”

“내려 보내게. 아래층도 조용히 시키고.”

“예에.”

그러나 중년인의 발걸음은 이미 다른 곳을 향해 움직이고 있었다.

“저 창가 자리가 괜찮겠군.”

“헉, 대협!”

기겁한 주인장 대신 나선 것은, 앞서 말했던 반백의 장년인이었다.

“멈추시게.”

천천히 신형을 돌린 중년인이 되물었다.

“그거 설마 나한테 한 소린가?”

“그럼 이 자리에 자네 말고 또 누가 있을까.”

“자네?”

“보아하니 나보다 나이도 한참 젊은 것 같은데, 괜한 분란 일으키지 말고 내려가게.”

반백의 장년인이 점잖게 한 마디를 덧붙였다.

“견식이 짧아 보이는 듯하니 알려 주지. 나는 방가(房家)일세. 강호에는 월미도(月美刀)라는 별호로 잘 알려져 있지.”

“오.”

“이 정도면 충분히 알아들었을 터. 자, 이제 소란 피울 생각 말고 얌전히 내려가게.”

잠시 눈을 깜빡이던 중년인이 입을 열었다.

“방금 했던 말, 정말인가?”

월미도는 피식 웃었다.

자신이 누구인가. 이미 오래전 검기상인(劒氣傷人)의 경지에 오른 특급 낭인이다.

고작 절정 초입의 경지로 뻐기고 다니던 혈곤 같은 낭인 나부랭이와는 격이 다른 존재인 것이다.

“허허. 거짓말을 해서 무엇할까. 하긴, 믿지 못할 만도 하지. 이런 곳에서 나를 만날 거라고는 생각 못 했을 테니.”

“아니, 그거 말고. 정말 그래 보이냐고.”

“……?”

이 자가 무슨 말을 하는 거지?

잠깐 멍한 표정으로 중년인을 바라보던 월미도가 눈살을 찌푸렸다.

“그게 무슨 소리지? 도무지 알아듣지 못하겠는데.”

“젊어 보인다고 했던 것 말이다. 틀림없는 사실이겠지?”

“……!”

“으흠. 기분이 썩 나쁘지 않구먼. 좋아. 잘 알겠네.”

월미도가 뭐라 입을 떼기도 전, 호탕하게 껄껄 웃은 중년인이 손을 들어 창가를 가리켰다.

“난 신경 쓰지 말고 계속 마시거라. 마침 아는 얼굴이 있어서 말이야.”

“듣자 하니 이 작자가…….”

“어이구, 대협!”

월미도와 주인장의 외침이 동시에 울려 퍼진 그때, 창가에서 홀로 술을 마시고 있던 노인이 불쑥 입을 열었다.

“혼자 마시던 차에 적적했었는데, 잘됐구려. 어서 오시오.”

“……!”

“……!”

주인장은 물론이고 월미도까지 꿀 먹은 벙어리가 되어 입을 다물었다.

주인장 입장에서는 손님이 괜찮다는데 뭐라 할 말이 없었고, 월미도는 아까 전부터 유독 신경 쓰이던 노인의 태도에 멈칫했다.

‘그냥 돈푼깨나 있는 늙은이처럼 보이기도 하고, 범상치 않은 인물 같기도 한데…… 저 식견 짧은 놈과 무슨 연관이 있나?’

마음 같아서는 당장이라도 저 중년인에게 본때를 보여 주고 싶은데, 왠지 모르게 찝찝한 기분.

그런 월미도의 생각을 아는지 모르는지, 노인의 맞은편에 털썩 주저앉은 중년인은 다짜고짜 술병을 기울였다.

“크, 좋다. 여아홍(女兒紅)이오?”

노인이 고개를 끄덕였다.

“주인장의 말에 따르면 족히 이십 년은 묵혔다고 하더이다.”

“좋은 술이오. 하지만 역시 술 중에는 화주가 제일이지. 곧 주인장이 가져올 테니 한 번 맛보시구려.”

“사양하겠소. 술은 평소에 그리 즐기는 편이 아니라.”

“저런. 안타까운 일이군. 한데 왜 이런 곳에 혼자 있소?”

“별것 아니오. 그저 오랜만에 다른 이들 사이에 파묻혀 볼까 하여.”

노인이 문득 고개를 돌려 창밖을 응시했다.

거리를 지나는 많은 사람과 시끌벅적한 소음. 그 모든 것들을 한동안 말없이 보고 듣던 그가 말을 이었다.

“막상 와 보니 나쁘지 않구려. 이렇게 홀로 있는 것도.”

“혼자 온 것 같지는 않아 보이는데.”

“물론 자식과 손주들이 있소. 그대에게 제자가 있는 것처럼.”

“제자인지 원수인지 모를 놈이 하나 있긴 하지. 한데 어떻게 알았소?”

“모를 수가 있겠소. 직접 보기까지 했는데.”

탁.

중년인이 소리 내어 술병을 내려놓았다.

입가에서 흐른 술이 그의 턱수염을 축축하게 적셨다. 은은한 불빛 때문인지 그 색이 유난히도 붉어 보였다.

“옘병할. 내 그럴 줄 알았지. 한데 그 녀석은 만난 적 없다고 끝까지 잡아떼더이다.”

“제자를 참으로 잘 키웠소, 화왕(火王).”

옷소매로 턱수염을 문질러 닦은 중년인, 화왕 적천강이 물끄러미 노인을 바라보았다.

“지난번에는 제자가 폐를 끼쳤지. 하여 직접 만나러 왔소, 창천검왕(蒼天劍王).”

노인. 아니, 남궁세가의 태상가주이자 십왕(十王)의 일 인인 창천검왕이 빙긋 웃었다.

“그것참 반가운 말씀이오.”

“그대라면 알아볼 줄 알았지, 노부를.”

“하마터면 몰라볼 뻔했소. 반로환동이라…… 기다린 보람이 있구려.”

“그때 했던 약속, 늦었지만 지금 지켜도 되겠소?”

“그 말만을 기다렸소. 참으로 오랜 시간 동안.”

창천검왕의 눈빛이 희열에 물들었다.

지금으로부터 이십여 년 전, 그는 한 사람의 목숨을 적천강에게 일임하는 대가로 비무를 약속받았다.

오늘의 만남은 실로 오랜 기다림 끝에 찾아온 결실이다.

“거참 아쉽군. 곧 화주가 나올 터인데.”

“서 있는 사람이 마시는 것으로 하십시다.”

“검은? 없어도 되겠소?”

“검이라.”

창천검왕은 탁자 위에 가지런히 놓인 두 개의 젓가락을 집어 들었다.

“이것으로 충분하오.”

적천강이 피식 웃으며 창밖을 바라보았다.

“하늘은 푸르고, 당신은 검을 들었구려.”

“태양도 떠 있으니 안성맞춤이오.”

솨아아아아.

바람이 분다. 두 사람의 전신에서 뿜어져 나온 무형의 기파(氣波)가 사방을 휩쓸었다.

그리고 객잔 안의 누군가가 그 사실을 알아차리기도 전에, 두 절대자는 서로를 향해 출수(出手)했다.

콰아아앙!



* * *



쾅! 쾅! 콰아앙!

“오메.”

시방 저게 뭐시여.

나는 창밖 저 멀리에서 보이는 광경에 입을 딱 벌렸다.

아니, 그건 연이어 울려 퍼지는 굉음과 높이 솟구치는 검은 연기 때문만은 아니었다.

나보다 한발 늦게 그 사실을 알아차린 무명 역시 굳은 얼굴로 입을 열었다.

“시주께서도 느끼셨습니까?”

나는 작게 고개를 끄덕였다.

상당한 거리가 있음에도 불구하고 이곳까지 느껴지는 기의 파동. 이건 최소 초절정 고수 간의 격돌이다.

“이런 일이 생겼다면 아마도…….”

“아미타불. 예, 암천의 습격인 것 같습니다.”

“암천, 이 개새끼들이!”

“만전에 주의를 가했건만, 결국 또 다시 이런 일이 터지는군요. 이렇게 된 이상, 소승이 역시 놈들을 상대로 온 힘을 다하여 살계(殺戒)를 펼쳐야겠습니다.”

“나도 같이 펼칠게. 암천 상대로 살계 펼치는 게 취미야.”

그리고 그런 취미가 있는 사람은 나뿐만이 아닌 듯싶었다.

뎅, 데엥-!

“암천! 암천의 습격이다!”

“놈들을 죽여 의기(義氣)를 바로 세우자!”

“사악한 마두 놈들을 쳐 죽여라!”

사방에 울려 퍼지는 경종(警鐘) 소리와 함께 대로변을 오가던 무림인들이 개떼처럼 몰려간다.

보는 이로 하여금 피를 끓게 만드는 광경이 아닐 수 없었다.

‘아아, 이것이 무림 십자군.’

우리 편 존나 쎄. 개많아.

지금까지 암천을 상대로 수적 열세, 혹은 힘의 격차로 인해 온갖 개고생을 해 왔던 나로서는 눈물이 나올 지경이다.

이럴 때 빠질 수는 없지.

“나를! 나를 따르라!”

창밖으로 뛰쳐나가 우뚝 선 내 모습을 발견한 이들이 눈을 부릅떴다.

“열화신룡!”

“태원진가의 열화신룡이다!”

“오오오!”

내가 이래 봬도 무림에서는 상당한 네임드다.

산서성 같은 좁아터진 개천에서도 용이 난다는 걸 입증한 산증인! 정파의 젊은 아이콘!

“와아아아!”

“가자! 암천을 쓸어 버리자!”

“열화신룡이 함께한다!”

쉬쉬쉬쉬쉭!

용기백배한 무림인들이 함성을 내지르며 달려 나간다.

물론 그 선두에 나와 무명이 있음은 두말할 것 없었다.

“야, 시벌. 다 조져!”

공력을 한껏 담은 외침을 내지르자 더욱 커지는 함성.

이토록 많은 무림인과 함께라면 상대가 누구든 족쳐 버릴 수 있을 거라는 확신이 든다.

“성전이다!”

“진 대협께서 성전이랍신다!”

“저 마귀들을 쳐 죽여라!”

“아티마부우울!”

야 이 암천놈의 새끼들아! 니들 거기 꼼짝 말고 있어! 내가 지금 무림 십자군을 몰고 가서 니놈들 머리통을. 머리통을…….

“아.”

순간 뇌가 정지했다. 참혹하게 불타오르는 건물 내부에서 걸어 나오는 한 사람 때문이었다.

“이게 다 뭐 하는 짓거리냐?”

“…….”

마귀가, 우리 쪽 마귀였네.
```

## Final English reading copy

```markdown
# Chapter 518

A middle-aged man, thoroughly drunk, suddenly raised one hand.

“Innkeeper, bring me a bottle of strong liquor!”

“Roast duck, too!”

“Would you look at these petty-minded fools. We’re on the verge of a momentous event—the founding of the Murim Alliance—and you want strong liquor and roast duck? We’ve come to Henan, so we should at least drink Dukang wine!”

“Oh, we’d love that, but aren’t you pushing yourself too far?”

“It’s fine. We’re splitting the bill anyway.”

“…You’ve lost your mind. Switch it to strong liquor.”

The inn along the main road near Mount Song was packed with people. Most of them, of course, were Murim practitioners.

From wandering martial artists who still looked like greenhorns to old veterans who had roamed the martial world for ten years—or even several decades.

The people gathered here differed in purpose, age, and gender.

And wherever people gathered, conflict was bound to follow. Especially when the people in question were drunk Murim practitioners.

“Wait. You’re…!”

“Oh-ho. Aren’t you the Senior Disciple of the Xiao He Gate? Is that finger they cut off still missing?”

“You bastard! You came looking for a place to die!”

The world might be vast, but enemies had a way of meeting even on a single-plank bridge.

Whenever people tangled in such complicated webs of gratitude and grudges happened to meet, a clash of blades was sure to follow.

Clang! Slash!

Sharp weapons swung at one another, and blood sprayed through the air. The fierce exchange unfolding before them sent the surrounding Murim practitioners into an uproar.

“Waaah!”

“It’s a fight!”

“One silver nyang on the Senior Disciple of the Xiao He Gate!”

“Then I’ll bet two nyang on the Long Serpent Saber!”

They said the two most entertaining things in the world were watching someone else’s house burn and watching someone else fight.

The very few people with no connection to Murim backed away with horrified expressions. But the Murim practitioners, who were crazy about fighting regardless of whether it involved the orthodox, unorthodox, or Demonic Path, shouted and applauded without hesitation.

And amid all that chaos, almost no one noticed the middle-aged man who had just opened the inn’s old door and entered.

Clang! Bang!

Waaah!

A fierce battle was raging in the middle of the inn, but the middle-aged man did not spare it a glance. He flicked a silver nyang toward the innkeeper.

“Two bottles of strong liquor and one roast duck. Bring them to a seat with a good view of the street. Oh, and roast the duck until it’s crisp.”

“Great Hero…”

“Hm?”

The innkeeper bowed deeply toward the middle-aged man.

“I’m sorry, but there aren’t any suitable seats available right now.”

“There aren’t?”

“No, Great Hero. As you can see, so many heroes of the Murim have come to visit…”

The middle-aged man looked around, then suddenly raised his head. Several faces were peering down from the landing above.

“There seem to be seats up there.”

“Ah, I’m terribly sorry, but that floor is occupied by other—”

“That one looks good.”

“W-wait a moment, Great Hero! Great Hero!”

The middle-aged man ignored the innkeeper’s desperate cries.

He strode up the stairs, ignoring the sharp gazes that poured down on him, and muttered,

“Much better. It’s quiet.”

The second floor of the inn was reserved for people of higher status.

It was only about twenty steps above the first floor, but unlike the noisy chaos below, a serious atmosphere hung over the second floor. Nor were the people seated at its tables anything like Third Rate martial artists.

“G-Great Hero! You can’t go up there!”

At the innkeeper’s cry from behind him, the low conversations abruptly stopped.

A graying middle-aged man seated at the table closest to the stairs frowned and spoke.

“Such noise. What is going on?”

“I-I’m sorry, Great Hero. This gentleman seems to have mistaken his place and—”

“Send him downstairs. And quiet down the first floor as well.”

“Yes, sir.”

But the middle-aged man was already walking somewhere else.

“That seat by the window looks fine.”

“Gasp, Great Hero!”

The one who stepped forward in place of the horrified innkeeper was the graying middle-aged man from before.

“Stop.”

The middle-aged man slowly turned around.

“Was that directed at me?”

“Who else would I be speaking to?”

“You?”

“You look a great deal younger than I am, so don’t cause unnecessary trouble. Go back downstairs.”

The graying middle-aged man added one more remark in a dignified tone.

“You appear to be lacking in worldly knowledge, so allow me to enlighten you. I am Fang of the Fang Family, widely known throughout the martial world by the sobriquet Moon Beauty Saber.”

“Oh.”

“That should be enough for you to understand. Now stop making a scene and go downstairs quietly.”

The middle-aged man blinked a few times before speaking.

“What you just said—was it really true?”

Moon Beauty Saber gave a short laugh.

Who was he? He was a top-tier wandering martial artist who had long since reached the level of injuring others with Sword Energy.

He was on an entirely different level from wandering martial artists like Blood Cudgel, who strutted around despite being merely at the early Peak realm.

“Heh heh. Why would I lie? Then again, I suppose it’s understandable that you don’t believe me. You probably never expected to meet me in a place like this.”

“No, not that. I meant, do I really look that way?”

“…?”

What was this man talking about?

Moon Beauty Saber stared blankly at the middle-aged man for a moment, then frowned.

“What do you mean? I don’t understand you at all.”

“You said I looked young. That was certainly true, wasn’t it?”

“…!”

“Hm. I don’t dislike hearing that. Good. I understand.”

Before Moon Beauty Saber could say another word, the middle-aged man let out a hearty laugh and raised a hand toward the window.

“Don’t mind me. Keep drinking. I happen to know someone.”

“Why, you bastard…”

“Great Hero!”

Moon Beauty Saber and the innkeeper shouted at the same time.

That was when the old man drinking alone by the window suddenly spoke.

“I was feeling lonely drinking by myself, so this is perfect. Come, sit.”

“…”

“…”

The innkeeper and Moon Beauty Saber both fell silent.

From the innkeeper’s perspective, the guest had said it was fine, so he had nothing more to say. Moon Beauty Saber, meanwhile, hesitated because of the old man’s manner—a manner that had been bothering him for some time.

*He looks like nothing more than a wealthy old man, but he also seems like no ordinary person… What connection could he have with that ignorant bastard?*

Moon Beauty Saber wanted nothing more than to teach the middle-aged man a lesson right then and there, but he felt strangely uneasy.

Whether he knew what Moon Beauty Saber was thinking or not, the middle-aged man dropped into the seat across from the old man and immediately tilted back a bottle.

“Ah, good. Is this Yeoahong?”

The old man nodded.

“The innkeeper said it had been aged for at least twenty years.”

“It’s good liquor. But among all liquor, strong liquor is still the best. The innkeeper will bring some soon, so have a taste.”

“I’ll pass. I don’t usually drink much.”

“What a shame. But why are you here alone?”

“It’s nothing. I simply thought I would try burying myself among other people after such a long time.”

The old man suddenly turned his head and gazed out the window.

He watched and listened to the many people passing through the street and the raucous noise for a while without speaking. Then he continued.

“Now that I’m here, it isn’t so bad. Being alone like this.”

“You don’t seem to have come alone.”

“Of course I have children and grandchildren. Just as you have a Disciple.”

“I do have one fellow who may be a Disciple or an enemy. But how did you know?”

“How could I not? I even saw him myself.”

Clack.

The middle-aged man set down the bottle with a loud sound.

Liquor had spilled from the corner of his mouth, dampening his beard. Perhaps because of the soft light, the beard looked unusually red.

“Damn it. I knew it. But that brat kept insisting to the very end that he’d never met you.”

“You certainly raised your Disciple well, Fire King.”

The middle-aged man wiped his beard with his sleeve, then stared at the old man.

“Last time, my Disciple caused you trouble. So I came to meet you myself, Azure Sky Sword King.”

The old man—no, the Grand Family Head of the Nangong Family and one of the Ten Kings, the Azure Sky Sword King—smiled faintly.

“That is most welcome news.”

“I knew you, of all people, would recognize this old man.”

“I almost failed to recognize you. Returned to Youth… It was worth waiting for.”

“May I keep the promise I made back then, even if I’m late?”

“I have been waiting for those words. For a very long time.”

Joy filled the Azure Sky Sword King’s eyes.

More than twenty years ago, in exchange for entrusting one person’s life to Jeok Cheongang, he had been promised a duel.

Today’s meeting was the fruit of that long wait.

“What a shame. The strong liquor will be here soon.”

“Let whoever is left standing drink it.”

“What about the sword? Will you be all right without one?”

“The sword?”

The Azure Sky Sword King picked up the two chopsticks lying neatly on the table.

“These will suffice.”

Jeok Cheongang gave a short laugh and looked out the window.

“The sky is blue, and you have a sword in your hand.”

“The sun is up as well, so the timing couldn’t be better.”

Whoooosh.

The wind blew.

Invisible waves of martial aura erupted from the two men’s bodies and swept through every direction.

And before anyone in the inn could notice, the two supreme masters struck at each other.

KABOOM!

* * *

Bang! Bang! KABOOM!

“Good Lord.”

*What in tarnation is that?*

I stood there gaping at the scene visible in the distance beyond the window.

No, it wasn’t only because of the successive booms or the black smoke rising high into the sky.

Unnamed, who realized it a moment after I did, spoke with a hardened expression.

“Did you feel it too, Benefactor?”

I gave a small nod.

A wave of qi that could be felt all the way here despite the considerable distance.

*This is a clash between at least Supreme Peak masters.*

“If something like this happened, then it must be…”

“Amitabha. Yes. It appears to be an assault by Dark Heaven.”

“Dark Heaven, those sons of bitches!”

“Though we took every precaution, this has happened again. Given that, this humble monk will have no choice but to break the precept against killing and go all out against them.”

“I’ll join you. I make a hobby of breaking the no-killing precept against Dark Heaven.”

And it seemed I wasn’t the only one with that hobby.

Ding. Diiing!

“Dark Heaven! It’s an attack by Dark Heaven!”

“Kill them and uphold justice!”

“Beat those wicked fiends to death!”

Along with the alarm bells ringing throughout the area, the Murim practitioners traveling along the main road rushed toward the disturbance like a pack of dogs.

It was a sight that made the blood boil.

*Ah, so this is the Murim Crusade.*

*Our side is fucking strong. And there are a hell of a lot of us.*

Until now, I had suffered every kind of hell against Dark Heaven because of our numerical disadvantage—or simply because of the gap in strength.

I was almost moved to tears.

*I can’t sit this one out.*

“Follow me! Follow me!”

Those who saw me leap out the window and stand tall widened their eyes.

“The Blazing Flame Divine Dragon!”

“It’s the Blazing Flame Divine Dragon of the Jin Family of Taiyuan!”

“Ooooooh!”

Believe it or not, I was quite a big name in Murim.

I was living proof that even a cramped backwater like Shanxi Province could produce a dragon! A young icon of the orthodox factions!

“Waaah!”

“Let’s go! Let’s sweep Dark Heaven away!”

“The Blazing Flame Divine Dragon is with us!”

Whoosh, whoosh, whoosh, whoosh!

The Murim practitioners, their courage redoubled, charged forward with a roar.

Needless to say, Unnamed and I were at the very front.

“Fuck! Wreck ’em all!”

When I shouted with all my internal energy behind my voice, the uproar grew even louder.

With this many Murim practitioners at my side, I was certain we could beat the hell out of any opponent.

“It’s a holy war!”

“Great Hero Jin says it’s a holy war!”

“Kill those demons!”

“Amitabhaaa!”

*You Dark Heaven bastards! Stay right there! I’m bringing the Murim Crusade to you, and I’m going to bash your heads in. Your heads…*

“Ah.”

My brain suddenly stopped working.

A single person was walking out from inside a building burning horribly.

“What the hell are you all doing?”

“…”

*The fiend was ours.*
```
