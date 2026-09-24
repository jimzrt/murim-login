<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0976.txt",
      "sha256": "a3143dd737c38f340b5280e9638765a94a2d2afba7a479cd9f1da2ab5e639f1a",
      "bytes": 13547
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a937389b597764cc101ddee1917cd56dfe2306596e8eb48113bd16aa5c21c31f",
      "bytes": 1194
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "65892110351fce017f8020b13720d8c5e71418799da1db239060ea308ecc01e4",
      "bytes": 235501
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "dba657c824ce761e726f819b444d75350cf614f03c867d39e27b6903872f7186",
      "bytes": 759
    },
    {
      "path": "characters/Jamukha.md",
      "sha256": "49ad79f1c3c1f4e2045af306f413bae669d8995488880ee4922ebadae12eed47",
      "bytes": 611
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "faf89886c3dcc020807c02cff7dd7af834ea8ec4cb8c052a2849603a6af7d4e9",
      "bytes": 1291
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "563bd21844bc061a79a1bfd425956f71d732f1f807f57a0b7583e726e0092964",
      "bytes": 1481
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "0536c5afebb38570907dfb5cf046201da58b09134f3331d6970f532c9cdebdd2",
      "bytes": 1116
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8977e4652a26309585803ae58173efc1b1925bc8feae246a7b5f6a02dc25aa67",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4ab770334cae05e602b597ac621bf33ba47f4c3e433b466c45967edfdcdd594f",
      "bytes": 271188
    }
  ],
  "estimated_tokens": 11336
}
-->

# Durable State Update — Chapter 976

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
1 and safe_through 976. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 976. Profile updates may replace only one
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
  "chapter": 976,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 976,
    "continuity_sources": [976],
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
    "The Bow Saint has left the gorge to aid the Hebei Peng Family, where roughly two thousand fighters remain and pill-enhanced Keshiks have broken their formation.",
    "Jin Taekyung killed Jamukha and leveled up after the System awarded him substantial EXP and Fame.",
    "The North Heaven Demon Lord is retreating toward the gorge exit; a huge arrow of light is flying toward him, but its source and outcome are unknown.",
    "The conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu remain unknown.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved."
  ],
  "continuity_sources": [
    974,
    975
  ],
  "open_questions": [
    "Who sent the huge arrow of light toward the North Heaven Demon Lord, and what happens to him?",
    "What are the conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu?",
    "Can the Hebei Peng Family withstand the pill-enhanced Keshiks?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 975,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 정파     | **orthodox faction**                             |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 반고 | **Pangu** | Primordial giant from Chinese creation mythology. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 모용백 | **Murong Baek** | Former northern rival and later comrade of Peng Cheolhu. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 모용백 | 자무카 | commander_to_subordinate | you | plain and authoritative | Murong Baek gives Jamukha direct orders and rebukes him without honorific speech. |
| 자무카 | 모용백 | subordinate_to_commander_and_savior | you | deferential and honorific | Jamukha thanks Murong and addresses him with honorific speech. |
| 진태경 | 모용백 | adversaries | you | informal and confrontational | Directly asks whether Murong Baek beat up his older brother. |
| 모용백 | 진태경 | adversaries | you | informal | Addresses Taekyung directly during their confrontation. |
| 진태경 | 북천마군 | hostile opponents | you | casual, taunting, and profane | Taekyung teases and insults him during their standoff. |
| 적천강 | 북천마군 | former battlefield adversaries | you; you pup | blunt, familiar, and taunting | Jeok addresses him informally while challenging his alliance with Dark Heaven. |
| 북천마군 | 궁성 | hostile martial opponents | Bow Saint | calm and formally familiar | Addresses her directly while acknowledging her effort. |
| 북천마군 | 자무카 | lord to subordinate | my lord | formal-deferential | Jamukha answers the Demon Lord’s command with 하명하십시오. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 975
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jamukha.md

# Jamukha (자무카)

- **Safe through:** Chapter 975
- **Aliases:** None
- **Role:** Jamukha was the ruler of the western steppe and a former eastern-steppe chieftain recruited into Dark Heaven by Murong Baek; Jin Taekyung killed him.
- **Personality:** Patient and ambitious, he was willing to feign loyalty to gain the power to rule the steppe and north.
- **Voice:** Not established
- **Relationships:** Peng Cheolhu defeated him more than fifty years ago; Murong Baek spared and recruited him, but Jamukha’s loyalty to him was feigned.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 975
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 975
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and learning to trust his allies rather than carry every burden alone.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 966
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he commits firmly to his principles, even when doing so means remaining in a losing battle.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 975
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃976화



등 뒤에서 벼락처럼 내리꽂히는 한 줄기의 섬뜩한 기운을 인지한 그 순간, 북천마군은 섬광과도 같은 속도로 돌아서며 창을 휘둘렀다.

콰아앙!

거대한 충돌.

그러나 창날에 실린 미증유의 기운이 빛의 화살을 집어삼키는 광경 앞에서도, 북천마군의 얼굴은 돌처럼 딱딱하게 굳어 있었다.

그를 향한 공격은, 그것으로 끝이 아니었으니까.

슈화아악!

바람이 갈라졌다.

칠흑처럼 어두컴컴하던 허공이, 그 너머에서 들이닥치는 십여 개의 빛줄기를 바라보는 북천마군의 눈동자가 붉게 물들었다.

“궁성(弓星)-!”

분노가 실린 일갈을 터트리며, 더 이상의 선택지가 없음을 깨달은 북천마군은 창을 내뻗었다.

그의 손에 들린 창날이 나아가는 궤적을 따라 공간이 일그러졌다.

콰아아앙!

드드득!

마치 지진이라도 난 것처럼 요동치는 공간 속, 굉음과 함께 터져 나온 막강한 충격파가 반경 십여 장을 휩쓸었다.

그리고 찰나의 순간 비좁은 협곡을 집어삼킨 그 거대한 먼지구름 사이로, 두 줄기의 바람이 불었다.

무더운 한여름 낮의 그것보다 뜨겁고, 머나먼 서쪽 너머에 펼쳐진 열사(熱砂)의 사막보다 숨 막히는 열기를 간직한 바람이.

화악.

순식간에 불어닥친 그 열풍(熱風)을, 북천마군은 똑똑히 느낄 수 있었다.

동시에 보았다.

섬광 너머로 자신을 향해 쏘아지는 두 사람의 모습을.

같은 뿌리에서 자라나, 각기 다른 색의 화염이 이글거리는 두 개의 주먹을.

고오오옹.

멸염신권(滅炎神拳).

공간을 불사르며 나아가는 끔찍한 열기를 직시하며, 북천마군은 온 힘을 다해 창날을 내뻗었다.

구구구구궁!

그 끝에, 아득한 섬광이 있었다.



* * *



모든 것은 찰나의 순간에 시작되고, 끝났다.

반고(盤古).

한 자루의 도끼로 세상을 갈랐다는 태곳적의 거인이 한껏 숨을 들이쉰 것처럼 온 사방의 공기가 팽팽하게 조여들었고, 이내 모든 것을 터트리고 밀어 냈다.

구구구궁!

이것을 무엇이라 불러야 할까.

폭발? 아니면 재앙?

진위경을 비롯한 산서인들은 그 의문에 대한 답을 찾을 수 없었다.

그들은 지금껏 겪어 본 적 없는. 아니, 상상할 수도 없었던 압도적인 기운에 짓눌린 채 자신들을 휩쓸어 오는 그 거대한 힘의 파도를 바라볼 뿐이었다.

쿠궁, 콰아아아아!

세상이 뒤집혔다.

보이지 않는 파동에 휩쓸려 튕겨 나가려는 신형을 붙잡기 위해, 산서인들은 서로를 지탱하고 각자의 날붙이를 지면 깊숙이 박아 넣었다.

귀가 먹먹했다.

본능적으로 일어난 경외와 공포가 그들의 전신을 옥죄었다.

정확히는 이 거대한 충격파를 불러온 원인이자 이유라 할 수 있는, 몇 사람을 제외한 모두를.

스악.

창날이 공간을 갈랐다.

눈과 귀로 파악할 수 없는 새로운 영역에서, 진태경과 적천강은 창날을 따라 쏘아진 강기를 피하며 주먹을 뻗었다.

퍼어엉!

끔찍한 열기와 함께 터져 나가는 공기.

그러나 뒤늦게 울려 퍼진 파공성보다 앞서 쏘아진 화염이 공간을 휘감았을 때, 북천마군의 신형은 이미 그들의 머리 위를 덮쳐 가고 있었다.

슈확!

비스듬히 내리그어진 창날.

진태경이 신형을 비튼 그때, 창날에 실린 강기가 더욱 크기를 부풀리며 그의 어깻죽지를 향해 떨어져 내렸다.

서걱.

‘베었다.’

순간 북천마군의 뇌리에 떠오른 확신이었고, 틀림없는 사실이기도 했다.

지금 막 그가 베어 낸 것이, 살과 뼈가 아니라 불그스름한 빛이 도는 갑옷이라는 것을 제외한다면.

푸슉!

강기에 의해 갈라진 화룡갑(火龍鉀)의 틈새로 솟구치는 선혈.

불과 한 줌도 되지 않는 그 미량의 핏물만이 북천마군이 취할 수 있었던 모든 것이었고, 두 스승과 제자는 기회를 놓치지 않았다.

콰득.

진태경이 갈고리처럼 그러쥔 양손으로 창대를 붙잡은 순간, 북천마군은 본능적으로 깨달았다.

잠력단을 통해 극도로 향상된 신체 능력으로도, 끝없이 샘솟는 수 갑자의 공력으로도 눈앞의 핏덩이가 지닌 힘을 감당할 수 없다는 것을.

‘무슨 이런 괴물이……!’

무릇 높은 곳에 이를수록 멀리 보이는 법.

하지만 광활하기 그지없는 북천마군의 세상 속에서도, 진태경의 존재는 지금껏 본 적 없는 괴물 그 자체였다.

나이가 믿어지지 않는 성취.

초인(超人)이라 불리는 이들조차 훌쩍 넘어선 신체 능력에 더하여, 어째서인지 자무카를 쓰러트린 뒤부터 더욱 빠르고 강해진 움직임과 공력까지.

이것만으로도 충분히 위협적인 적수였지만, 지금 이 순간 북천마군의 등골을 더욱 서늘하게 만드는 것은 이 젊은 괴물과 함께하는 노괴(老怪)의 존재였다.

후웅.

새벽의 찬 공기가, 그 안에 스며든 습기가 단숨에 증발한다.

무시무시한 열기를 머금은 일장(一掌)을 내뻗으며 들이닥친 적천강의 모습이, 북천마군의 눈동자를 불그스름하게 달구었다.

‘화왕(火王)……!’

더 이상 선택의 여지도, 새로운 선택지를 찾을 시간조차 없다.

북천마군은 오랜 세월 동안 함께 했던 애병(愛兵)을 놓으며 땅을 박찼다.

치이익.

영혼까지 스며드는 듯한 작열통(灼熱痛).

다급하게 물러나는 표적을 쫓아 맹렬하게 솟구친 화염은 스친 것만으로도 갑옷을 녹이고 살갗을 태웠다.

그리고 찰나의 고통을 감내하며 다급하게 뒷걸음질 치는 북천마군을 향해, 그를 떠나 새로운 주인을 찾은 창날이 번뜩였다.

쉬쉬쉬쉭!

수십 개로 나뉘어 쏟아지는 창영(槍影)이 공간을 뒤덮는다.

모든 감각을 끌어올린 채 쉴 새 없이 신형을 비틀고 뒤집는 북천마군의 움직임을 쫓아, 끈질기게 달라붙는 창날의 끝에서 청백색의 화염이 솟구쳤다.

화아악, 서걱!

뜨겁다.

베어짐과 동시에 녹아내린 갑옷의 틈새 사이로 핏물이 솟구쳤다.

앞서 진태경이 흘린 것보다도 많고, 어두운색을 지닌 검붉은 핏줄기가 순간 아찔해진 북천마군의 시야를 물들였다.

불현듯 귓가를 파고든, 나직한 목소리와 함께.

“아직 안 끝났다.”

“……!”

“이 악물어.”

서걱, 서걱, 서걱!

쌓아 올리기까지는 오랜 세월이 걸렸으나, 무너지는 것은 한순간이다.

기회를 놓치지 않고 연이어 휘둘려진 창날에, 북천마군의 전신을 빈틈없이 둘러싸던 갑옷은 무용지물이나 다름없었다.

철컥. 투두둑!

조각난 철갑 위로 핏물이 흩뿌려진다.

북천마군은 타들어 가는 듯한 통증을 느끼며 이를 악물었다.

지금 이 순간 쉴 새 없이 들이닥치는 화염에 힘없이 녹아내리고, 부서지는 것은 비단 그가 걸친 갑옷뿐만이 아니었다.

모든 것.

모용백으로서 이루었던, 북천마군으로서 이루고자 했던 과거와 미래의 모든 것이 잿더미가 되어 조금씩 흩어지고 있었다.

‘어째서!’

북천마군은 마음속으로 부르짖었다. 아직 사그라지지 않은 거대한 기운을 주먹에 담아 흩뿌렸다.

콰앙!

하늘이 쪼개지는 듯한 굉음과 함께 공간이 뒤흔들렸다.

그러나 산도 허물어 버릴 것 같은 그 일격은, 그 무엇에도 닿지 못한 채 허공을 찢어발겼을 뿐이었다.

“오래전, 네놈을 마주할 때마다 항상 드는 생각이 있었지.”

화왕 적천강.

일백하고도 수십여 년을 살아온 구화산의 노괴가, 북천마군을 향해 걸음을 뗐다.

쉭.

증발하듯 사라져 버린 신형. 동시에 옆구리를 뜨겁게 달구는 거대한 열기.

화아악.

눈부신 광염(光焰)이 어둠을 집어삼킨다. 본능적으로 고개를 든 북천마군의 두 눈동자를 새하얗게 물들였다.

“그놈 참, 못 믿을 눈깔을 가졌다고.”

그 순간.

북천마군은 보았다.

평온한 목소리와는 어울리지 않는 광포한 화염을.

붉지도, 푸르지도 않은 눈부신 불의 파도를.

콰아아앙!

움직임을 따라가지 못한 굉음이 뒤늦게 온 사방을 떨쳐 울린다.

강대한 힘을 이기지 못하고 암벽 깊숙이 처박힌 북천마군은 울컥 솟구치는 핏물을 삼켜 냈다.

‘아직, 아직이다.’

끝나지 않았다. 쓰러질 수 없다.

북천마군은 흐릿해진 시야를 느끼며, 요람처럼 전신을 감싼 암벽에서 몸을 일으켜 세웠다.

아니, 일으켜 세우려 했다.

충돌의 여파로 소나기처럼 떨어져 내리는 무수한 암석의 파편과 희뿌옇게 피어오르는 먼지구름 너머, 한 줄기 섬광이 번뜩이기 전까지는.

푹, 콰드득!

청백색의 불꽃이, 그 끔찍한 열기로 뒤덮인 창날이 어깻죽지를 관통한다. 뼈와 살을 부수고 암벽 깊숙이 틀어박혔다.

“……!”

형용할 수 없는 격통에 파르르 떨리는 전신.

그러나 북천마군은 포기하지 않았다. 눈앞을 새하얗게 물들이는 고통 속에서 온 힘을 다해 몸부림쳤다.

“크아아아아악!”

퍼걱, 푸화악!

마침내 뽑혀 나온 창날. 아니, 몸뚱어리.

어깨를 관통하고 암벽 깊숙이 틀어박힌 창을 뽑는 대신, 이를 악물어 어깨를 뽑아낸 북천마군은 지면을 박차고 솟구쳤다.

휘몰아치는 먼지구름을 뚫고, 암벽과 허공을 밟으며 쏘아졌다.

자신을 죽음 끝까지 몰아세운 두 괴물을 피해서.

그리고 자신의 앞에 놓인 유일한 생로(生路)를 향해서.

쐐애액!

극심한 고통와 부상으로 진작 쓰러지고도 남았을 몸뚱어리도, 고작 한 줌밖에 남지 않았을 공력도 잠력단의 효능으로 잊혀진 지금.

북천마군은 혼신의 힘을 다해 나아가고 있었다.

사방에 내려앉은 짙은 먼지구름 너머에서, 이 믿을 수 없는 광경 앞에 굳어 있을 사냥감들을 생각하며.

위기에 처한 자신을 구해 줄 수 있는 유일한 동아줄을 떠올리며.

‘진위경.’

태원진가의 소가주이자, 오늘날의 전투를 이끈 산서성의 맹주.

그와 더불어, 누군가의 소중한 혈육.

‘놈을 사로잡는다면, 생로가 열린다.’

천하 오대 세가의 일원인 모용세가의 후계자로, 가주로 일평생을 살았다.

비록 속살은 검었으나, 거죽은 희었다.

그렇게 맹수의 이빨을 감춘 채 정파(正波)라는 울타리에서 함께 어울려 지낸 세월이 몇 년이던가.

북천마군은 소위 정파라 불리는 이들에 대해 누구보다 잘 알고 있었다.

그들의 생리, 습성, 사고방식을 비롯한 그 모든 것들을.

그리고 화왕 적천강과 함께 자신의 궁지로 몰아세운 태원진가의 젊은 핏덩이가, 다른 그 누구보다 정(正)이라는 단어에 얽매인 인물이라는 것 역시도.

‘그래서다. 너희가 나를, 우리를 꺾을 수 없는 가장 큰 이유는.’

서로의 전력을 다한 전투에서 패배했고, 반드시 성공하리라 확신했던 대계(大計)는 물거품으로 돌아갔다.

하지만 그것이 마지막을 의미하는 것은 아니다.

살아남을 수만 있다면, 기회는 온다.

그리고 북천마군은 반드시 돌아올 것이다.

머지않은 미래에, 그가 느낀 패배의 쓰라림과 적들의 환호가 가라앉기도 전에 다시 한번 모용세가의 깃발을 휘날리며 천하를 종횡할 터였다.

어두운 하늘 아래에서, 숨겨 두었던 이빨을 마음껏 드러낸 채.

‘다시 돌아올 것이다. 내 모든 것을 걸어서라도.’

북천마군은 오늘 자신이 겪은 패배감과 수모를 떠올리며 새로운 각오를 되새겼다.

지금 이 순간, 고통과 희망으로 마비되어 버린 이성이 헛된 판단을 내리고 있다는 사실조차 인지하지 못한 채.

어찌하여 이런 상황에서도 적천강과 진태경이 자신을 뒤쫓지 않는지에 대한 의문조차 제대로 떠올리지 못한 채.

그리고 마침내 흩어지는 먼지구름 너머로, 북천마군은 그토록 바라왔던 진위경의 모습을 확인할 수 있었다.

처음부터 지금까지, 늘 선두에서 모든 이들을 이끌었던 그의 앞에 우뚝 선 한 사람의 존재도 함께.

“궁……성.”

철벅.

북천마군의 입술 사이로 흘러나온 침음성.

끝없이 계속해서 나아갈 것 같던 발걸음이 피 웅덩이를 밟으며 멈춰선 그 순간, 공허한 눈빛으로 궁성을 바라보던 북천마군의 귓가로 누군가의 목소리가 흘러들었다.

“뽀삐. 어디 갔니, 뽀삐.”

먼지구름을 비집고 울려 퍼지는 애타는 목소리.

얼마 지나지 않아 그 안에서 불쑥 모습을 드러낸 진태경이, 북천마군을 향해 눈을 부릅떴다.

“세상에, 뽀삐! 여기서 뭐 해!”

“……!”

북천마군의 눈꺼풀이 파르르 떨렸다.
```

## Final English reading copy

```markdown
# Chapter 976

The instant he sensed a chilling force plunge down behind him like a bolt of lightning, the North Heaven Demon Lord spun around at lightning speed and swung his spear.

*BOOOOM!*

A tremendous collision.

Yet even as the unprecedented force carried on his spearhead swallowed the arrow of light, the North Heaven Demon Lord’s face remained as hard as stone.

Because the attack aimed at him wasn’t over.

*Shwaaa!*

The wind split apart.

The eyes of the North Heaven Demon Lord, watching a dozen or so streaks of light rush at him from beyond the pitch-black sky, turned red.

“Bow Saint—!”

With an angry shout, the North Heaven Demon Lord realized he had no choice left and thrust out his spear.

Space warped along the path of the spearhead in his hand.

*BOOOOM!*

*Krrrrk!*

Space shuddered as if struck by an earthquake. A tremendous shock wave burst forth with a deafening roar and swept across a radius of more than a dozen *zhang*.

An enormous cloud of dust swallowed the narrow gorge in an instant. From within it, two gusts of wind blew.

Hotter than the air on a midsummer afternoon, more suffocating than the scorching desert sands far to the west.

*Fwoosh.*

The North Heaven Demon Lord felt that sudden blast of heat all too clearly.

And he saw them.

Two figures shooting toward him through the flash of light.

Two fists, grown from the same root, wreathed in flames of different colors.

*Gooooong.*

Flame-Extinguishing Divine Fist.

As he stared down the terrifying heat burning its way through space, the North Heaven Demon Lord thrust out his spearhead with all his strength.

*Rrrrrum!*

At its tip, a distant flash of light blazed.

* * *

It all began and ended in the blink of an eye.

Pangu.[^1]

As if the primordial giant who was said to have split the world with a single axe had drawn in a deep breath, the air all around tightened taut. Then it burst outward, sweeping everything away.

*Rrrrrum!*

What should this be called?

An explosion? Or a catastrophe?

Jin Wikyung and the people of Shanxi couldn’t find an answer.

Crushed beneath an overwhelming force they had never experienced before—no, one they couldn’t even have imagined—they could only watch as a vast wave of power swept toward them.

*KABOOM! KAAAAABOOM!*

The world turned upside down.

To keep themselves from being swept up and flung away by the invisible shock wave, the people of Shanxi braced one another and drove their blades deep into the ground.

Their ears rang.

Instinctive awe and terror tightened around their entire bodies.

That was true of everyone except the few people who had caused this tremendous shock wave.

*Shhk.*

A spearhead cleaved through space.

In a realm neither eyes nor ears could perceive, Jin Taekyung and Jeok Cheongang dodged the Force shooting along the spearhead and thrust out their fists.

*Poom!*

Air erupted with a blast of terrible heat.

But when the flames, launched before the delayed boom, coiled through space, the North Heaven Demon Lord was already swooping down over their heads.

*Shwaa!*

A spearhead slashed down at an angle.

Just as Jin Taekyung twisted his body, the Force carried on the spearhead swelled larger still and came crashing toward his shoulder.

*Shhk.*

*I cut him.*

That certainty flashed through the North Heaven Demon Lord’s mind. It was absolutely true.

Except what he had just cut wasn’t flesh and bone, but armor that glowed faintly red.

*Pshk!*

Blood spurted from the split in the Fire Dragon Armor, cut open by the Force.

That tiny trickle—not even a handful—was all the North Heaven Demon Lord had managed to draw. The Master and Disciple didn’t let the opportunity slip.

*Crack.*

The instant Jin Taekyung clamped both hands around the shaft like hooks, the North Heaven Demon Lord understood on instinct.

Even with the Temporary Strength Pill’s immense boost to his physical abilities, and even with several centuries’ worth of internal energy surging without end, he couldn’t withstand the strength of the young man before him.

*What kind of monster is this…!*

The higher you climbed, the farther you could see.

But even across the North Heaven Demon Lord’s vast world, Jin Taekyung was a monster the likes of which he had never seen.

An achievement unbelievable for his age.

Physical abilities far beyond even those called superhuman. And for some reason, ever since defeating Jamukha, his movements and internal energy had grown faster and stronger still.

That alone made him a dangerous opponent. But what chilled the North Heaven Demon Lord’s spine even more in that moment was the old monster fighting alongside the young one.

*Whoom.*

The moisture in the cold dawn air evaporated in an instant.

Jeok Cheongang charged in with a palm strike brimming with terrifying heat. A reddish glow lit the North Heaven Demon Lord’s eyes.

*The Fire King…!*

There were no choices left, not even time to look for another.

The North Heaven Demon Lord released the beloved weapon he had carried for years and kicked off the ground.

*Sss!*

A burning pain that seemed to seep into his very soul.

The flames surged after their retreating target. Even a glancing touch melted armor and scorched skin.

And as the North Heaven Demon Lord endured that instant of pain and stumbled backward in a desperate retreat, the spearhead that had left him for a new master flashed toward him.

*Shshshshk!*

Dozens of spear images poured down, covering the space. The spearhead relentlessly pursued the North Heaven Demon Lord as he twisted and flipped his body without respite, drawing on every sense. Blue-white flames surged from its tip.

*Fwoosh! Shhk!*

Hot.

Blood welled from the gaps in the armor, melted open as it was cut. More than the blood Jin Taekyung had shed, it poured out in a dark, deep crimson stream, staining the North Heaven Demon Lord’s vision as it swam for a moment.

Along with a quiet voice that suddenly reached his ear.

“It’s not over yet.”

“……!”

“Grit your teeth.”

*Shhk, shhk, shhk!*

It took a long time to build something up, but it could all come crashing down in an instant.

The spearhead kept swinging, one strike after another, leaving the armor that had covered the North Heaven Demon Lord’s whole body all but useless.

*Clank. Clatter!*

Blood sprayed across the shattered iron plates.

The North Heaven Demon Lord gritted his teeth against the searing pain.

The flames that kept crashing down on him melted and broke things apart without resistance. And what was falling to pieces wasn’t only the armor he wore.

Everything.

Everything he had accomplished as Murong Baek, everything he had hoped to accomplish as the North Heaven Demon Lord—his past and future, all of it—was turning to ashes and scattering, bit by bit.

*Why!*

The North Heaven Demon Lord screamed in his heart. He gathered the vast force that had yet to fade into his fist and flung it outward.

*BOOM!*

Space shook with a roar that sounded as if the heavens had split apart.

Yet the strike, powerful enough to bring down a mountain, tore through empty air without touching a thing.

“Long ago, every time I saw you, I always had the same thought.”

The Fire King, Jeok Cheongang.

The old monster of Mount Jiuhua, who had lived for well over a hundred years, took a step toward the North Heaven Demon Lord.

*Whoosh.*

His figure vanished as if it had evaporated. At the same time, enormous heat scorched the North Heaven Demon Lord’s side.

*Fwoosh.*

Blinding light-flames swallowed the darkness. The North Heaven Demon Lord instinctively looked up, his eyes turning white with their light.

“You really do have the kind of eyes no one can trust.”

In that instant,

the North Heaven Demon Lord saw it.

A savage blaze at odds with Jeok Cheongang’s calm voice.

A dazzling wave of fire, neither red nor blue.

*BOOOOM!*

The roar came too late to keep up with the movement, then shook everything around them.

Unable to withstand the force, the North Heaven Demon Lord crashed deep into the cliff wall and swallowed the blood surging up his throat.

*Not yet. Not yet.*

It wasn’t over. He couldn’t fall.

He sensed his vision blurring and pushed himself up from the cliff that cradled him like a nest.

No—he tried to.

Until a flash of light flickered through the dust cloud rising pale beyond the countless rock fragments raining down from the collision.

*Thud! Krrrk!*

The spearhead, wreathed in blue-white flame and cloaked in dreadful heat, pierced his shoulder. It smashed through bone and flesh and drove deep into the cliff.

“……!”

His entire body quivered with indescribable pain.

But the North Heaven Demon Lord refused to give up. Through the pain that turned his vision white, he fought with all his strength.

“GRAAAAAH!”

*Crack! Fwoosh!*

At last, the spearhead came free—or rather, his body did.

Instead of pulling out the spear lodged deep in the cliff through his shoulder, the North Heaven Demon Lord gritted his teeth and tore his shoulder free. Then he kicked off the ground and shot upward.

He burst through the churning dust cloud, bounding off the cliff face and the very air.

Away from the two monsters who had pushed him to the brink of death.

Toward the only path of escape before him.

*Shweee!*

His body should have already collapsed from his terrible pain and injuries. His internal energy should have dwindled to a mere handful. But the Temporary Strength Pill’s effects made him forget all of it.

The North Heaven Demon Lord pushed onward with every ounce of strength he had.

Thinking of the prey who would be frozen in disbelief beyond the thick dust cloud settling all around.

Thinking of the only lifeline that could save him from his predicament.

*Jin Wikyung.*

The Lesser Family Head of the Jin Family of Taiyuan, and Alliance Leader of Shanxi Province’s forces in today’s battle.

And, to someone, a precious member of the family.

*If I take him hostage, I can escape.*

He had spent his entire life as the heir—and then the Family Head—of the Murong Family, one of the Five Great Families.

His insides had been black, but his outward face was clean.

How many years had he spent hiding the teeth of a beast while living alongside them within the orthodox faction’s fence?

The North Heaven Demon Lord understood the people called orthodox better than anyone.

Their nature, their habits, their way of thinking—all of it.

He also knew that the young upstart of the Jin Family of Taiyuan who had cornered him alongside the Fire King was bound more tightly than anyone else by the word *righteousness*.

*That’s why. It’s the biggest reason you can’t defeat me—or us.*

They had lost a battle in which both sides had given everything they had, and the grand plan they had been certain would succeed had gone up in smoke.

But that didn’t mean it was the end.

As long as he survived, another chance would come.

And the North Heaven Demon Lord would return.

In the not-too-distant future, before the sting of his defeat and his enemies’ cheers had faded, he would once more unfurl the Murong Family’s banner and stride across the land.

Beneath a dark sky, with his hidden fangs bared to the fullest.

*I will return. Even if I have to stake everything I have.*

The North Heaven Demon Lord thought back on the defeat and humiliation he had suffered that day and renewed his resolve.

In that moment, his reason—numbed by pain and hope—couldn’t even recognize the foolishness of his decision.

He couldn’t even properly wonder why Jeok Cheongang and Jin Taekyung weren’t chasing him, even in this situation.

And at last, beyond the dispersing cloud of dust, the North Heaven Demon Lord saw Jin Wikyung—the man he had wanted so desperately to find.

He also saw the person standing tall before him, directly in front of Jin Wikyung, who had led everyone from the front from the very beginning.

“Bow… Saint.”

*Splash.*

A low moan slipped between the North Heaven Demon Lord’s lips.

Just as his steps—which had seemed as if they would go on forever—stopped in a pool of blood, he stared at the Bow Saint with hollow eyes. Then someone’s voice drifted into his ears.

“Poppy. Where did you go, Poppy?”

An anxious voice rang out through the cloud of dust.

Moments later, Jin Taekyung suddenly emerged from within it and stared wide-eyed at the North Heaven Demon Lord.

“Oh my god, Poppy! What are you doing here?”

“……!”

The North Heaven Demon Lord’s eyelids twitched.

[^1]: Pangu is a primordial giant in Chinese creation mythology, said to have separated heaven and earth.
```
