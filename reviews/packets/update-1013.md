<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1013.txt",
      "sha256": "0b1caaeec197e090dc85912e7e74283eb38dfe14114608d4e69f156e69254d2b",
      "bytes": 13708
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9025ec39b1a48feb55cc315d4f7cb498d7797c46596ab16031cadd2af50421dc",
      "bytes": 1072
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "30a1ac39205f115d497753cde782f960c1172e8e0adb18958de06997f7b51e57",
      "bytes": 237950
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "855c0f28eb9c5eeec39966625d794d9b0cec7cc1fd536e0bd5355cf1c537b6ba",
      "bytes": 1000
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "670f9fdd474e03322da515d65ee185c77c7bb0a79f20eff034ec0da90b305b23",
      "bytes": 1408
    },
    {
      "path": "characters/Ma Junggeol.md",
      "sha256": "f8b01b3b228898e19d703da59c126601c512a69890465fab6e27c46754e09810",
      "bytes": 636
    },
    {
      "path": "characters/Namho.md",
      "sha256": "0ed9027313d98dbe05d33a3b6ea0fe44a4ddcaa514b67015b99c5290c9861c28",
      "bytes": 1092
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8a36c21af3e33ce8297d5a41a312212a7b74793dcd26a6bf5d9ca9c9372e2ef2",
      "bytes": 276653
    }
  ],
  "estimated_tokens": 10155
}
-->

# Durable State Update — Chapter 1013

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
1 and safe_through 1013. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1013. Profile updates may replace only one
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
  "chapter": 1013,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1013,
    "continuity_sources": [1013],
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
    "Ma Junggeol and the Seven Masters of Baekma Bang are traveling with Taekyung’s group after recounting their history.",
    "The Seven Masters revere a mysterious master they call the Lord, who appeared in Ningxia, subdued the area, and has lived there for nearly ten years; they know little about his identity and describe him as highly unpredictable.",
    "Taekyung and Jeok Cheongang believe Ma Junggeol and his brothers are telling the truth and do not appear to be Dark Heaven spies.",
    "Taekyung has asked Ma Junggeol’s group how long it would take to bring the Lord to their destination."
  ],
  "continuity_sources": [
    1011,
    1012
  ],
  "open_questions": [
    "Who is the Lord, and what are his motives and connection, if any, to Dark Heaven?",
    "Will Ma Junggeol’s group bring the Lord to Taekyung’s destination?",
    "What is Dark Heaven’s full strength and objective in the western desert, and have its forces begun advancing?"
  ],
  "safe_through": 1012,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 굉도     | **Hong Dao**       |
| 법왕     | **Dharma King**               | Hong Dao       |
| 종남파    | **Zhongnan Sect**                |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마적     | **mounted bandits**                              |                                                       |
| 제자     | **Disciple**                                 |
| 감숙     | **Gansu**              |
| 노부      | **this old man / I**                                            |
| 마중걸 | **Ma Junggeol** |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 기련산 | **Qilian Mountains** | Mountain range in Qinghai from which the Qilian Three Fiends emerged. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 마방 | **horse caravans** | Descendants of northern mounted tribes who traveled ancient trade routes between the Outer Lands and the Central Plains. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 멸지 | **Land of Ruin** | Name used for the desert region beyond which Dark Heaven’s forces are approaching. |
| 백마방 | **Baekma Bang** | Ma Junggeol’s horse-caravan group, founded by reformed mounted-bandit leaders. |
| 백마칠종 | **Seven Masters of Baekma Bang** | Collective title for Ma Junggeol and his six associates. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 적천강 | 법왕 | close deceased friend and peer | you | familiar and reflective | Jeok addresses the Dharma King in private thought while wishing he were present to clarify Jeok's confusion. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 마중걸 | 적천강 | visiting horse-caravan chief to legendary martial master | Great Hero Jeok Cheongang | polite and deferential | Recognizes Jeok as the Fire King. |

## Listed compact profiles

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 990
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1012
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Ma Junggeol.md

# Ma Junggeol (마중걸)

- **Safe through:** Chapter 1012
- **Aliases:** Chief of Baekma Bang
- **Role:** Ma Junggeol is the chief of Baekma Bang, a horse-caravan group founded by reformed Ningxia mounted-bandit leaders.
- **Personality:** Though timid by nature, he is earnest and protective of his group, and places firm trust in the benefactor who led them onto a better path.
- **Voice:** Not established
- **Relationships:** He leads six sworn brothers who, with him, are known as the Seven Masters of Baekma Bang, and trusts the benefactor they call the Lord.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1012
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

## Korean source

```text
＃1013화



“대, 대인을?”

생각지도 못한 말이었는지, 마중걸과 그의 의형제들은 크게 뜨인 눈으로 나를 바라보다 뒤늦게 정신을 차렸다.

“아니, 대인은 갑자기 왜…….”

말꼬리를 흐리는 마중걸을 향해, 나는 담담하게 대꾸했다.

“이번 일과 어느 정도 연관이 있으니 갑자기는 아니지. 이유야 뭐, 굳이 말 안 해도 알고 있죠?”

“지금 나를…… 아니 우리를 암천의 간자로 의심하고 있는 거요?”

“그렇진 않습니다. 적어도 이 자리에 있는 당신들에 한해서만큼은.”

“하면, 대인을?”

내가 대답 대신 어깨를 으쓱해 보이자, 마중걸을 비롯한 백마칠종의 얼굴이 딱딱하게 굳었다.

“말도 안 되는 소리!”

“젠장, 도대체 아니라고 몇 번을 말해야 하는 거요?”

“저희 대형께서도 말씀드렸다시피, 대인께서는 결코 그런 분이 아니십니다. 직접 들으셨으니 아실 거 아닙니까?”

당연히 알지.

매우 보기 드문 부류의 희한한 인간이라는 것만.

하지만 지금은 아, 저런 사람도 있구나 하고 넘어갈 만한 상황이 아니다.

“갈! 필요하다면 내 목이라도 걸겠소!”

나는 한 박자 늦게 외친 난쟁이를 바라보며 턱을 긁적였다.

“그쪽에 계신 분, 본인 목을 거시겠다고?”

“……어?”

막상 이렇게 콕 찝을 줄은 몰랐는지, 순간 움찔한 난쟁이가 입술을 오물거렸다.

“그, 목은 좀 그렇고 손목을…….”

“남아일언중천금! 당연히 걸겠소! 둘째 형님 목을 자르시오!”

“아니, 이 미친놈아!”

불쑥 끼어든 주먹코의 대리 배팅에 난쟁이가 허둥지둥하던 그때, 내가 착 가라앉은 음성으로 입을 열었다.

“손목이건 모가지건, 어차피 수지타산이 안 맞는 건 똑같은데.”

“그게 무슨…….”

“궁금해서 묻는 건데, 당신들 눈에는 이 많은 사람이 단지 심심해서 옆 동네 마실 나가는 거로 보입니까?”

“……!”

삽시간에 무거워진 분위기 속, 흔들리는 그들의 눈동자에는 어느새 저 멀리 앞서가는 수많은 이들의 뒷모습이 비치고 있었다.

흑룡마문. 종남파.

감숙 무림에 속한 크고 작은 문파의 무인들.

그리고 마지막, 나와 화룡각 대원들까지.

단지 이뿐만이 아니다. 수천의 인마(人馬)가 전력을 다해 달려가는 방향에는, 언제 위기에 처할지 모를 수만 명의 아군이 있다.

난쟁이 한 사람만이 아니라 칠종백마 전원이 목숨을 건다 해도, 이는 같은 저울에 올려 비교할 수 없는 막중한 무게였다.

“전쟁은 도박이 아니라는 말, 혹시 여기서 나만 들어 봤나?”

혼잣말처럼 내뱉은 물음에 마중걸은 물론 누구 하나 감히 입을 열지 못했다.

당연한 일이다.

고작 마방 몇 명의 증언으로 의문의 초절정 고수에 대한 의심을 완전히 거둔다는 것이, 얼마나 허황된 바람인지 저들 역시 알고 있을 테니까.

천하의 운명을 판가름할 대전쟁은 현재 진행형이고, 전쟁은 결코 도박이 아니다.

게다가…….

‘충분한 이유가 있으니, 괜한 의심도 아니지.’

내심 중얼거린 나는 마중걸을 똑바로 응시했다.

전날 백마칠종 사이에 오갔던 전음의 내용을 떠올리며.

“당신들끼리 주고받은 전음 중에 아주 흥미로운 내용이 있는 것 같던데, 어떻게 생각합니까?”

“흥미로운 내용이라면, 어떤…….”

“똑똑히 들었습니다. 그 대인이라는 사람이 앞으로 나아가야 할 방향을 이것저것 알려 줬다고. 그것도 제법 최근에.”

마지막 뒷말에 유독 힘을 주어 덧붙이자, 안 그래도 침잠하게 가라앉아 있던 마중걸의 눈동자가 눈에 띌 만큼 요동쳤다.

“그, 그건.”

“문득 궁금해지네요. 그 최근이 정확히 언제인지, 그리고 무엇을 알려 줬는지. 안 그렇습니까?”

불현듯 고개를 돌려 던진 물음에, 상황을 주시하던 적천강이 고개를 끄덕였다.

“네 녀석이 하는 말을 듣자 하니 노부도 궁금해지는구나. 그토록 중요한 얘기를 왜 지금까지 입 밖으로 꺼내지 않았는지도.”

돌이켜보면 누구 한 사람쯤은 충분히 의심할 만한 일이었다.

전직 마적단. 그것도 지금껏 한 번도 두각을 드러내지 못한 그저 그런 뜨내기들인 백마칠종이 어떻게 멸지(滅智)의 사막을 넘겠다는 대담무쌍한 발상을 떠올렸을까.

그리고 비록 짧은 시간이지만 저들을 가장 가까이에서 지켜 봐왔고, 전음의 내용 역시 모조리 기억하고 있는 나는 이미 그 의문에 대한 답을 짐작하고 있었다.

“서쪽으로 향하는 새로운 교역로를 뚫어야 한다는 생각은, 처음부터 당신들이 떠올린 것이 아니었습니다. 내 말이 틀립니까?”

“……!”

“……!”

아마도 전날 남호의 조언을 따라 일찍이 후미로 위치를 옮기지 않았다면, 지금 내가 뱉은 말에 깜짝 놀랄만한 사람들이 제법 있었을 것이다.

하지만 반경 십여 장에는 우리뿐이었고, 마중걸에게 남은 선택지 역시 하나뿐이었다.

“……더 숨길 것도 없군.”

무거운 침묵 끝에 흘러나온, 시인이나 다름 없는 한 마디.

그의 의형제들이 다급히 뭐라 외치기 직전, 손을 들어 모두의 말문을 틀어막은 나는 담담하게 질문을 이어 갔다.

“그 사실을 숨겼던 이유는?”

“대인께서 원치 않으셨을 테니까. 그분 덕분에 마음을 고쳐먹고 지금껏 잘 살아왔는데, 우리가 금수(禽獸)도 아니고 어찌 그 사실을 대놓고 떠들 수 있겠소?”

“더 자세히.”

“이번이 처음은 아니오. 십여 년 전부터 오늘날에 이르기까지 대인께서는 나와 아우들에게 이런저런 조언을 해 주셨소. 첫 대면 당시에는 그분의 신위(神威)에 놀라 수하가 되길 청했으나, 일언지하에 거절하시며 말씀하시더군.”

복잡한 표정을 한 의형제들을 천천히 바라보며, 마중걸이 말을 이었다.

“송충이는 솔잎을 먹어야 하는 법이라고. 차라리 우리처럼 개심의 여지가 있는 마적들을 모아 한 울타리를 이루는 것이 어떻겠느냐고. 하여 나와 아우들은 대인께서 하신 조언을 따르기로 했소.”

“백마방(白馬方)…….”

“맞소. 그것이 백마방의 시작이었지. 그 후로도 대인께서는 어려운 일이 생길 때마다 늘 올바른 방향을 알려 주셨소. 새로운 교역로 역시 마찬가지였고.”

“그렇다면 몇 년 전부터 서쪽 교역로를 염두에 두고 있었다는 말도 혹시.”

내 물음에 담긴 의미를 즉각 이해한 마중걸이 황급히 손을 내저었다.

“이런 상황에서 믿어 줄지는 모르겠지만, 그것만큼은 틀림없는 사실이오. 다만 대인께서 그리 조언하셨을 뿐이지. 그 후로 우리는 서쪽으로 향하는 새로운 경로를 탐색하기 시작했고, 초원만이 유일한 대안책이라는 것을 깨달았소. 당연히 그동안은 엄두도 내지 못했지만.”

“서부 초원의 공백을 금세 알아차릴 수 있었던 것 또한 그 덕분이었을 테고.”

불쑥 울려 퍼진 적천강의 뇌까림에, 마중걸이 고개를 끄덕였다.

“그렇습니다. 물론 상황이 이리 뜻하지 않은 방향으로 흘러갈 줄은 저희야 까맣게 몰랐지요. 대인께서도 마찬가지 셨겠지만 말입니다.”

그야 당연하다.

설령 천기(天氣)를 읽을 줄 알았던 법왕 굉도가 아직 살아있었다 하더라도, 수년 뒤에나 벌어질 일을 어찌 그토록 자세히 예측할 수 있었겠나.

‘그쯤 되면 천기를 읽는 수준이 아니라, 예언이지. 예언.’

게다가 이어지는 마중걸의 이야기를 들어 보니, 대인이라 불리는 그자의 조언은 딱히 특별하지도 않았다.

어디 갈 곳도 없고, 농사 한번 지어 본 적 없는 착한 마적 몇 명에게 특기를 살려서 백마방을 차리게 도와준 것이 시작이다.

사막 너머로 향하는 새로운 교역로?

범인(凡人)이라면 쉽게 생각할 수 없는 대담한 발상이긴 하지만, 애초에 그자의 무위나 행적을 들어 보면 평범과는 거리가 멀다.

사막에 인접한 거대 방파의 수장이거나, 야망이 큰 상단주들 역시 한 번쯤은 품었을 희망 사항이기도 하고.

하지만 뭘까, 알 수 없는 이 기묘한 느낌은.

‘뭐지, 도대체.’

고개를 흔들어 잡생각을 털어낸 나는, 마른침을 꼴깍 삼키고 있는 마중걸을 향해 잠시 닫혀 있던 입술을 뗐다.

“그렇다면 마지막으로 한 가지만 더, 우리를 찾아온 건 누구의 생각입니까?”

“부끄럽지만, 그 역시 대인의 조언이었소.”

“역시.”

“사실 한나절 정도는 더 빨리 올 수 있었소. 하지만 우리끼리 결정하기에는 워낙 심각한 사안이라, 녕하 땅에 들어서자마자 대인을 찾아뵈었지.”

“계속하십시오.”

“초원과 사막에서 있었던 일을 말씀드리니, 어디서 개가 짖냐는 듯이 술만 몇 사발 들이켜시더니 그러시더이다. 진작 감숙으로 갔어야 할 놈들이 왜 아직도 여기에 엉덩이를 붙이고 앉아 있느냐고.”

“……!”

“그 후의 일은 뭐, 이렇게 됐소. 제기랄.”

마중걸이 반쯤 체념한 얼굴로 입을 다물자 잠시 침묵이 흘렀다.

그리고 말들이 내뿜는 거친 숨결과 세차게 달려가는 말발굽 소리만 울려 퍼지던 그때, 눈치를 살피던 주먹코가 조심스럽게 입을 열었다.

“칠주야(七晝夜). 칠주야 정도면 될 듯싶습니다.”

“갑자기 그게 무슨 개소리냐?”

생뚱맞은 말에 적천강이 눈살을 찌푸리자, 식겁한 주먹코가 다급한 손짓으로 나를 가리켰다.

“저, 저기 계신 제자분께서 아까 저희에게 물어보시지 않았습니까. 대인을 모시고 돌아오기까지 어느 정도의 시일이 걸리겠냐고. 거기에 대해 대답해 드린 겁니다.”

처음이 어렵지, 두 번째부터는 쉽다.

입술만 오물거리고 있던 마중걸의 의형제들이 그제야 한마디씩 말을 보탰다.

“셋째 형님이 간만에 옳은 말씀하시네. 칠주야면 떡을 치지.”

“맡겨만 주십시오. 죽을힘을 다해 모셔오겠습니다.”

“그, 물론 기련산이면 칠주야지만 대설산이나 돈황(敦煌)까지라면 좀 더 걸릴 수도 있긴 한데.”

“대인께서 뭐 극악무도한 마두도 아니고, 이대로 쭉 궁벽한 촌구석에 틀어박혀 있을 바에야 이참에 무림맹에 출사(出仕)하시는 것도 나쁘지 않지. 안 그렇소?”

“갈! 나쁘지 않다니! 이미 우리 일곱 형제를 보내어 암천에 대한 경고를 하신 것만으로도 큰 공을 세우셨으니 필시 대인께도 아주 좋은 선택이 될…….”

쉭, 빠악!

“커헉!”

“이런 호로 새끼를 봤나, 갈갈거리지 말라니까 노부의 말을 귓등으로 들어?”

유령 같은 움직임으로 말안장을 박차고 날아올라, 난쟁이의 뒤통수를 후려갈기고 돌아온 적천강이 나를 향해 고개를 돌렸다.

“그래서, 어찌하겠느냐?”

백마칠종의 얼굴을 천천히 훑은 내가 대답했다.

“엿새. 아니, 닷새.”

“예?”

“닷새로 하죠. 지금 이 행군이 멈추는 장소가 기련산이건 대설산이건, 돈황이건 그 안에 돌아오는 것으로.”

“……!”

“물론 한 사람은 무조건 남아야 합니다. 그게 누구인지는 굳이 내 입으로 말 안 해도 아실 거고.”

“자, 잠깐. 그 말씀은 우리 대형을……!”

내 말에 담긴 의미를 알아차린 백마칠종이 입을 모아 반박하려던 그때, 마중걸이 불현듯 입을 열었다.

“좋소.”

“대형!”

“우형(愚兄)은 이곳에 남아도 상관없다. 그러니 너희는 한시라도 빨리 대인을 모시고 돌아오너라. 어서!”

단호한 마중걸의 태도에서 무언가를 느낀 것일까.

뭐라 말할 듯이 입술을 달싹이던 그들은, 내 조용한 고갯짓에 황급히 말머리를 돌려 대열을 이탈했다.

두두두두!

금세 어둠에 파묻혀 사라지는 여섯 필의 초원마를, 마중걸은 심유한 눈빛으로 지켜보았다.

그리고 결의에 찬 표정과는 달리, 미세하게 움직이는 입술은 차마 크게 말하지 못한 진심을 담고 있었다.

“시발, 진짜 좆 됐다…….”

“…….”

“…….”

이거 진짜 뭐 하는 새끼지.

어느새 눈가가 촉촉해진 마중걸을 나와 적천강이 황당하다는 듯 바라보고 있던 그때, 들썩이는 말안장 위에서 거의 널뛰기 수준의 묘기를 선보이던 남호가 다가와 말을 걸었다.

“할 얘기가 있는데. 잠깐 시간 되나?”

곧장 수뇌부에게 이 사실을 전달할 생각이었던 나는 고개를 저었다.

아니, 정확히는 고개를 저으려고 했다.

다음 순간, 한껏 목소리를 낮춘 남호의 속삭임이 귓가를 파고들기 전까지는.

“중요한 이야기일세. 지금이 아니라면 할 수 없는.”
```

## Final English reading copy

```markdown
# Chapter 1013

“Y-you mean the Lord?”

It must have been the last thing they expected. Ma Junggeol and his sworn brothers stared at me with wide eyes, then belatedly came to their senses.

“No, why the Lord all of a sudden…?”

I answered Ma Junggeol, whose voice trailed off, in an even tone.

“It’s not all of a sudden. He’s connected to this situation to some extent. And I’m sure you know why I’m asking, so I don’t need to spell it out, do I?”

“You suspect me… no, us, of being Dark Heaven’s spies?”

“Not exactly. At least, not the people here.”

“Then, the Lord?”

When I answered with a shrug instead of words, Ma Junggeol and the rest of the Seven Masters of Baekma Bang stiffened.

“That’s ridiculous!”

“Damn it, how many times do we have to tell you it isn’t true?”

“As our Chief already told you, the Lord is absolutely not that kind of person. You heard it all for yourself, didn’t you?”

Of course I did.

I’d learned only that he was a highly unusual person—the kind you rarely came across.

But this wasn’t a situation where I could just think, *Huh. People like that exist,* and let it go.

“Enough! If necessary, I’ll stake my own neck on it!”

I scratched my chin as I looked at the shorty who’d shouted a beat late.

“You over there. You’re staking your own neck?”

“…Huh?”

Perhaps he hadn’t expected me to call his bluff so directly. The shorty flinched and fumbled with his lips.

“I-I mean, the neck is a bit much. Maybe my wrist…”

“A man’s word is worth its weight in gold! Of course I’ll stake it! Cut off Second Brother’s head!”

“Hey, you crazy bastard!”

While the shorty flailed at the bulbous-nosed man’s sudden offer to wager on his behalf, I spoke in a low, measured voice.

“Whether it’s a wrist or a head, the math still doesn’t work out.”

“What do you mean…?”

“I’m asking because I’m curious. Do you think all these people are taking a casual trip to the next town over just because they’re bored?”

“……!”

The mood turned heavy in an instant. Their wavering eyes were fixed on the backs of the countless people riding far ahead.

The Black Dragon Demon Gate. The Zhongnan Sect.

Martial artists from large and small sects throughout Gansu Murim.

And finally, me and the members of the Fire Dragon Pavilion.

And that wasn’t all. In the direction thousands of men and horses were riding at full speed lay tens of thousands of our allies, who could find themselves in danger at any moment.

Even if not just one shorty but all the Seven Masters of Baekma Bang staked their lives, their wager couldn’t be weighed against that burden.

“Am I the only one here who’s ever heard the saying, ‘War isn’t a gamble’?”

Ma Junggeol and the others didn’t dare answer my question, which I’d murmured almost to myself.

Naturally.

They had to know how absurd it would be to cast aside all suspicion of a mysterious Supreme Peak master based on nothing but the testimony of a few horse-caravan men.

The Great War that would decide the fate of the world was already underway, and war was no gamble.

Besides…

*There’s good reason to be suspicious. This isn’t paranoia.*

I murmured to myself and stared straight at Ma Junggeol.

Remembering the Sound Transmissions that had passed among the Seven Masters the previous day.

“I heard something very interesting in the Sound Transmission you exchanged among yourselves. What do you make of that?”

“If you heard something interesting, what was it…?”

“I heard you say the Lord had given you all kinds of advice about which direction to take. And not that long ago, either.”

I put particular emphasis on the last part. Ma Junggeol’s eyes, already lowered with worry, visibly wavered.

“T-that…”

“Now I’m curious. Exactly how recently was it? And what did he tell you? Don’t you think?”

I suddenly turned and tossed the question to Jeok Cheongang, who had been watching the situation. He nodded.

“Hearing you say that, this old man is curious too. Why did you keep something so important to yourselves until now?”

Looking back, it was more than enough to make anyone suspicious.

How had the Seven Masters of Baekma Bang—former mounted bandits, no less, and ordinary drifters who’d never distinguished themselves—come up with the bold idea of crossing the Land of Ruin?

Though I’d watched them closely for a short time, and remembered every word of their Sound Transmission, I already had a guess at the answer.

“The idea of opening a new trade route to the west wasn’t yours from the start. Am I wrong?”

“……!”

“……!”

If I hadn’t followed Namho’s advice the day before and moved back early, quite a few people might have been startled by what I’d just said.

But within a dozen or so yards, it was just us. And Ma Junggeol had only one option left.

“…There’s nothing more to hide.”

The words slipped out after a heavy silence. They were as good as an admission.

Before his sworn brothers could hurriedly shout something, I raised a hand to silence them and calmly continued my questions.

“Why did you hide it?”

“Because the Lord wouldn’t have wanted us to. Thanks to him, we changed our ways and have lived well ever since. We’re not animals—how could we go around openly blabbing about that?”

“Tell me more.”

“This wasn’t the first time. From more than ten years ago right up until today, the Lord has given my younger brothers and me all kinds of advice. When we first met him, we were so overwhelmed by his divine might that we asked to become his subordinates. He refused us outright and said…”

Ma Junggeol slowly looked over his sworn brothers, their expressions complicated, then went on.

“A caterpillar should eat pine needles. He asked if it might be better to gather mounted bandits like us, who still had a chance to repent, and make a home together. So my younger brothers and I decided to follow his advice.”

“Baekma Bang…”

“That’s right. That was how Baekma Bang began. And even after that, whenever we ran into trouble, the Lord always showed us the right way forward. The new trade route was no different.”

“Then when you said you’d been considering a western trade route for years, was that…”

Ma Junggeol immediately understood what I meant and hastily waved his hands.

“I don’t know if you’ll believe me in a situation like this, but that part is absolutely true. The Lord simply advised us to do it. Afterward, we started searching for a new route west and realized the grasslands were our only option. Of course, we hadn’t dared attempt it all that time.”

“And that must also be how you noticed the gap in the western grasslands so quickly.”

At Jeok Cheongang’s sudden mutter, Ma Junggeol nodded.

“That’s right. Of course, we had no idea things would take such an unexpected turn. The Lord probably didn’t, either.”

Naturally.

Even if Hong Dao, the Dharma King who could read the heavenly patterns, were still alive, how could he have predicted in such detail something that would happen years later?

*At that point, it wouldn’t be reading the heavenly patterns. It’d be prophecy. Prophecy.*

And from the rest of Ma Junggeol’s story, the advice from the man they called the Lord didn’t seem all that special.

He’d started by helping a few decent mounted bandits—with nowhere to go and no experience farming—put their skills to use and form Baekma Bang.

A new trade route beyond the desert?

It was a bold idea, not one an ordinary person would come up with easily. But given his martial prowess and deeds, the man was anything but ordinary.

It was also the kind of wish the heads of the great groups bordering the desert or ambitious merchant-house leaders might have entertained at least once.

But what was this strange feeling I couldn’t explain?

*What the hell?*

I shook my head to clear away my stray thoughts, then parted my lips, which had been closed for a while, toward Ma Junggeol, who was swallowing nervously.

“Then I have just one last question. Whose idea was it to come find us?”

“I’m ashamed to say it was the Lord’s advice as well.”

“Just as I thought.”

“To be honest, we could have arrived half a day earlier. But it was such a serious matter that we couldn’t decide among ourselves, so as soon as we entered Ningxia, we went to see the Lord.”

“Go on.”

“We told him what happened on the grasslands and in the desert. He knocked back several bowls of liquor as though he were listening to a dog bark, then said, ‘You idiots should’ve gone to Gansu ages ago. Why are you still sitting on your asses here?’”

“……!”

“After that, well, here we are. Damn it.”

Ma Junggeol fell silent, his face half resigned. A brief silence followed.

Then, just as only the horses’ ragged breathing and the clatter of their hooves thundering along could be heard, the bulbous-nosed man glanced around and cautiously spoke up.

“Seven days and nights. I think that should do it.”

“What the hell are you talking about all of a sudden?”

Jeok Cheongang frowned at the out-of-nowhere remark. The bulbous-nosed man panicked and hurriedly pointed at me.

“Y-your Disciple over there asked us earlier how long it would take to bring the Lord back, didn’t he? That’s what I was answering.”

The first time is hard. After that, it gets easier.

Ma Junggeol’s sworn brothers, who’d been moving their lips without managing to say anything, finally chimed in.

“Third Brother’s right for once. Seven days and nights will be plenty.”

“Just leave it to us. We’ll bring him back, even if we have to give it everything we’ve got.”

“W-well, it’d take seven days and nights if we’re going to the Qilian Mountains. It might take longer if it’s the Great Snow Mountain or Dunhuang.”

“It’s not as if the Lord’s some fiendishly evil fiend. Rather than staying cooped up in some remote village, why not take this chance to enter the Murim Alliance’s service? What do you think?”

“Hah! ‘Not a bad idea,’ you say? He’s already done a great service by sending the seven of us to warn you about Dark Heaven. It’s bound to be an excellent choice for the Lord too, since…”

Whoosh! Wham!

“Gah!”

“You little shit! I told you to stop shouting ‘Hah!’ Did my words go in one ear and out the other?”

Jeok Cheongang moved like a ghost, kicked off the saddle, soared through the air, and smacked the shorty on the back of the head. Then he returned and turned to me.

“So, what will you do?”

I slowly swept my gaze across the Seven Masters of Baekma Bang and answered.

“Six days. No—five.”

“Huh?”

“Let’s make it five days. Whether this march stops at the Qilian Mountains, the Great Snow Mountain, or Dunhuang, you’ll be back within that time.”

“……!”

“Of course, one person has to stay behind, no matter what. You know who that is. I don’t have to say it out loud.”

“W-wait. You mean our Chief…!”

The Seven Masters of Baekma Bang began to object all at once, having realized what my words meant. Then Ma Junggeol suddenly spoke.

“Fine.”

“Chief!”

“I can stay here. You all go bring the Lord back as quickly as you can. Go!”

Perhaps they sensed something in Ma Junggeol’s firm manner.

The others, their lips moving as if they wanted to say something, turned their horses in a hurry and left the formation at my quiet nod.

*Thud-thud-thud!*

Ma Junggeol watched the six grassland horses disappear into the darkness, his gaze deep and steady.

And though his face was resolute, his barely moving lips held the words he couldn’t bring himself to say aloud.

“Fuck. I’m so fucking screwed…”

“……”

“……”

*What the hell kind of guy is this?*

Just as Jeok Cheongang and I were staring at Ma Junggeol, whose eyes had grown damp, in disbelief, Namho came over, performing an almost acrobatic routine on his bouncing saddle.

“There’s something I need to talk to you about. Got a minute?”

I was planning to report this to the command staff right away, so I shook my head.

No, more precisely, I was going to shake my head.

Until the next moment, when Namho lowered his voice and whispered into my ear.

“It’s important. I can only tell you now.”
```
