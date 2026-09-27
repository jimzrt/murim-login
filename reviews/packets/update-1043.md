<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1043.txt",
      "sha256": "1431008cf0ac30fda1de60805871a5114b36a008320ad78116277664f5fe3629",
      "bytes": 12904
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a4df01264eae50147b7baca09d5a5539c8c0db97c203209f6e4e8985fbc7bc91",
      "bytes": 1755
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91edff1ea0e7f2d1bdf20f77998a86f250b89f1bc3f043cd106289bea1e118b4",
      "bytes": 240895
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5114d70915e6627069b966210c41109afeae52deff42e7dc7547a8ae96d9f2fe",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "47cdf2895e2a0f138af174f82d71a8778321d822f7ede0fa26abb9aa9cb4ec1f",
      "bytes": 549
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a45114ecf3aa0d13129d0e70c0541d4c233391ced26202f8ca2269ff21ce4917",
      "bytes": 1823
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "57402ad95e1027538b2c9dbd0802432877edefe49dd5e3d045a13e976de6458e",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2428a1be963cdb07658d729ee231e58c5da34556fef0a579c1815526a76b5af9",
      "bytes": 280192
    }
  ],
  "estimated_tokens": 9639
}
-->

# Durable State Update — Chapter 1043

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
1 and safe_through 1043. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1043. Profile updates may replace only one
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
  "chapter": 1043,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1043,
    "continuity_sources": [1043],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "Jeok Cheongang is injured but holding off the Blood-Sword Demon Lord while Jin Taekyung targets the mages.",
    "Fire Dragon Armor is severely damaged, stored in Inventory, and unavailable until its automatic repair completes in three days.",
    "The white-robed mages can use varied Magic; repeatedly dispelling their spells causes energy backlash that incapacitates them.",
    "Nineteen of the twenty white-robed mages have fallen; their veiled female leader, the Grand Mage, remains.",
    "The Grand Mage’s wide-area Magic erupts as Jin Taekyung launches an incomplete, life-consuming One Annihilation at her barrier.",
    "The Wind-and-Cloud Sword Lord is badly wounded but refuses to retreat; his two Senior Brothers have secured a way out and urge him to withdraw.",
    "A shock wave disrupts the two Black Ghosts facing the Wind-and-Cloud Sword Lord, and the battlefield sees an enormous sphere of Hell Fire."
  ],
  "continuity_sources": [
    1041,
    1042
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?",
    "How were the former Demonic Cult fiends made into Black Ghosts?",
    "What are the outcomes of Jin Taekyung’s strike, the Grand Mage’s Magic, and the Hell Fire blast?"
  ],
  "safe_through": 1042,
  "temporary_decisions": [
    "Render 대마도사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 은인     | **Benefactor**                               |
| 감숙     | **Gansu**              |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 블링크 | **Blink** | Arch Lich movement spell |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 풍운검군 | 진태경 | martial artist to fellow martial artist | Daoist Friend Jin | respectful and familiar | Thinks of Jin as 진 도우 when recognizing him as a possible turning point in the battle. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1042
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1042
- **Aliases:** None
- **Role:** The Grand Mage leads the white-robed mages and is a formidable mage who has reached the edge of truth.
- **Personality:** She remains composed while taunting Jin and appears pleased and excited to meet him.
- **Voice:** Calm and politely phrased, with teasing remarks and a hint of excitement.
- **Relationships:** She commands the white-robed mages and is an adversary of Jin Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1042
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1042
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1043화



한순간, 전장의 모두가 넋 나간 눈빛으로 하늘을 바라보았다.

단 한 사람의 예외조차 없었다.

그야말로 천운(天運)이라 할 수 있는 상황 덕분에 두 마리의 흑귀를 쓰러트린 풍운검군도.

어째서인지 착잡한 표정이 되어, 모든 힘을 소진하고 비틀거리는 사제를 부축하기 위해 달려가던 못난 사형들도.

피로 뒤덮인 눈밭에서 각자의 싸움을 이어 가던 종남파의 제자들과 감숙 무림 연합군도.

아들이 사라진 그 자리에 망부석처럼 서 있던 어느 한 아버지와 이미 저 멀리 앞서나간 친구이자 상관을 쫓아 혼신의 힘을 다해 나아가고 있던 화룡각 대원들도.

심지어는 텅 빈 눈동자로 맹목적인 전투만을 이어 가던 암천의 교도들도.

살아있다 말할 수 있는 모든 존재가 ‘그것’을 바라보았다.

지금껏 본 적도, 들은 적도 없는 거대한 불의 구를.

구구구구궁.

태곳적 거인이 고함을 내지른다면 이런 소리가 나는 것일까.

낡은 경전 속에 기록된 지옥의 유황불이 존재한다면, 바로 이런 것일까.

귓가가 먹먹해지는 굉음이 모두의 머리 위로 쏟아져 내린다.

아득한 높이에서 유성처럼 떨어지는 그것을 따라, 끔찍한 열기가 하늘을 달구고 있었다.

“아, 아아…….”

곳곳에서 흘러나오는 신음들.

모두가 그 자리에서 얼어붙었고, 그것만이 그들이 할 수 있는 전부였다.

직접 자신들의 두 눈으로 보고 있음에도 믿을 수 없는, 불가해(不可解)의 영역.

아니, 재앙.

그렇기에 그 누구도 저것의 정확한 명칭을 알지 못했다.

필사적으로 재앙을 막으려 했던, 그러나 끝끝내 막지 못한 한 사람을 제외하고는.

‘헬 파이어(Hell Fire)……!’

마치 멈춘 듯한 세상 속에서, 진태경은 입술 사이를 비집고 흘러나오려는 비명을 씹어 삼켰다.

명칭 그대로, 지옥의 겁화.

인간이 발휘할 수 있는 가장 강력한 광범위 마법 중 하나이자, 단 한 번의 발동으로 능히 수천의 목숨을 앗아갈 수도 있는 재앙 그 자체.

‘안 돼.’

누구보다 저것의 위력을 잘 알고 있었기에 막고자 했다.

설령 그 과정에서 목숨을 잃게 된다 하더라도 상관없었다.

그 대가로 누군가를 쓰러트릴 수 있다면, 그렇게 해서라도 재앙을 막을 수 있다면 괜찮은 최후라고 자위할 수 있을 테니까.

하지만 결국 막지 못했다.

지금 이 순간 진태경이 할 수 있는 것은, 전신을 옥죄는 탈력감을 느끼며 그저 멍하니 재앙의 발현을 지켜보는 것뿐이었다.

‘지금이라도…… 지금이라도 무슨 수를 써야 하는데.’

간절한 마음과는 달리 흔들리는 시야.

그뿐만이 아니다.

마치 거인의 손에 쥐어 짜지는 것처럼 온몸의 뼈마디와 근육이 고통을 호소하고, 이미 텅 비어 버린 단전에는 한 줌의 공력조차 찾아볼 수 없었다.

미완성인 채로 쏘아졌던 일섬(一殲).

그것은 불행인 동시에 행운이었다.

미완성이었기에 모든 방어막을 부수지 못했고, 그랬기에 진태경이 살아남을 수 있었으니.

그러나 모든 것을 각오했던 누군가에게는, 이것이 곧 불행이었다.

‘제기랄.’

시시각각 전신 깊숙한 곳을 헤집는 그 끔찍한 여파에 진태경은 자신도 모르게 몸을 떨었다.

그러나 포기할 수 없었다. 이대로 모든 것을 포기하기 싫었다.

콰득.

이를 악물고, 경련이 일어나는 팔다리를 움직였다.

그는 자꾸만 손아귀에서 미끄러지려는 창대를 힘주어 움켜잡고, 그것을 지팡이 삼아 휘청이는 몸을 일으켜 세웠다.

- 피해! 모두 피해라!

- 으아, 으아아아아!

어두웠던 하늘을 붉게 물들이며 떨어져 내리는 재앙을 비로소 현실로 인지한 사람들의 비명을 들으며.

언덕 아래에 펼쳐진 전장을 뒤덮은 극심한 혼란과 공포, 그리고 이런 상황과는 어울리지 않는 평온한 목소리 역시도 함께.

“그냥 누워 계시는 거 어때요? 더 무리하면 그때는 정말 힘들어질 텐데.”

담담하기 그지없는 대마도사의 음성에, 한껏 악물린 진태경의 입가에서 핏줄기가 흘러내렸다.

“아가리 닥쳐. 썅년아.”

“말이 심하네요. 그래도 따지고 보면 내가 생명의 은인일 텐데.”

팟.

마치 순간 이동하듯, 아니 순간 이동 그 자체인 블링크(Blink)로 불현듯 다가온 대마도사가 일장도 안 되는 거리에서 멈춰 섰다.

정확히는 여전히 진태경과 자신 사이에 놓여 있는, 보이지 않은 마법의 방어막 앞에서.

“솔직히, 조금 전에는 정말 놀랐어요. 순간적으로 모골이 송연해졌다니까?”

스륵.

핏줄이 고스란히 비칠 만큼 얇고 투명한 손가락이 부드럽게 방어막을 훑었다.

다른 누구도 아닌 대마도사가 직접 수십 번에 걸쳐 중첩시킨 강력한 방어막은 이제 단 한 겹만이 남아 아슬아슬하게 형태를 유지 중이었지만, 그녀는 조금도 긴장한 기색을 보이지 않았다.

지금의 진태경은, 공격은커녕 스스로의 힘으로 일어서는 것조차 버거운 상황이라는 것을 알고 있었으니까.

“노파심에 하는 말인데, 괜히 헛수고하지 말아요. 당신도 알고 있지 않나요? 지금 날 죽여 봤자 이미 벌어진 일은 막을 수 없다는 걸.”

“그래, 알지.”

진태경은 숨을 헐떡이며 대답했다.

그러나 음성과는 달리 그의 시선은 대마도사를 향하고 있지 않았다.

진태경은 그 거대한 크기만큼이나 느릿한 속도로, 검게 물든 하늘을 가로지르는 지옥의 겁화를 응시하며 말을 이었다.

“네년이, 너희가 절대 날 죽일 수 없다는 것도.”

누구보다 그 사실을 잘 알기에, 진태경은 망설임 없이 돌아서서 백염을 역수(逆手)로 쥐었다.

그가 목숨까지 걸어 가며 싸웠던 이유는, 단순히 대마도사를 죽이기 위해서가 아니었으니까.

한 사람의 강적보다 한 명의 아군을, 수만 명이나 되는 목숨들을 지키기 위해서였으니까.

‘제발 한 번. 마지막으로 단 한 번이라도.’

간절한 염원을 담아, 진태경은 전신에 남아 있는 실낱같은 기운을 모조리 쥐어 짜냈다.

금방이라도 부서질 것 같은 자신의 몸뚱어리를 활로 삼아, 백염이라는 화살을 시위에 걸었다.

뿌드득.

눈앞을 아득하게 물들이는 끔찍한 격통.

이미 나약해질 대로 나약해진 몸이 비명을 내지른다.

앞서 감당할 수 없는 과도한 힘의 방출로 망가진 혈도는 한 줌밖에 안 되는 열양지기에도 타들어 간다.

까드득.

하지만 범인이라면 상상조차 할 수 없을 그 고통을, 진태경은 이를 악물며 견뎌 냈다.

금이 가다 못해 이제는 부서져 버린 어금니와 입안에 고인 핏물을 함께 삼켜 내며.

지금 이 순간에도 지상에 성큼 가까워지는 불덩어리를 향해 창날을 겨누었다.

더는 강기(罡氣)라 부를 수 없는, 아지랑이처럼 희미하고 은은한 기운만이 맺혀있는 그것을.

“참 미련하네요. 당신이란 사람은.”

대마도사의 입술 사이로 한숨 섞인 목소리가 흘러나왔으나, 진태경의 귀에는 들리지 않았다.

그저 모든 감각과 힘을 집중한 채, 그는 자신에게 주어진 마지막 기회를 부여잡고 있을 뿐이었다.

‘할 수 있을까. 내가.’

문득 뇌리에 떠오른 의문.

그러나 진태경은 이미 이 의문에 대한 답을 알고 있었다.

아니, 지금 이 상황을 보았다면 그 누구라 할지라도 같은 답을 내놓았을 것이다.

할 수 없다고.

단지 허황된 꿈에 불과하다고.

이건 그저, 마지막까지 포기하지 않고 최선을 다하고 싶었던 한 사람의 발악이자 염원에 지나지 않는다고.

하지만…….

‘이런 허황된 꿈이라도 꾸지 못했다면, 지금 여기까지 오지도 못했어.’

어느 한 청년에게 있어, 인생이란 긴 꿈이었다.

비록 잔인한 현실에 분노하고, 순응하고, 잠시나마 절망한 적도 있었으나 청년은 여전히 꿈을 꾸고 있었다.

그리고 어느 날, 꿈은 현실이 되었다.

생각지도 못한 새로운 목표와 갈망을, 강한 힘과 그보다 무거운 책임을 청년은 그 꿈속에서 깨달았다.

그것이 단 하나의 이유였다.

타오르는 불꽃을 향해 달려드는 부나방과 같다 해도, 이글거리는 태양의 열기에 파묻혀 사라질 반딧불이라 할지라도 결코 포기할 수 없는 이유.

저벅. 그그극.

어느덧 떨림이 멎은 다리가 철탑처럼 지면을 밟는다.

동시에 뒤로 한껏 젖혀진 어깨가, 아득한 허공을 향해 겨누어진 창날이 다음 순간 힘차게 나아가는 발걸음과 함께 쏘아졌다.

‘가라.’

퍼엉!

한 사람이 지니고 있던 모든 힘이 실린 응축과 폭발.

동시에 폭발하듯 터져 나가는 압축된 공기.

슈화아악!

백염의 창날이 바람을 찢었다. 공간을 갈랐다.

불길한 어둠으로 물든 하늘을 가로지른 한 줄기의 섬광이, 그와는 비교도 할 수 없는 크기와 힘을 지닌 구체를 향해 쏘아졌다.

그리고 자그마치 일백여 장에 달하는 공간을 좁히며, 하나의 점이 되어 버린 그것을 진태경은 흐릿해져 가는 눈동자로 바라보고 있었다.

아직 창날은 목표에 닿지 않았다.

그러나 보지 않아도 알 수 있는 것이 있다.

바로 지금처럼.

‘틀렸어.’

진태경의 마음속에서 공허한 뇌까림이 울려 퍼졌다.

실패다.

대마도사가 준비해 둔 헬 파이어를 저지하기에는 힘도, 속도도, 공력도 터무니없이 부족했다.

단지…… 단지 그뿐이었다.

모든 것을 쏟아부은 지금, 이제 진태경에게 남은 것은 없었다.

만약 남은 것이 있다면, 그것은 더욱 무겁게 몸뚱어리를 짓누르는 피로감과 그보다 더한 무력감.

그리고 이 모든 것을 그에게 안겨 준 적의 비웃음뿐이었다.

“저런, 너무 낙심하지는 마요. 그래도 옆에서 지켜본 입장에서는 아주 인상적인 시도였으니까.”

대마도사는 동정과 웃음이 뒤섞인 말과 함께, 미약하기 그지없는 기운이 실린 창날이 마침내 자신이 펼친 마법과 맞닿는 것을 지켜보았다.

그리고 동시에, 똑똑히 들었다.

바로 그 순간 온 사방에 울려 퍼진, 하늘이 쪼개지는 듯한 굉음을.

콰아아아앙!

“……!”

“……!”

진태경과 대마도사는 누가 먼저랄 것도 없이 눈을 부릅떴다.

구구구구궁!

헬 파이어.

그 끔찍한 지옥의 겁화가, 거대한 불덩어리가 뒤흔들리고 있었다.

“이게 무슨……!”

대마도사는 경악했다.

어린아이와 초절정 고수 간의 생사결만큼이나 당연하게 정해져 있던 결과.

그만큼 진태경은 지쳐 있었고, 백염의 창날에 실려 있던 힘은 미약하기 짝이 없었다.

그렇기에 제지조차 하지 않고 지켜만 보았다.

처음부터 안 될 것을 알았으니까.

그녀가 보기에는 그저 허황된 꿈에 불과했으니까.

하지만 그 한 자루의 창이, 수백 배나 거대한 불덩어리의 방향을 뒤바꾸었다.

이글거리는 불길의 일부를 꺾고, 균열을 일으켰다.

“어떻게…… 도대체 어떻게 이런 일이 가능하지?”

그리고 도무지 이해할 수 없는 이 현실 속에서, 불현듯 고개를 돌린 대마도사는 마침내 볼 수 있었다.

휘청이는 몸을 억지로 부여잡은 채, 그 믿을 수 없는 광경을 지켜보고 있는 진태경의 모습을.

그의 입가에 맺힌 흐릿한 미소와 핏물로 말라붙은 입술이 달싹이는 것을.

“그래, 포기하기 싫은 건 누구나 똑같지.”

힘겹게 흘러나오는 목소리가, 그녀의 고막에 선명하게 틀어박혔다.

“나도, 저들도.”

“……!”

짧은 한마디.

그러나 무언가를 느낀 대마도사는 벼락처럼 고개를 돌렸고, 동시에 앞서 자신이 품은 의문에 대한 답을 찾을 수 있었다.

쐐애애액, 콰아앙!

지상에서 솟구쳐 올라, 모두의 머리 위를 덮은 불덩어리를 향해 퍼부어지는 휘황한 섬광들.

어느 청년과 같은 꿈을 꾸는 자들이, 그곳에 있었다.
```

## Final English reading copy

```markdown
# Chapter 1043

For one instant, everyone on the battlefield stared at the sky, their eyes vacant.

Not a single person was an exception.

Not even the Wind-and-Cloud Sword Lord, who had brought down two Black Ghosts thanks to what could only be called a stroke of heaven-sent luck.

Not even his two pathetic Senior Brothers, who had somehow gone somber and were now rushing to support their Junior Brother as he staggered, utterly spent.

Not even the Disciples of the Zhongnan Sect and the Gansu Murim Alliance, still fighting their separate battles on the blood-soaked snow.

Not even a father standing like a stone monument where his son had disappeared, or the Fire Dragon Pavilion members pouring every last bit of strength into chasing after their friend and leader, who had already raced far ahead.

Not even the Dark Heaven cultists, whose eyes were empty as they continued their mindless fighting.

Every living being looked at *it*.

A vast sphere of fire, unlike anything they had ever seen or heard of.

Grrrrrrr-BOOM.

Would this be the sound of an ancient giant roaring?

If the hellish brimstone fires recorded in old scriptures really existed, would they look like this?

A deafening roar that left their ears ringing poured down over everyone’s heads.

Following the thing as it fell from dizzying heights like a meteor, an unbearable heat scorched the sky.

“A-aah…”

Groans rose from here and there.

Everyone froze where they stood. It was all they could do.

They were seeing it with their own eyes, and still couldn’t believe it. Something beyond comprehension.

No—a calamity.

That was why no one knew its exact name.

No one except the one person who had desperately tried to stop the calamity, but failed in the end.

*Hell Fire…!*

In a world that seemed frozen in time, Jin Taekyung bit back the scream rising between his lips.

Hellfire, just as its name suggested.

One of the most powerful wide-area spells a human could wield—and a calamity in its own right, capable of taking thousands of lives with a single cast.

*No.*

He knew its power better than anyone, and that was why he’d tried to stop it.

He hadn’t cared if he lost his life in the process.

If he could bring someone down in exchange—if he could stop the calamity—that would have been a decent end. He could have told himself as much.

But in the end, he hadn’t stopped it.

Right now, all Jin Taekyung could do was feel the weakness constricting his entire body and stare blankly as the calamity unfolded.

*Even now… I have to do something. Somehow.*

His vision wavered, no matter how desperately he wished otherwise.

And that wasn’t all.

Every bone and muscle in his body screamed in pain, as if squeezed in a giant’s fist. His dantian was already empty; he couldn’t find even a trace of internal energy.

The One Annihilation he’d launched while it was still incomplete.

That had been both misfortune and good luck.

Because it was incomplete, it hadn’t shattered every defensive barrier. And because of that, Jin Taekyung had survived.

But for someone who had been prepared to give up everything, this was misfortune.

*Shit.*

The horrible aftereffects tore deeper and deeper through his body. Jin Taekyung shuddered without meaning to.

But he couldn’t give up. He didn’t want to give up everything here.

Crack.

He clenched his teeth and moved his twitching arms and legs.

Gripping the spear shaft before it could slip from his grasp, he used it as a cane and hauled his unsteady body upright.

“—Run! Everyone, run!”

“Aaah! Aaaaaah!”

He heard the screams of those who finally understood that the calamity falling from the sky, painting it red, was real.

He heard, too, the terrible confusion and fear covering the battlefield below the hill—and, somehow out of place amid it all, a calm voice.

“Why don’t you just lie down? If you push yourself any harder, you really will be in trouble.”

At the Grand Mage’s utterly composed voice, blood trickled from between Jin Taekyung’s clenched lips.

“Shut your damn mouth, you bitch.”

“That’s a little harsh. When you think about it, I’m the one who saved your life.”

Pop.

She appeared beside him as if she’d teleported—or, rather, she’d used Blink, which was teleportation itself—and stopped less than a *jang* away.

More precisely, she stopped before the invisible magic barrier still standing between them.

“Honestly, you really surprised me just now. It gave me goose bumps.”

Her fingers, so thin and translucent that every vein showed through, gently traced the barrier.

The powerful barrier she’d personally layered dozens of times was down to a single layer, barely holding its shape. But she showed no sign of tension.

She knew Jin Taekyung could barely get to his feet under his own power, let alone attack.

“I’m only saying this out of concern, but don’t waste your effort. You know, don’t you? Killing me now won’t undo what’s already happened.”

“Yeah. I know.”

Jin Taekyung answered between ragged breaths.

But unlike his voice, his eyes weren’t on the Grand Mage.

He watched the hellfire as it crossed the blackened sky, as slow as its enormous size, and continued,

“I also know you—and the rest of your lot—can never kill me.”

Because he knew that better than anyone, Jin Taekyung turned without hesitation and gripped White Flame in a reverse hold.

He hadn’t risked his life just to kill the Grand Mage.

He’d fought to protect one ally rather than bring down one formidable enemy—to protect tens of thousands of lives.

*Please. Just once. One last time.*

With a desperate prayer, Jin Taekyung wrung every last thread of energy from his body.

He made his body, ready to break at any moment, into a bow and set White Flame, his spear, against its string.

Crrrk.

Excruciating pain filled his vision.

His already-weakened body screamed.

The acupoints damaged earlier by the excessive release of power burned even under the tiny amount of Scorching Yang Qi he could muster.

Grind.

But Jin Taekyung clenched his teeth and endured pain no ordinary person could even imagine.

He swallowed the blood pooled in his mouth along with the molar that had cracked and finally broken apart.

Even now, the blazing sphere was drawing closer to the ground. He aimed his spearhead at it.

A faint, delicate energy clung to the spearhead, like a heat haze. It could no longer be called Force.

“You really are a fool.”

The Grand Mage’s voice came with a sigh, but Jin Taekyung didn’t hear it.

He focused every sense and every ounce of strength on seizing his last chance.

*Can I do this? Can I?*

The question surfaced in his mind.

But Jin Taekyung already knew the answer.

No—or rather, anyone who saw this situation would give the same answer.

He couldn’t.

It was nothing but a foolish dream.

Nothing more than the desperation and hope of a man who wanted to do his best, right up to the end.

But…

*If I couldn’t even dream a foolish dream like this, I never would’ve made it this far.*

For one young man, life had been a long dream.

He’d been enraged by cruel reality, resigned to it, and, for a time, despaired. But the young man had kept dreaming.

Then, one day, the dream became reality.

In that dream, he discovered an unexpected new goal and longing, great power—and an even heavier responsibility.

That was the one reason.

The reason he could never give up, even if he was a moth flying toward a blazing flame, even if he was a firefly destined to vanish beneath the heat of the burning sun.

Step. Scrape.

His trembling legs finally steadied and planted themselves in the ground like iron pillars.

At the same time, his shoulder drew back. The spearhead aimed at the distant sky shot forward with his next powerful step.

*Go.*

Whoom!

Every bit of a person’s strength condensed, then burst forth.

At the same time, compressed air exploded outward.

Shwoooosh!

White Flame’s spearhead tore through the wind. It split open space.

A streak of light crossed the sky, dyed in ominous darkness, and shot toward a sphere whose size and power dwarfed it.

It covered more than a hundred *jang* of distance, shrinking until it became a single point. Jin Taekyung watched it with eyes growing dim.

The spearhead hadn’t reached its target yet.

But some things could be known without seeing them.

Like this.

*It’s no use.*

An empty murmur echoed in Jin Taekyung’s heart.

Failure.

He was nowhere near strong enough, fast enough, or possessed of enough internal energy to stop the Hell Fire the Grand Mage had prepared.

That was all. That was all there was to it.

Now that he’d poured out everything, Jin Taekyung had nothing left.

If anything remained, it was exhaustion weighing even more heavily on his body, and a helplessness greater than that.

And the enemy’s sneer—the one who’d brought all of this upon him.

“Oh, don’t be too disappointed. From where I was standing, it was a very impressive attempt.”

The Grand Mage spoke with a mix of sympathy and amusement as she watched the spearhead, carrying the faintest trace of energy, finally touch the Magic she’d cast.

And at the same time, she heard it clearly.

The deafening boom that rang out all around them, as if the sky had split apart.

KWA-BOOOOM!

“……!”

“……!”

Jin Taekyung and the Grand Mage both stared wide-eyed.

Grrrrrrr-BOOM!

Hell Fire.

The horrifying hellfire, the enormous sphere of flame, was shaking.

“What is this…!”

The Grand Mage was astonished.

The outcome had seemed as certain as a life-and-death duel between a child and a Supreme Peak master.

Jin Taekyung was exhausted, and the force behind White Flame’s spearhead had been pitifully weak.

That was why she’d simply watched without even trying to stop him.

She’d known from the start that he couldn’t do it.

To her, it was nothing more than a foolish dream.

And yet that single spear had changed the course of a sphere of fire hundreds of times its size.

It had bent part of the blazing flames and opened a rift in them.

“How…? How could this possibly happen?”

And in the midst of a reality she couldn’t begin to understand, the Grand Mage suddenly turned her head.

At last, she saw Jin Taekyung, forcing his unsteady body to hold together as he watched the unbelievable scene.

She saw the faint smile on his lips, and those lips, caked with dried blood, moving.

“Yeah. Nobody wants to give up.”

His voice came out with difficulty, but it rang clearly in her ears.

“Me, too. And them.”

“……!”

A brief remark.

But the Grand Mage felt something and whipped her head around. At the same time, she found the answer to the question she’d asked herself moments earlier.

Shwoooosh—KWA-BOOM!

Dazzling streaks of light shot up from the ground and rained down on the sphere of fire covering everyone’s heads.

The people who shared the same dream as that young man were there.
```
