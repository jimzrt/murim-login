<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1088.txt",
      "sha256": "3ac5bf0219b847c7955832f18c19243212e8daf3f788e0487521dd86234717a7",
      "bytes": 14210
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8805a17f118ea45a9e451b8566efbd92d84dfbfa2fff70c9f177af28ad4db84f",
      "bytes": 1313
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4ed8101452df2425b89e5c8364c1fe6dfdf6c2111129928b6ce5e8f121d10f80",
      "bytes": 243758
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b24bac097b24c2e1f682fd49ac13a632e761bd356b1c211689b92ced6be99613",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "9c5d5c3c11d5c09ea2e7a2fab6b2a3aec0f38821b770dbbf090fbc7b3d9af689",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "4a1a5624fb1284a87578d71a4fcc0fd25494c9960386a9ac7543bb4bdc31645b",
      "bytes": 1502
    },
    {
      "path": "characters/Tae Gunak.md",
      "sha256": "304cac9a96e97c1561c0461116185c0f935b4099223bd4d07a421c75cbec0efc",
      "bytes": 642
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "d15ae9d6d177967a67585f6d05ae47be31dce5d7bb9992b3c3ad66088b46311a",
      "bytes": 650
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c4a0e6a83aedc85b5783bb09dd09c0203fec4ce272e8879854936f6a4d11be19",
      "bytes": 286755
    }
  ],
  "estimated_tokens": 11046
}
-->

# Durable State Update — Chapter 1088

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
1 and safe_through 1088. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1088. Profile updates may replace only one
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
  "chapter": 1088,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1088,
    "continuity_sources": [1088],
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
    "The Yangtze River Channel League and Green Forest Alliance are advancing west in a large combined force.",
    "Ten thousand Dark Heaven faithful entered the Central Plains through hidden magic formations and joined the two advancing alliances.",
    "Most hidden magic formations retain one use; two or three used in the Shaolin attack may be spent.",
    "The Blood Lord’s forces are marching on Xining to take Qinghai; securing Jin Taekyung is a further objective if possible.",
    "Mae Jonghak and the New Murim Alliance have prepared an operation against Dark Heaven; Zhuge Feng has the intelligence and tasking to execute it.",
    "The Zhuge Clan is preparing to leave its current home immediately.",
    "Zhuge Feng urged Jin Taekyung to hold on in the west."
  ],
  "continuity_sources": [
    1086,
    1087
  ],
  "open_questions": [
    "What is the black-robed captive in Qinghai’s identity and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "Who is the black-robed man beside Pa Ryun?"
  ],
  "safe_through": 1087,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 파륜     | **Pa Ryun**        |
| 궁성     | **Bow Saint**                 | —              |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 무당파    | **Wudang**                       |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 게이트     | **Gate**              |
| 사천     | **Sichuan**            |
| 청해     | **Qinghai**            |
| 무당산    | **Mount Wudang**       |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 태군악 | **Tae Gunak** | Green Forest Battle King. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 군선 | **military vessel** | Vessel carrying the Hubei government troops and sailors. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 포달랍궁 | **Potala Palace** | Palace in Tibet. |
| 녹림투왕 | **Green Forest Battle King** | Epithet of the Green Forest Alliance Leader, distinguished from the Ten Kings. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1086
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1082
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1081
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Tae Gunak.md

# Tae Gunak (태군악)

- **Safe through:** Chapter 1082
- **Aliases:** Green Forest Battle King
- **Role:** Tae Gunak is the Green Forest Battle King and the founder of the current Green Forest Alliance.
- **Personality:** Ruthless in pursuing what he wants, he is strategic enough to set aside his longstanding rivalry with Pa Ryun when their plan requires cooperation.
- **Voice:** He speaks in profane, cutting taunts and refers to himself as 노부.
- **Relationships:** Pa Ryun is his longtime rival and current collaborator in a plan to take control of the Yangtze.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 1087
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
1088화




나는 지금껏 숱한 위기를 넘어왔다.

당장 게이트 안에서만 따져도 생사가 오가는 순간을 무수히 맞닥트렸으니, 경험으로만 치면 여느 노강호 못지않다고 해도 과언이 아니다.

그렇기에 아주 잘 알고 있다.

이럴 때일수록 더욱더 냉철하게 상황을 판단해야 한다는 것을.

그리고 서녕(西寧)에 도착한 지 벌써 나흘이라는 시간이 흐른 지금, 나는 냉철한 판단과 추가적인 정보들을 통해 마침내 한 가지 결론에 도달했다.

“무진아.”

“예. 뭐든 명령만 내리십쇼.”

혁무진이 활활 타오르는 눈빛으로 나를 바라보며 가슴을 두드렸다.

“조장님의 든든한 오른팔인 이 혁무진이 있잖습니까.”

초라한 새끼발가락 같은 녀석을 향해, 내가 입을 열었다.

“아무래도 좆된 것 같다.”

“예?”

“좆된 것 같다고. 진짜로.”

“……진심이세요?”

활활 타오르던 눈동자가 찬물이라도 끼얹은 것처럼 차갑게 식었지만, 나는 담담하게 대답할 수밖에 없었다.

“어. 완전히.”

“아니, 며칠 전까지는 안 그러셨잖아요.”

“그랬지. 처음에는.”

하지만 그때와는 상황이 천지 차이다.

장강수로맹과 녹림맹.

두 도적 떼에게 뒤통수를 거하게 얻어맞은 것으로도 모자라 서장의 포달랍궁까지 암천과 손을 잡았으니까.

이처럼 절묘한 시점에 벌어진 포달랍궁의 발호는, 더 이상 사천(四川)의 지원도 기대할 수 없게 됐다는 뜻이기도 했다.

그리고 중원은.

“장강의 지류를 지키고 있던 대국의 군선들까지 전멸당한 이상, 당분간 중원의 수로(水路)는 완전히 놈들의 수중에 떨어진 거나 다름없어.”

부정하고 싶지만, 더 이상은 부정할 수 없는 현실이었다.

해상왕(海上王) 파륜이 이끄는 장강수로맹의 수적들이 대국을 상대로 엄청난 대승을 거두었다는 소문은, 이미 전날 밤 도착한 전서응을 통해 사실로 확인되었으니까.

“이번에 대패하긴 했어도 아직 남아있는 군선들이 많지 않습니까? 대국의 여력이 이 정도도 아니고, 또 장강이 얼마나 넓은데요.”

혁무진의 말도 맞다.

대국이 괜히 대국이겠나.

비록 이번 장강수로맹과의 전투로 극심한 피해를 보긴 했지만, 이 정도로 장강의 지배권을 완전히 상실한다면 애당초 천하의 주인을 자처하지도 못했을 것이다.

다만 중요한 것은.

“시간. 시간이 문제지. 그렇지 않으냐?”

불쑥 끼어든 익숙한 목소리.

어느샌가 나타난 적천강의 등 뒤에서 모습을 드러낸 궁성이 말을 받았다.

“저들에게 주어진 그 당분간의 시간이, 우리에게는 무엇보다 치명적일 테고.”

맞다.

삼일천하건, 화무십일홍이건 간에 현재의 장강수로맹을 당장 막을 방법은 없다.

대국이 국가의 권위를 앞세워 닥치는 대로 선박을 징발하고, 천하 각지에 흩어진 수군 전력을 집결시킬 때쯤에는 모든 것이 한발 늦은 후일 것이다.

그때쯤에는 청해성, 아니 바로 이곳 서녕이 앞뒤로 완전히 포위된 상황일 테니까.

“그래서 그 염병할 도적놈들이 몇이나 모였다더냐?”

적천강의 물음에 내가 대답했다.

“현재까지 추정하기로는 대략 삼만입니다.”

“허, 개떼처럼 몰려오는군. 하기야 흑도 놈들이 자랑할 만한 게 머릿수밖에 없긴 하지.”

“머릿수만 많았다면 차라리 한결 나았겠죠. 머리만 사라지면 알아서 허물어질 테니까.”

어느 곳에서나 그렇지만, 흑도와 사파는 특히 구심점의 중요성이 두드러지는 집단이다.

강력한 무력과 용인술을 바탕으로 무리의 중심이자 머리가 되는 개인에 의존하여 이합집산(離合集散)을 반복하는 것이 그들의 본질이니까. 

해상왕 파륜.

그리고 녹림투왕 태군악.

흑도를 상징하는 두 초절정 고수만 제거한다면 장강수로맹과 녹림맹의 연합군은 그리 까다로운 상대가 아닐지도 몰랐다.

물론, 이건 어디까지나 새로운 불청객들이 등장하지 않았을 때의 이야기지만.

“그래, 암천. 그놈들이 합류했다고 했었지.”

“예. 그것도 무려 일만. 총병력의 삼분지 일입니다.”

내 대답을 들은 적천강이 입맛을 다셨다.

“목줄을 아주 단단하게 채웠군. 감히 주인에게 이빨을 들이대지 못하도록.”

“그래서 더 문제인 거죠. 이제는 파륜과 태군악이 어떻게 된다 하더라도 저희에게 달려들 테니까.”

“그렇겠지. 말로만 듣던 괴이한 사술의 존재를 확인한 겁쟁이 놈들은 더욱더 꼬리를 말 테고.”

무려 일만이나 되는 적들이 튀어나왔다.

그것도 중원의 한복판에서.

중원 무림에 있어 이동진(移動陳)의 존재는 늘 우려의 대상이었지만, 그 우려가 현실이 되는 것은 전혀 다른 문제다.

그리고 이는 제갈세가나 무당파와 같은 명문대파(名門大波)도 외면할 수 없는 문제였던 모양이다.

호북 무림의 패자나 다름없는 그들조차, 감히 정면에서 맞서지 못하고 회피를 택했으니.

그중에서도 특히 제갈세가는 수백여 년간 뿌리내린 본가를 떠나 무당산으로 피신하기까지 했다고 들었다.

‘상대적으로 다른 명문대파에 비해 무력이 약하니 이해가 안 되는 건 아니지만……정말 그 선택이 최선이었을까.’

나는 문득 제갈세가의 가주, 와룡객 제갈풍을 떠올렸다.

그리 오랫동안 이어진 인연은 아니었지만, 호북에서 머무르는 동안 곁에서 지켜본 바에 의하면 그는 괜찮은 사람이었다.

마치 거친 물살 속의 바위처럼, 자유분방했으나 흔들리지 않는 뚝심이 있었고 이를 받쳐줄 만한 능력도 출중했던.

그리고 무엇보다, 그 역시 대협(大俠)이라 불리기에 조금의 부족함도 없던 이였다.

‘그런데 어째서?’

묻고 싶다.

지금처럼 마음속으로가 아니라, 그들의 앞에서.

구파일방과 오대세가, 수많은 정파의 문주와 가주들.

그들 모두가 모여 세운 하나의 깃발. 무림맹(武林盟).

스스로를 정파인이라 칭하기를 주저하지 않던 그들의 눈을 똑바로 들여다보며 묻고 하고 싶었다.

이것이 당신들이 그토록 자랑스럽게 여겼던 정도(正道)냐고.

서쪽으로 향하는 배반자들을 막지 못한 이유가, 당신들이 말하는 대의(代議)냐고.

으득.

어느샌가 힘이 들어간 주먹에서 뼈소리가 울려 퍼진 그때. 침잠한 눈빛으로 나를 응시하고 있던 적천강이 문득 입을 열었다.

“위기 앞에서는 비겁해질 수 있지. 누구든.”

“알고 있습니다.”

나는 조용히 덧붙였다.

지금까지도 흉터처럼 남아있는 과거를 떠올리며.

“저도 그랬었으니까요.”

“두 번 다시 그러지 않겠다는 뜻으로 들리는구나.”

“약속했습니다. 저 스스로에게.”

“네 녀석도 뼈저리게 느끼고 있겠지만, 현재까지 밝혀진 것으로만 따져도 놈들의 전력은 상상 이상이다. 이대로 서녕이 포위된다면 우리로서는 매우 어려운 전투가 될 터.”

그 말에 동의하듯 조용히 상황을 지켜보던 궁성 역시 고개를 끄덕였다.

무인이라면 감히 꿈에도 바라지 못할 만큼 드높은 경지에 오른 두 사람이었으나, 그런 그들조차 패배라는 단어를 떠올릴 정도로 현재의 상황은 최악이었다.

“앞서 노부가 말했었지. 위기 앞에서는 누구나 비겁해질 수 있다고.”

적천강의 심유한 시선이 나를 향한다. 착 가라앉은 목소리가 그 뒤를 이었다.

“지금 같은 상황이라면 설령 후일을 도모한다 해도, 천하의 그 누구도 네 녀석에게 손가락질하지 못할 것이다.”

후일을 도모한다.

그 짧은 한마디에 담긴 의미를 깨달은 혁무진의 눈이 크게 뜨이고, 궁성은 침묵을 지켰다.

그리고 나는.

“그렇겠죠. 아마도, 아니 분명히.”

적천강을 똑바로 바라보며, 말을 이었다.

“만약 제가 후일을 도모……아니 도망친다고 해도 그들에게는 절 욕할 자격이 없으니까요.”

“설령 그렇다 해도 상관없다. 만약 네 녀석을 욕하는 자가 있다면 노부가 친히 그놈의 혀를 뽑을 것이고, 삿대질하는 놈의 손가락을 잿가루로 만들어버릴 테니.”

“그 또한 알고 있습니다.”

“그런데?”

“남겠습니다. 이곳에.”

내 담담한 대답에 적천강이 미간이 일그러졌다.

“어째서냐.”

“저희가 이대로 떠나면 청해는 끝장이니까요. 서녕에 머무르고 있는 수많은 양민들에게는 도망칠 시간조차 주어지지 않을 겁니다.”

“우리가 이곳에서 옥쇄(玉碎)한다면, 그때는 청해가 아니라 천하가 놈들의 손아귀에 떨어질지도 모른다.”

이 말은 결코 과신도, 과언도 아니다.

삼성(三星)과 십왕(十王)은 천하 무림의 상징이자 가장 강력한 전력이니까.

부끄럽지만, 어느덧 하나의 상징으로 자리매김한 나 역시도 그렇다.

더불어 전력의 공백이란 곧 패배로 직결되는 법.

침묵하는 나를 향해 적천강은 탄식처럼 말을 이었다.

“이미 천하가 외면했다. 구파일방과 오대세가가, 무림맹이 등을 돌렸다. 한데도 그런 머저리 같은 선택을 해야겠단 말이냐?”

바로 그 순간이었다.

내가 굳게 닫힌 입술을 연 것은.

“그렇다 하더라도, 해야죠.”

“뭐라?”

“아니, 모두가 외면하고 등을 돌렸으니 더욱더 해야 하는 겁니다.”

옥은 산산이 부서지는 그 순간마저도 아름답다.

수십 조각으로 나뉘며 뿜어내는 그 빛은 그 어느 때보다도 찬란하다.

그것이 옥쇄다.

그렇기에, 옥쇄다.

파괴라는 단어를 잊을 만큼 찬란했기에.

부서질지언정 더럽혀지지 않았기에.

“오물과 먼지로 뒤덮인 옥을 보신 적이 있습니까?”

크게 뜨인 눈으로 나를 바라보는 적천강을 향해, 나는 느리지만 또렷한 목소리로 말을 이어갔다.

“저는 없습니다. 하지만 압니다. 이미 지저분하게 더럽혀진 옥은 잠시나마 그 가치를 잃을 겁니다.”

물론 그렇다 할지라도 옥이 지닌 본질은 사라지지 않는다.

겉보기에는 오물에 불과할지라도, 그 속에는 빛이 숨겨져 있으니까.

하지만 아름다운 표면을 뒤덮은 오물을 본 사람들은 아무도 손을 대려 하지 않을 것이다.

어느 날 한바탕 쏟아진 빗줄기가 옥을 씻어내리지 않은 한은. 

옥의 본모습을 기억하는 누군가가 그것을 찾아 정성 들여 닦지 않는 한은.

그러니.

“더럽혀지는 것보다, 부서지는 것이 낫습니다.”

“……!”

“……!”

“……!”

파르르 떨리는 공기를 느끼며, 나는 참았던 숨을 토해냈다.

그래. 이것이 옳다.

비록 그 끝이 죽음일지라도, 본래의 찬란한 빛을 잃어서는 안 된다.

모두가 기억하게끔 만들어야 한다. 대의라는 변명과 잃어버릴 것에 대한 불안감에 사로잡혀 잠시 잊고 있었던 가장 중요한 것을 깨닫게 만들어야 한다.

바로 정의(正義)라는 옥을.

그리고 나는, 그것을 지키기 위해 온 힘을 다할 것이다.

부서지지도, 더럽혀지지도 않겠다.

찬란한 마지막 순간을 맞이하기에는, 아직 해야 할 일들이 너무나도 많이 남아있으니까.

세상에 그림자를 드리운 가장 거대하고도 단단한 벽이 남아있으니까.

‘천주(天主).’

성큼 가까워진 그 두 글자의 의미가 마음속으로 울려 퍼진 그때였다.

무겁게 가라앉은 공기 속, 고개를 숙인 채 상념에 젖어있던 적천강이 불현듯 입술을 뗀 것은.

“오물과 먼지로 뒤덮인 옥을 본 적이 있느냐고?”

혼잣말처럼 중얼거린 그가 고개를 들었다. 

비록 육신은 젊어졌으나, 세월이 담긴 그 노회한 눈동자에 익숙한 얼굴이 비쳤다.

“그래, 보았다. 아주 똑똑하게 기억하고 있느니라.”

그가 나를 바라본다.

그리 오래되지 않은 과거의 그 날을 떠올린, 깊게 가라앉아 있던 눈빛이 빛을 발한다.

“그때 깨달았다. 눈앞의 비루먹고 나약한 핏덩이가, 얼마나 찬란한 빛을 간직하고 있는지.”

“……!”

“노부가 말했었지. 네 녀석을 욕하거나 손가락질하는 놈들이 있다면, 내 친히 그놈들을 응징하겠노라고. 하지만 알고 있느냐?”

미간에 패인 주름이 깊어진다. 

어느덧 선명한 웃음을 머금은 그가, 천천히 손을 뻗어 내 어깨를 짚었다.

“만약 네 녀석이 그들과 같은 선택을 했다면, 노부는 결코 널 용서하지 않았을 것이다.”

궁성이 은은한 미소를 띤 채 입을 열었다.

“안타깝게도 그럴 일은 없겠군요. 그러기에는 너무 좋은 제자를 두었으니.”

나도 모르게 웃음이 흘러나왔다.

그래, 그랬겠지.

내가 아는 적천강은 처음부터 그런 사람이었으니까.

우선 당신의 하나뿐인 제자를 욕하는 놈들을 찾아가 자근자근 밟은 다음, 남은 힘으로 멍청한 제자를 흠씬 두들겨 팼을 사람이니까.

“아무래도 그 힘, 다른 곳에 쓰셔야겠네요.”

내 말에 크게 소리 내어 웃은 적천강이 대답했다.

“그럴 생각이다. 젖 먹던 힘까지 쥐어 짜내서.”

그리고 그 말은, 채 반나절도 지나지 않아 현실이 되었다.
```

## Final English reading copy

```markdown
# Chapter 1088

I’d made it through more crises than I could count.

Even if I considered only what I’d faced inside Gates, I’d been in life-or-death situations countless times. By sheer experience, it wouldn’t be an exaggeration to say I was as seasoned as any old master.

So I knew very well:

The more dire the situation, the more clearheadedly you had to assess it.

And now, four days after arriving in Xining, I’d finally reached a conclusion, thanks to some clearheaded thinking and a few more pieces of information.

“Mujin.”

“Yes, sir. Just give the order.”

Hyuk Mujin looked at me with blazing eyes and thumped his chest.

“Your reliable right-hand man is right here, Captain.”

I opened my mouth to the guy who was about as useful as a pathetic little toe.

“I think we’re fucked.”

“Pardon?”

“I said I think we’re fucked. For real.”

The fire in his eyes went out as if someone had doused it with cold water, but I could only answer calmly.

“Yeah. Completely.”

“But you weren’t saying that a few days ago.”

“I wasn’t. Not at first.”

But the situation had changed beyond recognition.

The Yangtze River Channel League and the Green Forest Alliance.

As if getting blindsided by those two bands of thieves wasn’t enough, Potala Palace in Tibet had joined forces with Dark Heaven.

Potala Palace’s rise at such a perfectly awful moment also meant we could no longer count on support from Sichuan.

And the Central Plains—

“Now that even the Great Nation’s military vessels guarding the Yangtze’s tributaries have been wiped out, the river routes through the Central Plains are basically in their hands for the time being.”

I wanted to deny it, but the truth was impossible to deny now.

A messenger eagle had arrived the night before, confirming the reports that Seafaring King Pa Ryun’s Yangtze River Channel League pirates had scored an overwhelming victory against the Great Nation.

“Even if they suffered a crushing defeat this time, don’t they still have plenty of military vessels left? The Great Nation has more strength than that, and the Yangtze is huge.”

Mujin had a point.

The Great Nation wasn’t called great for nothing.

The battle with the Yangtze River Channel League had dealt it a terrible blow, but if that were enough to make it lose control of the entire Yangtze, it never could have claimed to rule the world in the first place.

The important thing, though, was—

“Time. It’s a question of time, isn’t it?”

A familiar voice cut in.

Bow Saint emerged from behind Jeok Cheongang, who had appeared at some point.

“The time they’ve gained, however brief, will be more damaging to us than anything.”

Exactly.

Whether their reign lasted only three days or their glory faded as quickly as a flower, there was no way to stop the Yangtze River Channel League right now.

By the time the Great Nation invoked its authority to requisition ships wherever it could and gathered its naval forces from across the land, it would be too late.

By then, Qinghai Province—no, Xining itself—would be completely surrounded, front and back.

“So how many of those damn bandits have gathered?”

At Jeok Cheongang’s question, I answered,

“Our estimate so far is around thirty thousand.”

“Hah. They’re swarming in like a pack of dogs. Then again, numbers are about the only thing those dark-path bastards have to brag about.”

“If it were just numbers, that would be much better. Take out their heads, and the rest would collapse on its own.”

As was true everywhere, the dark-path figures and the unorthodox factions were especially dependent on having someone at their center.

Their nature was to gather and scatter around individuals who became the head of the group through overwhelming strength and the ability to command others.

Seafaring King Pa Ryun.

And Green Forest Battle King Tae Gunak.

If we took out those two Supreme Peak masters who embodied the dark path, the combined forces of the Yangtze River Channel League and the Green Forest Alliance might not be such a difficult opponent.

Of course, that was only if no new uninvited guests showed up.

“Right, Dark Heaven. You said they’d joined them.”

“Yes. Ten thousand of them. A full third of their forces.”

Jeok Cheongang smacked his lips at my answer.

“They’ve put a tight leash on those two. Made sure they won’t dare bare their teeth at their master.”

“That’s what makes it worse. Even if Pa Ryun and Tae Gunak are taken out now, their forces will still come after us.”

“Of course. Those cowards have seen for themselves that the dark arts they’d only heard about are real. They’ll be even more inclined to tuck their tails between their legs.”

Ten thousand enemies had appeared.

And right in the heart of the Central Plains.

The existence of Moving Formations had always been a source of concern for the Murim of the Central Plains. But having that concern become reality was another matter entirely.

It seemed even the great sects like the Zhuge Clan and Wudang couldn’t ignore the problem.

Even they, more or less the dominant powers of Hubei’s Murim, had chosen to avoid a direct confrontation.

I’d heard that the Zhuge Clan had gone so far as to flee to Mount Wudang, abandoning the family home where they’d put down roots for hundreds of years.

*They’re weaker than the other great sects, so I understand. But was that really the best choice?*

I found myself thinking of Zhuge Feng, Family Head of the Zhuge Clan and the Crouching Dragon Guest.

We hadn’t known each other for all that long, but from what I’d seen of him while I was in Hubei, he was a good man.

Like a rock in a raging current, he was carefree yet steadfast, with the ability to back up that resolve.

And most of all, he was a man who deserved to be called a Great Hero.

*So why?*

I wanted to ask.

Not in the privacy of my own thoughts, but to their faces.

The Nine Sects and One Gang. The Five Great Families. The many Sect Leaders and Family Heads of the orthodox factions.

The Murim Alliance—a single banner raised by all of them.

I wanted to look each of them in the eye, men who never hesitated to call themselves righteous, and ask:

Was this the righteous path they were so proud of?

Was this the great cause they spoke of, the reason they couldn’t stop the traitors heading west?

Crack.

Just then, my clenched fist popped. Jeok Cheongang, who had been watching me with a solemn gaze, spoke up.

“Anyone can become a coward when faced with a crisis.”

“I know.”

I added quietly, remembering a past that still lingered like a scar.

“I’ve been one myself.”

“It sounds like you’re saying you’ll never do it again.”

“I promised myself.”

“You must feel it in your bones, but even judging by what we know so far, their strength is beyond anything we imagined. If Xining is surrounded, we’ll be in for a very difficult fight.”

As if agreeing, Bow Saint nodded quietly. Both had reached heights martial artists could scarcely dream of, and yet even they had to consider the possibility of defeat. That was how dire things were.

“I told you before: anyone can become a coward in a crisis.”

Jeok Cheongang fixed his deep gaze on me. His voice was low and steady.

“In a situation like this, not a soul under heaven could blame you for choosing to live and fight another day.”

*Live and fight another day.*

Mujin’s eyes widened as he understood what Jeok Cheongang meant. Bow Saint stayed silent.

And I—

“Probably. No, definitely.”

I met Jeok Cheongang’s gaze and continued,

“Even if I chose to live and fight another day—no, if I ran away—they’d have no right to criticize me.”

“Even so, it wouldn’t matter. If anyone dared to criticize you, I’d personally rip out his tongue. If anyone pointed a finger at you, I’d turn it to ash.”

“I know that too.”

“Then?”

“I’m staying. Here.”

At my calm reply, Jeok Cheongang’s brow furrowed.

“Why?”

“Because if we leave, Qinghai is finished. The countless civilians living in Xining won’t even have time to escape.”

“If we meet our deaths here, it may not just be Qinghai that falls into their hands. It could be the whole world.”

He wasn’t being arrogant. He wasn’t exaggerating.

The Three Saints and Ten Kings were symbols of the Murim world, and its strongest forces.

It was embarrassing to admit, but I, too, had become a symbol of sorts.

And a gap in our forces could lead straight to defeat.

Jeok Cheongang let out a sigh as he looked at me in silence.

“The world has already looked away. The Nine Sects and One Gang, the Five Great Families, the Murim Alliance—they’ve all turned their backs. And you still plan to make such a foolhardy choice?”

That was when I finally parted my tightly closed lips.

“Even so, we have to.”

“What?”

“No. Because everyone has turned away and abandoned us, we have to do it even more.”

Jade is beautiful even as it shatters.

The light it throws off as it breaks into dozens of pieces is more brilliant than ever.

That is what it means to shatter like jade.

That is why it is called jade’s shattering.

It is so brilliant, you forget the word *destruction*.

It would rather break than be defiled.

“Have you ever seen jade covered in filth and dust?”

Jeok Cheongang stared at me, eyes wide. I continued, slowly, but clearly.

“I haven’t. But I know that jade already covered in grime can lose its value, at least for a while.”

Even so, the essence of the jade remained.

Even if it looked like nothing but dirt on the outside, there was still light hidden within.

But seeing filth cover its beautiful surface, no one would reach out to touch it.

Not unless a sudden downpour washed the jade clean.

Not unless someone who remembered what it once looked like found it and carefully wiped it off.

So—

“Better to break than to be defiled.”

“……!”

“……!”

“……!”

I felt the air tremble and let out the breath I’d been holding.

Yes. This was right.

Even if it ended in death, I couldn’t lose that brilliant light I’d had from the beginning.

I had to make everyone remember. I had to make them realize what mattered most—the thing they’d briefly forgotten while hiding behind excuses about the greater good and worrying about what they might lose.

The jade called justice.

And I would do everything in my power to protect it.

I wouldn’t break. I wouldn’t be defiled.

There was still far too much left to do before I could face a final moment of brilliance.

The greatest, strongest wall casting its shadow over the world was still standing.

*The Lord of Heaven.*

Just then, as the meaning of those two words rang through my heart and drew nearer than ever, Jeok Cheongang—head bowed, lost in thought amid the heavy silence—suddenly spoke.

“You asked whether I’d ever seen jade covered in filth and dust?”

He muttered as if speaking to himself, then raised his head.

Though his body had grown young again, a familiar face was reflected in eyes that held the weight of his years.

“Yes. I saw it. I remember it very clearly.”

He looked at me.

The gaze that had been sunk deep in memories of that day, not so long ago, began to shine.

“That was when I realized how brilliant a light the pathetic, weak little brat in front of me was carrying.”

“……!”

“I told you, didn’t I? If anyone dared to criticize you or point a finger at you, I’d personally punish them. But do you know something?”

The furrows between his brows deepened.

With a clear smile on his face, he slowly reached out and rested a hand on my shoulder.

“If you’d made the same choice as them, I never would have forgiven you.”

Bow Saint spoke with a faint smile.

“Unfortunately, that won’t be happening. Your Disciple is far too good for that.”

A laugh escaped me before I knew it.

Yeah. That was probably true.

The Jeok Cheongang I knew had been that sort of person from the start.

First, he’d go find everyone who insulted his one and only Disciple and beat them to a pulp. Then he’d use whatever strength he had left to thrash his idiot Disciple soundly.

“Looks like you’ll have to use that strength somewhere else.”

Jeok Cheongang laughed out loud at that.

“That’s the plan. I’ll squeeze out every last drop of strength I’ve got.”

And before half a day had passed, his words became reality.
```
