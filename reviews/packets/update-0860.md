<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0860.txt",
      "sha256": "4225f71c64f07b6f276569ccfd8266070149d80db95e42b75664fafcffd4633d",
      "bytes": 12866
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "54a1f5663cdbed9363696f82be74a28953d58e4c3398e5dcc06106dee37e6ed7",
      "bytes": 1939
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "947c5eb2a7110dbc90a975ccef0d718fc7dc499072ca47629f32e25ce8a382b7",
      "bytes": 228766
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "da24fc7760ea46993e2e0fdf1bfbde88171650eaa3c6733591537250f2270f58",
      "bytes": 797
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "95f53fb25a5f08c017659304beeef843ad4e0f4fda1b52180ebc54f6cf2c3137",
      "bytes": 1378
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "1c17c8195c49893290518b927d8629cf7b7a8a47f8bcd31a7149f5457ef14c59",
      "bytes": 1511
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "0d97c57070a38239823f7a72f4119f8ca796f4f8c9c352b45b8387d4cdf7671c",
      "bytes": 627
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "e34d5c86b9db7ca651fe874fdeb73b331855a28f7a91620fb3700e574158261e",
      "bytes": 699
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "175c4e0879b6eb8973116cd4cecc2f6950bd51e0f1c24ea332c5334e3bd45863",
      "bytes": 883
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1cc6bec51ffc7efad4fa98cc9a6565bf8465c71db4e90ecbc3058e014545b38d",
      "bytes": 254192
    }
  ],
  "estimated_tokens": 10905
}
-->

# Durable State Update — Chapter 860

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
1 and safe_through 860. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 860. Profile updates may replace only one
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
  "chapter": 860,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 860,
    "continuity_sources": [860],
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
    "The Divine Physician secured the Blood Soul Gu from the deceased City Lord of Sichuan Province. It weakens hosts, causes madness, and eventually kills them.",
    "Jin suspects Dark Heaven killed the City Lord as part of a scheme against the Great Nation, possibly its imperial family.",
    "Prince Shangshan Zhu Bao is traveling to the imperial capital with Hong Jin, the Embroidered Uniform Guard, and Jin’s party. The late Emperor entrusted Hong Jin with Zhu Bao’s care, and Zhu Bao trusts his elder brother. Jin fears the Emperor may turn the Imperial Guards against them.",
    "Jeong Hogun leads the Embroidered Uniform Guard escorting Zhu Bao discreetly. As predicted, uninvited guests interfered; Jeong sent a subordinate to report this to the Guard’s Commander-in-Chief.",
    "Zhu Bao gave Hyuk Mujin the joking title “Tenfold Man,” which Mujin inscribed on a bronze token."
  ],
  "continuity_sources": [
    858,
    859
  ],
  "open_questions": [
    "Why did Dark Heaven secretly kill the City Lord, and is it targeting the Emperor or imperial family?",
    "What does the Emperor intend for Prince Shangshan, and what prompted the imperial decree against Hong Jin?",
    "What does Zhu Bao’s secret letter to Jin contain?",
    "Who predicted that uninvited guests would interfere, and what do the Commander-in-Chief or Emperor know about the party?",
    "Who trained the Embroidered Uniform Guard’s highly skilled martial artists, and for what purpose?"
  ],
  "safe_through": 859,
  "temporary_decisions": [
    "Render 혈혼고 as “Blood Soul Gu”; 대국 as “Great Nation.”",
    "Render 금의위 as “Embroidered Uniform Guard”; 금위군 as “Imperial Guards.”",
    "Render 강소 as “Jiangsu.”",
    "Render 정호군 as “Jeong Hogun”; 정 천호 as “Commander Jeong.”",
    "Render 십상남자 as “Tenfold Man.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 하오문    | **Lower District Sect**          |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남궁세가   | **Nangong Family**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 정파     | **orthodox faction**                             |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 안휘     | **Anhui**              |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 태권도 | **Taekwondo** | Martial art Taekyung practiced as a child. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 심력 | **mental strength** | Inner mental capacity injured by Jongni Chu's feint. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 강서 | **Jiangxi** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 강소 | **Jiangsu** | Province at the eastern end of the Yangtze route. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 복건 | **Fujian** | Region referenced in the title First Beauty of Fujian. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 주표 | 혁무진 | prince_to_subordinate_of_his_companion | Tenfold Man Hyuk Mujin | formal and playful | Zhu Bao takes Mujin’s boast literally and grants him the title. |

## Listed compact profiles

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 859
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch who served the late Emperor and has been entrusted with Prince Shangshan’s protection since the prince’s infancy.
- **Personality:** Composed and socially deft, Hong Jin is considerate toward those beneath him and dislikes excessive deference, which recalls his impoverished past.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and trusts Jin Taekyung as the person best able to keep the prince safe.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 859
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 858
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 859
- **Aliases:** None
- **Role:** Jeong Hogun is a commander of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he presents loyalty to the Emperor's command as the foundation of his force's actions.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Commands the Embroidered Uniform Guard force confronting Jin Taekyung and serves the Emperor's command.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 859
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 859
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, compassionate, and eager to emulate Jin Taekyung; he takes responsibility for his loyal subjects’ hardship, though his trust in his elder brother shows his youth.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃860화



무림인은 마치 잡초 같은 존재다.

어두운 뒷골목에도, 환한 대로변에도 있고 첩첩산중과 드넓은 장강 어딘가에서조차 끈질기게 살아간다.

아마도 그렇기에 그들이 사는 세상이 무림(武林)이라 불리게 되었을 것이다.

보편적인 상식과 법을 무시하는 무뢰한들.

그러나 날카롭게 벼려 낸 창칼로 자신들만의 숲을 일군 무림인들이라 할지라도, 그들 모두가 거목(巨木)으로 성장할 수 있는 것은 아니었다.

무림이라는 이 거대한 숲에서 거목이라 불릴 만한 것은 구파일방과 오대세가. 그리고 아직 그에는 미치지 못하지만 한 성의 패자(霸者)로 자리매김한 몇몇 세력뿐이었으니까.

‘태원진가도 그중 하나고.’

나는 내심 중얼거리며 창밖을 바라보았다.

한창 호객 행위 중인 상인. 땀을 뻘뻘 흘리며 한 지게 가득 장작을 메고 지나가는 나무꾼. 평범해 보이는 양민들과 비단옷을 차려입은 높으신 분들까지.

하나의 사회를 이루는 수많은 인간군상이 그곳에 있었지만, 지금껏 어디에서나 보였던 특정 부류의 사람들은 좀처럼 보이지 않았다.

“못 찾겠죠?”

“네?”

“무림인들 말이야. 진 공자와 같은.”

내 생각을 정확히 읽어 낸 홍진이 하얗게 분을 칠한 얼굴로 웃어 보였다.

“괜히 심력 낭비할까 봐 미리 말해 두는데, 강소성에서는 찾기 힘들 거예요. 여긴 그런 곳이니까.”

“얼추 얘기를 듣긴 했습니다만…… 역시 황도(皇都)와 가까워서 그런 겁니까?”

“아무래도 영향이 없진 않겠죠. 천자께서 기거하시는 황도 인근에 그런 무뢰배들이 설치게 놔둘 수는 없으니까.”

홍진이 나와 혁무진을 바라보며 덧붙였다.

“오해할까 봐 말하자면, 이건 어디까지나 높으신 분들 생각이에요. 위로 갈수록 체면을 중요시하거든.”

혹여나 내 기분이 상할까 봐 립서비스 차원에서 던진 느낌이긴 한데, 굳이 그러지 않아도 어느 정도는 이해가 간다.

뭐, 엄밀히 따지자면 무림인 중에 막 나가는 놈들이 한둘도 아니고.

하지만 황도와 가깝다는 이유만으로 그 모든 것이 설명되는 것은 아니다.

다음 순간 혁무진이 불쑥 던진 질문도 같은 맥락이었다.

“그럼 안휘(安徽)에 버젓이 자리 잡은 남궁세가는 뭡니까? 거리 자체도 황도와 그리 멀리 떨어져 있지 않은데.”

“그 질문에 대답하기 전에, 어디 한 번 반대로 물어볼까? 황도와 인접한 지역 중 안휘의 남궁세가를 제외하면 뭐가 남는지?”

“남궁세가를 제외하면. 그게 그러니까…….”

쉽게 말을 잇지 못하는 혁무진의 모습에, 홍진이 작게 실소를 흘렸다.

“없어요. 강서. 복건. 강소. 안휘. 황도가 위치한 절강성을 둘러싼 네 개의 성 중에 이름있는 무림 문파는 남궁세가 하나뿐이야. 물론 예외인 곳도 있긴 하지만.”

“예외요?”

“응. 뭐랄까. 역사만 따져 보면 굉장히 위험할 것 같긴 한데, 그렇다고 해서 굳이 황실이 나서서 건드리기에는 찜찜한 그런 문파. 혁 무인은 몰라요?”

미간을 찌푸리며 생각에 잠겨 있던 혁무진이 대답했다.

“자세히 찾아보면 문파 몇 개쯤은 나오겠지만, 그런 문파가 있습니까? 어차피 안휘의 남궁세가에 비교하면 말 불알보다 못한 수준일 텐데.”

“혁 무인, 나는 불알이 없어요.”

“아앗, 죄송합니다.”

“아냐. 그렇게까지 사과할 필요는 없어. 그냥 듣다 보니까 기분이 이상해서 그래. 아무튼 정말 없다는 거죠?”

“예. 물론입니다.”

그 순간, 나는 자신감 있게 대답한 혁무진의 뒤통수를 후려쳤다.

빡!

“열화문! 개새끼야. 열화문!”

“억! 어억!”

“안휘성 구화산! 장장 삼백 년 역사! 열화문이 말 불알보다 못하냐? 열화문이 좆밥으로 보여!”

이래 봬도 열화문 입사 이 년 차이자 착실히 후계자 과정을 밟고 있는 몸.

내가 불타오르는 애사심을 원료 삼아 혁무진을 두들겨 패던 그때, 홍진이 나직하게 입을 열었다.

“저기 진 공자, 미안한데…….”

“아, 미안합니다. 그것도 없으셨죠.”

“아니, 그게 아니고. 전하께서 잠에서 깨실까 봐. 그리고 환관이라고 해서 둘 다 없는 건 아니에요. 이건 일전에도 한번 말했던 것 같은데.”

“다시 한번 죄송합니다. 하나만 없으신 걸 깜빡했어요.”

“……그래요. 좀 주의해 줘요. 전하 안 깨시게 목소리도 낮추고.”

반쯤 포기한 표정으로 대답한 홍진은 새근새근 잠든 상산왕 주표를 바라보며 말을 이었다.

“여하튼 절강성뿐만 아니라 황도와 인접한 성에는 무림인들이 크게 기승을 떨치지 못했어요. 흔히들 말하는 사마외도는 물론이고, 정파의 거목이자 오대세가의 일원인 바로 그 남궁세가도 고관대작(高官大爵)들과의 연줄을 총동원해야 했죠.”

“그 정도였습니까?”

“네. 건국 직후의 일이니 이미 오래전의 이야기지만, 지금까지 쭉 이어지고 있는 상황이기도 해요. 뭐, 제아무리 거친 무림인들이라 해도 모산파(茅山派)의 전철을 밟고 싶지는 않았겠죠.”

“모산파?”

제법 익숙한 이름이다.

학창 시절 즐겨 봤던 여러 무협 소설에 종종 등장하고는 했던 문파.

어느 무협에서도 매번 등장하는 구파일방 같은 메이저는 아니고, 마이너에 가까웠던 이미지였지만 그에 관한 기억을 떠올리는 것은 그리 어려운 일이 아니었다.

그나저나…….

“혹시 그 모산파 말씀하시는 겁니까? 무공보다 술법으로 유명하다는?”

“응? 몰랐어요? 바로 여기 강소성에 있었는데.”

내가 뭐 화왕처럼 백 년을 넘게 살아온 전대의 노고수도 아니고, 지금의 대국이 막 들어설 당시의 일까지 어떻게 일일이 꿰고 있겠나.

다만 조금 전 들었던 말에서 위화감을 느끼기에는 충분했다.

‘강소성에 있었다, 라…….’

현재형이 아니라 과거형이다.

거기에 더해 앞서 홍진이 전철이라는 단어를 운운했던 것과 지금까지 무림에서 활동하며 모산파라는 이름을 듣지 못했다는 사실을 새삼 떠올리자 하나의 결론이 나왔다.

“사라졌군요. 이미 오래전에.”

“정답.”

경쾌하게 손가락을 튕긴 홍진이 입을 열었다.

“당시 대국을 건국하신 태조(太祖)께서는 이곳을 도읍으로 정하셨어요. 과거 여섯 개의 왕조가 자리 잡았던 강소성의 남경(南京)이 바로 황실의 첫 보금자리였죠.”

“그래서 어떻게 됐습니까?”

“새로운 통일 왕조가 들어설 마당에, 감히 강호의 무뢰배들을 설치게 둘 수 있었을까? 황명이 떨어지자 모든 것이 일사천리였죠. 그때 강소성의 문파 대부분이 터전을 옮겼어요. 이쯤 되니까 슬슬 감이 잡히죠?”

모든 문파가 아니라, 대부분의 문파가 터전을 옮겼다고 했다.

뒷말을 짐작한 나는 나직이 뇌까렸다.

“모산파는 아니었군요.”

“맞아요. 모산파를 비롯한 소수의 무림 문파는 강소성을 떠나라는 황명을 거부하고 본거지를 지켰어요. 그 당시만 하더라도 구파일방에 비견될 만큼 커다란 규모였다고 했으니, 어느 정도 고집을 피운 거죠. 하지만…….”

흙바닥에서 태어나 새로운 하늘을 열어젖힌, 대국의 첫 황제는 모산파가 생각했던 것만큼 너그러운 사람이 아니었다.

“남아 있는 기록에 의하면 십만의 금위군이 출병(出兵)했어요. 풀 한 포기, 개미 새끼 한 마리 남기지 않고 모조리 죽이고 불태운 거지.”

“……!”

“……!”

“모산파는 그렇게 멸문당했고, 그 후로 강소성에는 어떤 무림 문파도 자리 잡지 못했어요. 작금의 천자께서 절강성으로 천도(遷都)하신 이후에도 쭉.”

강소성은 단순히 옛 황도가 아니었다.

이미 금위군이 한바탕 청소를 끝낸 무림인 청정 구역이자, 초대 황제의 흔적이 진하게 남아 있는 황실의 앞마당이었던 셈이다.

그리고 이 사실이 뜻하는 바는 실로 명확했다.

‘도움을 청하긴 글렀군.’

지금까지는 어디에서나 도움을 받을 수 있었다. 지방마다 터줏대감처럼 자리 잡은 문파 한두 개쯤은 있었고, 그들 중 대부분이 적천강 혹은 무림맹에 호의적이었으니까.

심지어 오지나 다름없던 남만이나, 오직 앞만 보고 달려와야 했던 지난 여정 역시 그러했다.

남만야수궁은 열화문과 과거의 연이 있었으며, 무림맹 산하의 개방과 하오문은 우리가 강소성으로 향하는 와중에도 길목 곳곳에 식량 혹은 준마를 준비해 두었었다.

하지만 지금부터는 아니다.

옛 황도였던 강소성부터 이 지경인데, 현재의 황도인 절강성은 어느 정도겠나.

‘그야말로 완전한 청정수겠지. 동네 무관 정도만 있는.’

우리에게 최악의 상황이 닥쳤을 때, 결국 가장 필요한 도움은 바로 무력(武力)이다.

그러나 내가 바라는 수준의 무력을 갖춘 집단은 인근 어디에서도 찾아볼 수 없을 것이다.

구파일방이나 오대세가는 고사하고, 이건 무슨 동네 태권도 학원뿐이니까.

‘아니, 이 경우는 태극권 학원인가.’

알록달록한 단체 도복을 입은 사람들이 우르르 몰려오는 상상을 하니 눈앞이 절로 아찔해진다.

‘도우러 왔습니다!’

‘어느 문파 출신이세요?’

‘경희 태극권입니다!’

‘아 그러시구나…… 그럼 실례지만 무공은 어느 정도?’

‘검은 띠입니다!’

‘아아…….’

‘절강 검도회에서도 왔습니다!’

‘아아아…….’

제발 어린이반 친구들만 아니길 바랄 뿐이다.

무관 가입 시 300만 메소. 아니 철전 석 냥을 준다는 조삼모사식 영업에 홀린 것도 슬픈데, 금위군까지 상대하게 되면 내가 무슨 낯으로 학부모 얼굴을 보겠나.

“최소 성인반. 오후 성인반으로…….”

“진 공자. 진 공자?”

홀린 듯이 중얼거리던 나는 홍진의 부름에 정신을 차렸다.

“아.”

“괜찮아요?”

“네. 괜찮습니다.”

“정말로? 식은땀이 비 오듯이 흐르는데.”

“잠깐 불길한 상상을 하는 바람에 그만.”

내 대답을 들은 홍진이 그늘진 얼굴로 입을 열었다.

“괜히 부른 게 아닌가 싶어서 미안해지네. 하지만 나로서도 어쩔 수 없는 선택이었어요. 오직 진 공자밖에 떠오르지 않더라고.”

“아닙니다. 충분히 이해해요.”

홍진이 단순히 믿을 만한 사람을 원했다면, 가장 가까운 태원진가에서 지원을 받아도 충분했을 것이다.

하지만 냉정하게 말하자면 태원진가에 나 정도의 고수는 어디에도 없다.

아니, 모든 요건을 충족시킬 수 있는 적임자는 천하 어디에서도 쉽게 찾아볼 수 없다.

홍진이 진정으로 원했던 것은, 신뢰 관계뿐만 아니라 어떤 위협에서도 상산왕 주표를 구해 줄 강자였으니까.

‘무림맹이 있지만, 당장 나 이외에 홍진이 믿을 수 있는 초절정 고수를 움직이기에는 위험 부담이 컸을 테고.’

해변의 바위가 움직여도 자국이 남는 법.

이미 암천과의 일전을 준비하며 천하 곳곳에 병력을 배치해 놓았을 텐데, 초절정 고수쯤 되는 전력이 빠진다면 그 공백이 너무나도 크다.

사안의 중요성이나 시기를 따져 봤을 때, 남만에서의 임무를 끝마친 나와 적천강만큼 믿음직한 패도 없었을 것이다.

‘자칫하면 나라의 근간부터 잠식당할 수도 있는 일이니까.’

차마 꺼내지 못한 말을 마음속으로 흘려보낸 그때. 몇 번을 들어도 아직 익숙해지지 않는 목소리가 창밖에서 들려왔다.

“곧 소주(蘇州)에 도착한다.”

바위처럼 딱딱한 음성. 금의위에서 천호(千戶)의 직책을 맡고 있는 사내. 정호군은 창문 틈새로 나를 바라보며 말을 이었다.

“상산왕 전하께 알려라. 오늘 안에 황제 폐하를 배알하실 것이라고.”
```

## Final English reading copy

```markdown
# Chapter 860

Murim martial artists were like weeds.

They could be found in dark back alleys and on bright main streets, surviving stubbornly in the depths of the mountains and even somewhere along the vast Yangtze.

Perhaps that was why the world they lived in came to be called Murim—the forest of martial arts.

Ruffians who ignored common sense and the law.

But even among the Murim martial artists who had carved out a forest of their own with sharply honed spears and blades, not all of them could grow into towering trees.

In the vast forest that was Murim, only the Nine Sects and One Gang, the Five Great Families, and a few forces that hadn’t reached their heights but had established themselves as the rulers of their respective provinces could be called towering trees.

*The Jin Family of Taiyuan was one of them, too.*

I thought to myself as I looked out the window.

Merchants in the middle of hawking their wares. A woodcutter passing by, sweating buckets under a back-breaking load of firewood. Ordinary commoners and well-dressed dignitaries in silk.

The world outside was full of all sorts of people, the stuff of any society. But one particular sort I’d seen just about everywhere until now was nowhere to be found.

“You can’t find any, can you?”

“Pardon?”

“Murim martial artists. Ones like Young Master Jin.”

Hong Jin had read my thoughts exactly. His face, powdered white, broke into a smile.

“I thought I’d warn you before you waste your energy looking. They’re hard to find in Jiangsu Province. That’s just the kind of place this is.”

“I’ve heard something to that effect… Is it because we’re so close to the imperial capital?”

“That must have something to do with it. They couldn’t let those ruffians run wild near the imperial capital, where the Son of Heaven resides.”

Hong Jin glanced at Hyuk Mujin and me, then added,

“Just so you don’t misunderstand, that’s how the powerful see it. The higher you climb, the more you care about appearances.”

It sounded like he was being polite in case I took offense, but there was no need. I could understand the reasoning to a point.

Well, to be precise, there were plenty of Murim martial artists who went too far.

But that didn’t explain everything just because we were close to the imperial capital.

Hyuk Mujin’s sudden question came from the same line of thought.

“Then what about the Nangong Family, sitting pretty in Anhui? It’s not all that far from the imperial capital, either.”

“Before I answer that, let me ask you the reverse. What’s left among the provinces next to the imperial capital, apart from the Nangong Family in Anhui?”

“Besides the Nangong Family… Well, that would be…”

Hyuk Mujin struggled to find an answer, and Hong Jin let out a quiet chuckle.

“Nothing. Jiangxi, Fujian, Jiangsu, and Anhui. Of the four provinces surrounding Zhejiang, where the imperial capital is located, the Nangong Family is the only famous Murim sect. Though there are exceptions.”

“Exceptions?”

“Yeah. How should I put it? If you judge by history alone, they seem like a real threat. But the imperial court would feel uneasy about going out of its way to provoke them. Martial artist Hyuk, you don’t know of any?”

Hyuk Mujin frowned and thought for a moment before answering.

“If I look into it carefully, I could probably name a few sects. But is there really one like that? Compared to the Nangong Family in Anhui, they’d be worth less than a horse’s balls.”

“Martial artist Hyuk, I don’t have any balls.”

“Ah! I’m sorry.”

“No, you don’t have to apologize that much. It just felt strange hearing it. Anyway, you really can’t think of one?”

“No. Of course not.”

Just then, I smacked Hyuk Mujin on the back of the head, the idiot who’d answered so confidently.

*Whack!*

“The Fire Gate Clan, you asshole! The Fire Gate Clan!”

“Ugh! Ow!”

“Mount Jiuhua in Anhui Province! Three hundred years of history! You saying the Fire Gate Clan’s worth less than a horse’s balls? You think the Fire Gate Clan’s a bunch of fucking pushovers?”

For the record, I was in my second year as a member of the Fire Gate Clan and diligently working my way through the heir-apparent training program.

As I beat Hyuk Mujin with my burning love for the company as fuel, Hong Jin spoke quietly.

“Um, Young Master Jin, sorry, but…”

“Oh, sorry. You don’t have those either.”

“That’s not what I meant. I was worried His Highness would wake up. And not all eunuchs are missing both. I believe I told you that once before.”

“My apologies again. I forgot you were only missing one.”

“……Fine. Please be careful. Keep your voice down so His Highness doesn’t wake.”

With an expression that had given up halfway, Hong Jin looked at Prince Shangshan Zhu Bao, sleeping peacefully, and continued.

“Anyway, Murim martial artists haven’t been able to run rampant in the provinces bordering the imperial capital—not just Zhejiang. Practitioners of the so-called demonic, heterodox arts couldn’t run rampant, of course. Even the Nangong Family—a towering tree of the orthodox faction and one of the Five Great Families—had to call on every connection it had among high-ranking officials.”

“It was that bad?”

“Yes. It happened right after the Great Nation was founded, so it was a long time ago. But things have stayed that way ever since. No matter how rough Murim martial artists were, they probably didn’t want to end up like the Maoshan Sect.”

“The Maoshan Sect?”

The name sounded familiar.

It had come up now and then in the many wuxia novels I’d loved to read back in school.

It wasn’t a major sect like the Nine Sects and One Gang, which appeared in every wuxia novel. It was more of a minor one, but it wasn’t hard to remember a few things about it.

More importantly…

“You mean the Maoshan Sect? The one famous for its sorcery rather than martial arts?”

“Hm? You didn’t know? It was right here in Jiangsu Province.”

It wasn’t as if I were some old master from a previous generation like the Fire King, who’d lived for over a hundred years. How was I supposed to know every little thing that had happened around the time the Great Nation was first established?

Still, what Hong Jin had just said was enough to make me pause.

*It was in Jiangsu Province…*

Past tense, not present.

Then I recalled how Hong Jin had mentioned the Maoshan Sect’s “fate,” and the fact that I’d never once heard its name during all my time in Murim.

The pieces fell into place.

“It disappeared. A long time ago.”

“Correct.”

Hong Jin snapped his fingers cheerfully and continued.

“The Great Nation’s first emperor, the Taizu, chose this place as his capital when he founded the country. Nanjing, in Jiangsu Province, had been the seat of six dynasties in the past. It was the imperial family’s first home.”

“So what happened?”

“With a new unified dynasty on the rise, could they really let the ruffians of the martial world run wild? Once the imperial edict went out, everything moved at lightning speed. Most of the sects in Jiangsu Province moved elsewhere. You’re starting to see where this is going, aren’t you?”

He’d said most of the sects, not all of them.

Guessing what came next, I murmured,

“The Maoshan Sect didn’t.”

“Right. A small number of Murim sects, including the Maoshan Sect, refused the imperial order to leave Jiangsu and held on to their headquarters. They say the Maoshan Sect was big enough to rival the Nine Sects and One Gang back then, so it could afford to be stubborn. But…”

The Great Nation’s first emperor had risen from the dirt and opened a new era—but he hadn’t been as magnanimous as the Maoshan Sect had thought.

“According to the records that remain, a hundred thousand Imperial Guards were dispatched. They killed and burned everything—not a single blade of grass or ant left behind.”

“……!”

“……!”

“That was how the Maoshan Sect was wiped out. And after that, no Murim sect ever established itself in Jiangsu again. Not even after His Imperial Majesty moved the capital to Zhejiang.”

Jiangsu wasn’t just an old imperial capital.

It was a Murim-free zone the Imperial Guards had already swept clean, the imperial family’s front yard, still steeped in the first emperor’s legacy.

And what that meant was perfectly clear.

*We can forget about asking for help.*

Until now, we’d been able to find help just about anywhere. Every province had one or two sects that had put down roots like the local old-timers, and most of them were friendly toward Jeok Cheongang or the Murim Alliance.

Even Nanman, practically the middle of nowhere, and our last journey, when we’d had to keep charging ahead without looking back, had been like that.

The Nanman Beast Palace had old ties with the Fire Gate Clan. And the Lower District Sect and the Beggars’ Sect, both under the Murim Alliance, had left food and fine horses along the route for us, even while we were on our way to Jiangsu.

But not from here on out.

If things were this bad in Jiangsu, the old imperial capital, what would Zhejiang, the current one, be like?

*An absolute Murim-free zone. Maybe they’ve got the odd neighborhood martial arts school.*

If the worst happened to us, what we’d need most of all was force.

But there probably wasn’t a group anywhere nearby with the level of strength I had in mind.

Forget the Nine Sects and One Gang or the Five Great Families. This was more like a neighborhood Taekwondo school.

*No, in this case, a tai chi school.*

Just picturing a mob of people in colorful matching uniforms coming to our aid made my eyes swim.

“We’ve come to help!”

“What sect are you from?”

“Kyunghee Tai Chi!”

“Oh, I see… So, if you don’t mind me asking, what level of martial arts have you reached?”

“I’m a black belt!”

“Ah…”

“We came from the Zhejiang Kendo Association, too!”

“Ahhh…”

I could only hope they weren’t all from the kids’ class.

It was bad enough to fall for that bait-and-switch pitch: sign up for the martial arts school and get three million mesos—no, three taels in iron coins. If those kids wound up facing the Imperial Guards too, how could I ever look their parents in the eye?

“Please, at least the adult class. The adult class in the afternoon…”

“Young Master Jin. Young Master Jin?”

I’d been muttering in a daze, but Hong Jin’s call snapped me back to my senses.

“Ah.”

“Are you all right?”

“Yes, I’m fine.”

“Really? You’re sweating like it’s pouring rain.”

“I just had a bad thought for a moment.”

At my answer, Hong Jin spoke with a shadow over his face.

“I’m starting to feel bad for calling you along. But I couldn’t help it. You were the only person I could think of.”

“No. I understand.”

If all Hong Jin wanted was someone he could trust, the Jin Family of Taiyuan was close enough to provide support.

But, coldly speaking, there was no one in the Jin Family of Taiyuan as strong as me.

No—the right person, someone who could meet every requirement, would be hard to find anywhere under heaven.

What Hong Jin truly wanted was not only someone he trusted, but a powerful martial artist who could save Prince Shangshan Zhu Bao from any threat.

*The Murim Alliance is there, but it would’ve been too risky to move a Supreme Peak master Hong Jin could trust other than me on such short notice.*

Even a rock on a beach left a mark when it moved.

They’d probably already deployed troops all over the land in preparation for a showdown with Dark Heaven. If they pulled away even one force as powerful as a Supreme Peak master, the gap would be enormous.

Given the importance and timing of the matter, there probably wasn’t a more dependable card than Jeok Cheongang and me, fresh from completing our mission in Nanman.

*This could eat away at the very foundations of the nation.*

I let the words I couldn’t bring myself to say drift through my mind. Then a voice that still sounded strange no matter how many times I heard it came from outside the window.

“We’ll reach Suzhou soon.”

His voice was as hard as a rock. The man held the rank of Thousand Captain in the Embroidered Uniform Guard. Jeong Hogun looked at me through the narrow gap in the window and continued.

“Inform His Highness Prince Shangshan. He will pay his respects to His Imperial Majesty sometime today.”
```
