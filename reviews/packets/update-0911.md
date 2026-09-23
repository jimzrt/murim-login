<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0911.txt",
      "sha256": "85f3cd0960f14845c422691030503bfd4eccc97e97dfad1024641680fdc8be17",
      "bytes": 13241
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3819cc3e25ae28bd68039ec5cc78358764a18cd23d1cf86636c32a86219b2f8d",
      "bytes": 946
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "66855c040f4342a0b241cbbead8026d866de6b64af95427c21f76fe8c96ddd55",
      "bytes": 231435
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "c16db45f2d850a74683ba69f1530863fe3b6514bea4434f8869a747acc6971a4",
      "bytes": 927
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1033bf5b2c2686efe4e88d1a76ef5e933943445d4e9ceb08263794001a165da2",
      "bytes": 759
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "efd90d6bb57812aab2a50bc66a84f504c34b3fb5423b85309d92542c0ad0a363",
      "bytes": 1000
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "016a69f541d8e27a6feaf6f8c4c5a51b7d1a2f5aabae7c2df66dd82e3ed7fbe9",
      "bytes": 1499
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "44ea28b47659a4b6536a932fd285ba7b9fef636d16e18a8c414ab6394f5ae902",
      "bytes": 628
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "40dcb4547fd5fc4e48980a474321c4abfe32c5ec08142909d6cad4af990240ef",
      "bytes": 699
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "490cd68b2f7ca6348d73948ede1e4c19ca218dbb5c8eea5dfa40c729111f0d81",
      "bytes": 263127
    }
  ],
  "estimated_tokens": 10637
}
-->

# Durable State Update — Chapter 911

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 911. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 911. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 911,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 911,
    "continuity_sources": [911],
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
    "Taekyung and the group are facing an advancing army of undead among the black-clad pursuers; roughly half of the first hundred struck by his attack rose again despite severe burns.",
    "Taekyung identified the attackers as undead and ordered the group to run.",
    "Jeok Cheongang is fighting the Eastern Heaven Demon Lord and has unleashed a greater blaze after realizing he can strive beyond his current realm.",
    "Hong Dao once wagered that Jeok would surpass the Three Saints and urged him to trust that prediction."
  ],
  "continuity_sources": [
    910
  ],
  "open_questions": [
    "Who created or commands the undead, and how can they be stopped?",
    "Can Taekyung’s group escape the advancing undead?",
    "Can Jeok Cheongang defeat the Eastern Heaven Demon Lord?",
    "Will Jeok Cheongang surpass the Three Saints?"
  ],
  "safe_through": 910,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 굉도     | **Hong Dao**       |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 법왕     | **Dharma King**               | Hong Dao       |
| 삼성     | **Three Saints**    |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 극양                        | **Extreme Yang**      |
| 상태               | **Status**                     |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 화타 | **Hua Tuo** | Historical physician invoked in Taekyung's comparison for Mungyeong's future medical skill. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 창룡후 | **azure dragon's roar** | Battle cry released by Tang Jinhu. |
| 염라대왕 | **Yama** | Expanded source form of the established underworld ruler term 염라. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 대라신선 | **Great Firmament Immortal** | Legendary immortal invoked by Mungyeong as unable to stop the dragon's death. |
| 창룡 | **Azure Dragon** | Divine dragon form invoked in Hyeongong's blessing. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 법왕 | close deceased friend and peer | you | familiar and reflective | Jeok addresses the Dharma King in private thought while wishing he were present to clarify Jeok's confusion. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 903
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 910
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 910
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 910
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged Disciple and intended heir, regards him as the light of his later years, and will stand by him whatever path he chooses; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 908
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 908
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

## Korean source

```text
＃911화



느껴진다.

몸도, 마음도 날아갈 듯이 가볍다.

전신 깊숙한 곳에서 끓어오르는 힘이, 비록 작게나마 한 걸음 높은 경지로 나아갔다는 환희가 적천강을 휘감았다.

그리고 갑작스럽게 찾아온 그 자그마한 깨달음은, 더욱 강렬하고 거대한 불꽃이 되어 피어오르고 있었다.

지금 이 순간처럼.

화륵.

실로 눈부신, 섬광처럼 빛나는 새하얀 광염(光焰)이 어둠을 깨운다. 집어삼키고 물어뜯으며 나아간다.

눈앞의 적을 향해. 동천마군의 회색빛 눈동자를 뜨겁게 달구며.

“……!”

공간을 지우며 들이닥치는 일권(一拳)에, 동천마군의 눈이 크게 뜨였다.

‘이게 무슨.’

그는 본능적으로 깨달았다.

저것에 담긴 힘은, 지금까지 수없이 부딪치고 피했던 공격과는 질적으로 다르다는 것을.

화왕이라 불리는 저 위대한 무인이 다시 한번 새로운 발걸음을 내디뎠다는 것을.

그리고 지금의 동천마군에게 있어, 그것은 한 가지 사실만을 의미했다.

‘피할 수 없다.’

그 순간.

콰아아아앙!

하늘이 쪼개지는 듯한 굉음과 함께 지축이 뒤흔들렸다.

무시무시한 진동과 힘의 여파가 사방을 휩쓸고, 끔찍한 열기를 머금은 연기와 수증기를 헤치며 한 사람의 신형이 튕겨 나왔다.

쐐애애액!

세찬 파공성과 함께 동천마군의 시야가 수없이 뒤집히던 그때. 적천강은 충격을 이기지 못하고 포탄처럼 쏘아지는 그를 향해 걸음을 떼었다.

쩌적, 쾅!

소리를 앞서나간 움직임.

한 줄기 불꽃이 되어 나아간 적천강은 손을 뻗었다.

십성(十成)의 경지에 다다른, 아니 이제는 어쩌면 그것마저 넘어선 멸염신권이 공간을 새하얗게 물들였다.

꽝!

일격(一擊)이 동천마군의 검을 부러트리고.

꽈앙!

아슬아슬하게 스쳐 지나간 이격(二格)이 지면을 녹였으며.

꽈아아앙!

마지막 삼격(三格)은 비틀거리는 동천마군의 가슴에 다시 한번 작렬했다.

그의 전신을 휘감고 있던 막강한 호신강기(護身罡氣)마저 산산이 부수어 깨트리며.

콰드드득!

대연회장의 지면에 깔려 있던 단단한 청석(靑石)이 두부처럼 으스러진다.

무려 십여 장이나 되는 거리를 몸으로 부수며 튕겨 나가는 동천마군의 모습에, 순식간에 일어난 이 믿을 수 없는 현실을 인지한 이들이 동시에 움직였다.

“놈을, 놈을 죽여라!”

“마군(魔軍)께서 위험하시다!”

“막아!”

곳곳에서 빗발치는 고함과 번뜩이는 날붙이.

그러나, 그 무엇도 지금의 적천강을 막을 수는 없었다.

“감히 그 누가.”

콰직!

“노부의 앞을 막아서느냐.”

퍼어어엉!

그 누구도 적천강에게 닿지 못했다. 닿을 수 없었다.

형형하게 빛나는 검기를 머금은 칼날은 멸염신권의 화염에 녹아내렸고, 공간을 격하고 쏘아진 화염신장은 다가오던 적들을 맹렬하게 휩쓸었다.

“꺼윽, 컥.”

“끄아아악!”

용기를 쥐어 짜내어 정면으로 달려든 자들은 차라리 운이 좋은 편이었다.

조금이라도 불길에 닿은 이들은 자신의 몸뚱어리가 산 채로 타들어 가는 고통을 느끼며 울부짖어야 했으니까.

그리고 그 비명과도 같은 단말마는, 곧 그들의 유언이 되었다.

스륵, 쿵.

짧지만 끔찍했던 고통 속, 숨이 끊어진 시체들이 썩은 고목 나무처럼 널브러진다.

이미 녹아내린 황금빛 갑옷과 한 몸이 되어 눌어붙은 배신자들의 시신 위로, 아직 빛을 잃지 않은 갑옷들이 번쩍였다.

“역적들을 참하라!”

“황제 폐하 만세!”

쉬쉬쉬쉭! 서걱!

믿을 수 없는 적천강의 신위에 얼어붙은 적을 일검에 베어 넘긴 정호군을 시작으로, 그의 뒤를 따라 돌격한 금의위들이 파도처럼 배신자들을 덮쳤다.

카카캉!

퍼걱!

서로를 향해 맹렬히 나아간 병장기가 불똥을 토해 내고, 사방에서 핏물이 솟구친다.

그리고 그 중심에서, 화왕(火王)이라 불리는 거인은 지금껏 그래왔듯이 앞을 가로막은 모든 걸 부수고 태우며 나아갔다.

이 싸움을 끝내기 위해.

지금도 자신을 향해 달려드는 수많은 부나방의 뒤에서 비틀거리며 일어나고 있는 동천마군을 향해.

콰앙!

용암과도 같은 열양지기가 수십여 명의 적들을 집어삼킨다.

본래의 매끄러운 빛을 잃고 처참하게 녹아내린 청석과 아직도 남아 있는 불씨로 인해 장작처럼 타들어 가는 시체들.

감히 그 누구도 막을 수 없는 화염의 길을 만들며 다가온 적천강의 모습에, 동천마군은 탄식과 감탄이 뒤섞인 목소리로 입을 열었다.

“깨달음을…… 쿨럭. 깨달음을 얻었나?”

불과 몇 걸음 앞에서 멈춰 선 적천강은 말없이 동천마군을 응시했다.

그의 상태는 누가 보더라도 처참했다.

신선처럼 새하얗던 수염은 핏물에 젖었고, 팔과 다리가 각각 하나씩 부러져 있었으며, 앞서 잿더미로 화한 의복으로 말미암아 훤히 드러난 가슴팍은 검게 그을려 있었으니까.

설령 화타가 아니라 대라신선(大羅神仙)이 온다고 하더라도 생존을 장담하기 힘든 상태.

그러나 동천마군은 연신 밭은기침을 내뱉으며 말을 이을 뿐이었다.

마치 그렇게 함으로써 자신이 느끼고 있는 이 끔찍한 고통을 잠시라도 덜어내려 하는 것처럼.

“삼성(三星)도 이제는 옛말이 되겠군. 바로 오늘, 이 자리에서 네 번째 별이 떠올랐으니 말이야.”

적천강이 가라앉은 목소리로 대답했다.

“네놈이 뭐라 부르건 상관없다. 그런 것 따위에는 아무런 관심도 없으니까. 다만…….”

저벅.

잠시 멈췄던 걸음이 나아간다. 이 짧은 악연을 마무리 지을 새하얀 겁화가 그의 전신에서 넘실거렸다.

“이제 곧 세 번째 마군(魔軍)이 뒈질 거라는 사실쯤은 알고 있지.”

비틀거리며 서 있는 동천마군을 응시하는 적천강의 눈빛은 그가 지닌 기운과는 달리 차갑고 냉정했다.

조금의 방심도 없이. 가장 확실한 죽음을 위해.

지금까지 암천의 일원들은 여러 번에 걸쳐 믿을 수 없는 능력을 보여 왔고, 그건 적천강이 장장 백 년이 넘는 세월 동안 믿고 있던 세상의 법칙을 정면으로 반박하는 것이었다.

그러나 그 모든 것들은 실패가 아닌 시행착오였다.

더 넓고 높은 어딘가로 나아가기 위한 과정.

예측할 수 없는 변수를 거쳐 살아남을 때마다 적천강은 새로운 경험과 깨달음을 얻었고, 조금씩 강해졌다.

구화산의 노괴(老怪)는, 여전히 성장하고 있었다.

자신의 제자가 그러하듯이.

그리고 이제는 죽고 없는 절친한 벗이 과거에 장담했듯이.

“어느 땡중이 오래전 그런 말을 했었다. 머지않아 노부가, 삼성을 뛰어넘을 것이라고.”

저벅.

신중하게 걸음을 내딛는 적천강을 바라보며, 동천마군이 힘없이 웃었다.

“그 땡중의 말이 옳았군.”

“그래, 그랬지. 이제 와 곰곰이 돌이켜보면 그 땡중이 재주를 부려 천기(天氣)라도 읽은 게 아닌가 싶은데…… 영영 확인할 수가 없게 됐어. 그 이유를 아느냐?”

동천마군은 대답하지 않았다. 천기를 읽었다는 것에서, 적천강이 말하는 땡중이 누구인지 깨달았으니까.

그리고 적천강 역시 대답을 기대하지 않았다.

“죽었다. 바로 네놈들, 암천의 손에.”

“……법왕(法王) 굉도.”

“차라리 노부가 구화산에 있었다면 이토록 분노하진 않았을 것이다. 손 쓸 수도 없는 일이었을 테니까.”

하지만 아니었다.

법왕 굉도는, 적천강의 벗은 소림사 경내에서 혈주에 의해 죽음을 맞이했다.

불과 촌각이면 닿을 수 있었던 그곳에서.

“땡중은 그렇게 죽었다. 노부가 갔을 때는 이미 늦었지.”

한때 적천강은 두려워했다.

자신에게 찾아온 이 빌어먹을 노환이, 언젠가 다시 깨어나 죽어 가고 있던 벗의 마지막 모습마저 지워 버릴까 봐. 피가 터져 나오도록 입술을 깨물며 했던 맹세마저 잊게 할까 봐.

“그날, 노부는 맹세했다.”

저벅.

다시 한번 걸음을 내디디며, 적천강은 말을 이었다.

“암천이라는 꼬리표를 달고 있는 놈들을, 단 하나도 빼놓지 않고 모조리 죽여 없애겠노라고.”

드득, 드드드득.

지면이 흔들린다. 대기가 들끓었다.

공기마저 지워 버리는 극양(極陽), 아니 극염(極炎)이라 불릴 만한 기운이 마치 용암처럼 적천강의 전신에서 흘러넘치고 있었다.

당장이라도 동천마군을 집어삼킬 듯이.

“그리고 오늘, 노부의 손으로 직접 한 놈을 더 저승으로 보낼 수 있게 되겠지.”

다섯 걸음.

그건 적천강과 동천마군 사이에 놓인 거리였고, 그들 중 누군가의 생사(生死)를 가르기에는 너무나도 짧은 거리였다.

“유언은…… 염라대왕 앞에서 해라.”

그 순간.

팟.

동천마군이 발을 뻗었다. 그의 몸이 사라졌다. 그 속도와 움직임에도 조금 전까지만 하더라도 가까워지던 죽음을 기다리는 모습은 조금도 찾아볼 수 없었다.

쉬쉭!

적천강은 귓가를 파고드는 소리에 반응했다.

겹쳐진 파공성은 하나가 아닌 둘, 아니 셋이었다.

“갈(喝)!”

파아앙!

전장을 떨어 울리는 창룡후(蒼龍吼)와 함께, 외침에 실린 공력이 압축된 공기를 터트렸다.

그리고 동시에, 보이지 않은 손에 의해 이끌리듯 적천강의 등 뒤로 쏘아지던 두 줄기의 섬광이 튕겨 나갔다.

바로 동천마군이 중단전(中丹田)의 힘으로 끌어당긴 두 자루의 검이었고, 적천강은 전신에서 끌어올린 기운을 양손에 담아 퍼올리듯 후려쳤다.

머리 위 하늘을 향해, 유성처럼 떨어져 내리는 동천마군을 향해.

후웅.

분명 닮았음에도 놀라울 정도로 다른, 두 개의 백색 기운이 서로를 향해 나아간다.

그들의 눈에는 개미의 움직임보다도 천천히. 그러나 다른 이들은 볼 수조차 없는 속도로.

그리고 두 괴물이 각자의 전력을 다해 후려친 쌍장(雙掌)이 맞닿은 그 순간.

콰아아앙!

구구구구궁!

모두의 시야를 가리는 눈부신 섬광이, 끔찍하리만치 거대한 미증유의 힘이 터져 나와 사방을 물들였다. 이미 전장이 되어 버린 드넓은 대연회장을 집어삼키며 부풀어 올랐다.

화아악.

어둠이 사라졌다. 불안하게 흔들리던 횃불도, 눈앞의 적을 향해 시퍼런 날붙이를 쑤셔 넣던 이들과 그들이 토해 내던 성난 고함도 지워졌다.

아니, 찰나의 순간 모두의 감각을 점령한 섬광과 굉음에 잠시나마 눈과 귀가 멀어 버렸다는 표현이 더욱 정확했다.

……!

……!!

아무것도 보이지도, 들리지도 않는 새하얀 세상.

그 안에 갇혀 버린 사람들은 적아를 잊은 채 극심한 혼란과 함께 얼어붙었지만, 극소수에 속하는 몇몇 이들만큼은 예외였다.

파파팟!

적천강과 동천마군은 서로를 향해 끊임없이 달려들었다.

소리보다도 앞선 움직임으로 상대의 공격을 흘려보내고, 동시에 반격하고, 재차 쏘아졌다.

이 세상에 있어서 그 모든 것은 찰나에 불과했지만, 이미 인간의 한계를 벗어던진 초인들에게는 달랐다.

그들은 멈춰 버린 듯한 시간 속에서 수백 합을 겨루었고, 수십 번의 위기를 겪었으며, 마침내 이 끝나지 않을 것 같던 생사결의 끝자락에 도달했다.

퍼걱!

뼈와 살이 으스러지는 소리와 함께 한 사람의 신형이 비틀거린다.

그러나 그의 가슴을 관통하고 등 뒤로 튀어나온 주먹은, 넘실거리는 백색 화염은 쓰러지는 것조차 허락하지 않았다.

“실로, 실로 대단한…….”

힘없이 늘어지는 목소리.

깊게 가라앉은 적천강의 눈동자에, 이미 산산이 부서진 두 팔을 축 늘어트린 동천마군의 모습이 비쳤다.

“염라가 네놈에게 왜 죽었냐 묻거든.”

푸욱.

천천히 빠져나오는 주먹. 그제야 비로소 천천히 허물어지는 신형.

“……땡중의 벗이 보냈다 전해라.”

쿵.

마침내 쓰러진 동천마군을, 더는 아무런 생명이 느껴지지 않는 시체를 적천강은 말없이 내려다보았다.

그리고 참았던 숨을 내뱉으며 돌아선 그 순간.

콰득.

느껴져서는 안 될, 도무지 이해할 수 없는 서늘한 고통이 그의 전신을 엄습했다.
```

## Final English reading copy

```markdown
# Chapter 911

He could feel it.

His body and mind both felt light enough to take flight.

A power boiling deep within him, and the joy of having taken even a small step into a higher realm, engulfed Jeok Cheongang.

And the little insight that had come to him so suddenly was blooming into an even more powerful, tremendous blaze.

Just like now.

*Fwoosh.*

A dazzling white flame, shining like a flash of light, roused the darkness. It devoured and tore its way forward.

Toward the enemy before him. Heating the Eastern Heaven Demon Lord’s gray eyes.

“……!”

The Eastern Heaven Demon Lord’s eyes widened as a fist came crashing toward him, erasing the space between them.

*What is this?*

He realized it instinctively.

The power contained in that fist was qualitatively different from the countless attacks he’d clashed with and evaded until now.

That great martial artist known as the Fire King had taken another step forward.

And for the Eastern Heaven Demon Lord, that meant only one thing.

*I can’t dodge it.*

At that moment—

*Kwaaaang!*

The earth shook as a deafening roar split the sky.

A terrifying tremor and the force of the impact swept over everything. Through the smoke and steam, heavy with dreadful heat, a figure was hurled away.

*Whooosh!*

As the Eastern Heaven Demon Lord’s view spun around and around amid a fierce rush of air, Jeok Cheongang stepped toward him. It was the Demon Lord who had been hurled away like a cannonball by the impact.

*Crack—boom!*

A movement that outstripped sound.

Jeok Cheongang shot forward like a streak of flame and reached out his hand.

The Flame-Extinguishing Divine Fist, brought to full mastery—or perhaps now beyond even that—washed the space in white.

*Bang!*

The first strike broke the Eastern Heaven Demon Lord’s sword.

*Boom!*

The second barely grazed past him, melting the ground.

*Kaaa-bang!*

The final, third strike slammed into the staggering Eastern Heaven Demon Lord’s chest once more.

It shattered even the formidable Body-Protecting Qi that had enveloped him.

*Krrrunch!*

The hard bluestone covering the grand banquet hall crumbled like tofu.

At the sight of the Eastern Heaven Demon Lord being hurled away, his body smashing through more than ten *jang* of ground, those who registered the unbelievable reality unfolding in an instant all moved at once.

“Kill him! Kill that bastard!”

“The Demon Lord is in danger!”

“Stop him!”

Shouts rained down from every direction. Blades flashed.

But nothing could stop Jeok Cheongang now.

“Who dares—”

*Crack!*

“—to stand in this old man’s way?”

*Boom!*

No one could reach Jeok Cheongang. No one could even come close.

Blades carrying gleaming Sword Energy melted in the flames of the Flame-Extinguishing Divine Fist, while the Flame Divine Palm shot across the space and swept fiercely over the approaching enemies.

“Urk—cough!”

“Aaargh!”

Those who summoned up their courage and charged him head-on were the lucky ones.

Anyone who so much as touched the flames had to howl as their own flesh burned away while they were still alive.

Those screams, like cries of agony, soon became their last words.

*Rustle. Thud.*

In their brief but horrific agony, the corpses of the dead sprawled like rotting trees.

Over the bodies of the traitors, fused with their golden armor as it melted and stuck to them, armor that had yet to lose its shine gleamed.

“Execute the traitors!”

“Long live His Majesty the Emperor!”

*Shh-shh-shing! Slash!*

Jeong Hogun was the first to cut down an enemy frozen by the unbelievable might Jeok Cheongang had displayed. The Embroidered Uniform Guards who charged after him swept over the traitors like a wave.

*Clang-clang!*

*Thwack!*

Weapons clashed fiercely, spitting sparks. Blood sprayed in every direction.

And at the center of it all, the giant known as the Fire King did what he had always done: smashed and burned everything in his path as he pressed forward.

To end this fight.

Toward the Eastern Heaven Demon Lord, who was staggering back to his feet behind the countless moths still rushing at him.

*Boom!*

Scorching Yang Qi, hot as lava, swallowed dozens of enemies.

The bluestone had lost its smooth, original sheen and melted into a wretched mess. Corpses still smoldered like firewood, flecks of flame clinging to them.

As Jeok Cheongang approached, forging a path of fire no one dared block, the Eastern Heaven Demon Lord spoke in a voice mixed with a sigh and admiration.

“You attained… cough. You attained enlightenment?”

Jeok Cheongang stopped just a few steps away and stared at him without a word.

His condition was pitiful by anyone’s standards.

His beard, once white as snow, was soaked with blood. One arm and one leg were broken. His clothes had already been reduced to ash, leaving his chest exposed and blackened with burns.

His injuries were so grave that not even Hua Tuo—or a Great Firmament Immortal—could guarantee he would survive.

Yet the Eastern Heaven Demon Lord only kept coughing roughly and continued to speak.

As if doing so could ease, if only for a moment, the terrible pain he was feeling.

“The Three Saints… are a thing of the past now, I see. A fourth star has risen right here, today.”

Jeok Cheongang answered in a low voice.

“Call it whatever you want. I don’t care about things like that. But…”

*Step.*

The footsteps that had paused began moving again. White hellfire rippled over his body, ready to bring this brief, ill-fated encounter to an end.

“You know one thing, at least. The third Demon Lord is about to die.”

Jeok Cheongang’s gaze on the unsteady Eastern Heaven Demon Lord was cold and clear, unlike the energy he wielded.

Not a hint of carelessness. He would make certain the man died.

Until now, the members of Dark Heaven had demonstrated unbelievable abilities time and again, directly contradicting the laws of the world Jeok Cheongang had believed in for more than a hundred years.

But all of it had been trial and error, not failure.

A process of moving toward somewhere broader and higher.

Each time he survived an unpredictable turn of events, Jeok Cheongang gained new experience and insight. He grew stronger, little by little.

The old monster of Mount Jiuhua was still growing.

Just as his Disciple was.

Just as his close friend, now dead, had once promised he would.

“A certain bald monk once said, long ago, that before long, this old man would surpass the Three Saints.”

*Step.*

Watching Jeok Cheongang tread carefully toward him, the Eastern Heaven Demon Lord gave a faint smile.

“That monk was right.”

“Yes, he was. Thinking back on it now, I wonder if that monk had some trick for reading the heavenly patterns… but I’ll never be able to find out. Do you know why?”

The Eastern Heaven Demon Lord didn’t answer. From the mention of reading the heavenly patterns, he’d realized who the bald monk Jeok Cheongang meant.

And Jeok Cheongang wasn’t expecting an answer.

“He’s dead. Killed by you people of Dark Heaven.”

“…Hong Dao, the Dharma King.”

“If I’d been at Mount Jiuhua, I wouldn’t have been this angry. There would’ve been nothing I could do about it.”

But that wasn’t what had happened.

Hong Dao, the Dharma King and Jeok Cheongang’s friend, had met his death at the hands of the Blood Lord within the grounds of Shaolin Temple.

Somewhere Jeok Cheongang could have reached in a matter of moments.

“The monk died like that. By the time I got there, it was already too late.”

There had been a time when Jeok Cheongang was afraid.

Afraid that the damned infirmities of old age that had come for him would someday wipe away even the final image of his dying friend. That they would make him forget the vow he’d made, biting his lip until it bled.

“That day, I made a vow.”

*Step.*

Taking another step, Jeok Cheongang continued.

“I swore I’d kill every last one of those bastards with the name Dark Heaven attached to them.”

*Rumble, rumble.*

The ground shook. The air boiled.

An energy so hot it seemed to erase even the air itself—an energy worthy of being called Extreme Yang, no, Extreme Flame—flowed from Jeok Cheongang’s entire body like lava.

As if ready to swallow the Eastern Heaven Demon Lord at any moment.

“And today, I’ll send one more of them to the afterlife with my own hands.”

Five steps.

That was the distance between Jeok Cheongang and the Eastern Heaven Demon Lord. At such close range, one of them could be dead in an instant.

“Save your last words for Yama.”

At that moment—

*Fap.*

The Eastern Heaven Demon Lord lunged. His body vanished. There was not the slightest hint in his speed or movement of the man who, moments ago, had seemed to be waiting for death to draw near.

*Shh-shing!*

Jeok Cheongang reacted to the sound piercing his ears.

There were two overlapping rushes of air. No—three.

“*Hah!*”

*Paaang!*

As the azure dragon’s roar shook the battlefield, the internal energy carried in his shout burst the compressed air.

At the same time, two streaks of light shot toward Jeok Cheongang’s back as if guided by an invisible hand—then were knocked away.

They were the Eastern Heaven Demon Lord’s two swords, drawn toward him by the power of his Middle Dantian. Jeok Cheongang brought up the energy from his entire body, poured it into both hands, and swung upward as if scooping something from below.

Toward the sky above him. Toward the Eastern Heaven Demon Lord, plunging down like a meteor.

*Whoom.*

Two white energies—clearly similar, yet astonishingly different—raced toward each other.

To their eyes, they moved slower than an ant. Yet they were moving too fast for anyone else to see.

And the moment the two palms, each monster swinging with everything he had, collided—

*Kaaaang!*

*Rumble, rumble, rumble!*

A blinding flash obscured everyone’s vision. An unbearably vast, unprecedented force burst outward, engulfing everything in light. It swelled, swallowing the sprawling grand banquet hall that had already become a battlefield.

*Whooosh.*

The darkness vanished. The unsteady torches disappeared, along with the people thrusting blue blades at their enemies and the angry shouts they’d been roaring.

No—in that instant, it was more accurate to say that everyone’s sight and hearing had been swallowed by the flash and roar.

……!

……!!

A white world where nothing could be seen or heard.

Those trapped inside it forgot friend and foe alike, frozen in utter confusion. Only a tiny handful were exceptions.

*Papapat!*

Jeok Cheongang and the Eastern Heaven Demon Lord charged at each other without pause.

They moved faster than sound, redirecting their opponent’s attacks, counterattacking, then shooting at each other again.

To the world, it all lasted but an instant. But to those superhuman beings who had cast off the limits of humanity, it was different.

Within time that seemed to have stopped, they fought hundreds of exchanges, faced danger dozens of times, and finally reached the end of their seemingly endless life-and-death duel.

*Thwack!*

With the sound of bone and flesh crushing, someone staggered.

But the fist that had pierced his chest and burst out his back—and the white flames that licked around it—wouldn’t even let him fall.

“Truly… truly incredible…”

His voice trailed off, drained of strength.

In Jeok Cheongang’s deeply shadowed eyes, the Eastern Heaven Demon Lord’s two arms hung limp, shattered beyond recognition.

“If Yama asks why you died…”

*Shunk.*

Jeok Cheongang’s fist slowly pulled free. Only then did the other man’s body begin to crumple.

“…Tell him a friend of that bald monk sent you.”

*Thud.*

Jeok Cheongang silently looked down at the fallen Eastern Heaven Demon Lord, the corpse in which not a trace of life remained.

Then, just as he let out the breath he’d been holding and turned away—

*Crack.*

A cold pain that shouldn’t have been there, a pain he couldn’t begin to understand, swept through his entire body.
```
