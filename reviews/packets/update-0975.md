<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0975.txt",
      "sha256": "5daa87111a2d84d823a87ca5db2c631c62074b636e5e7eaf810289b62324ebfc",
      "bytes": 12711
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "03429380dd6120063706497f3d5a809543dbcdabf1eacb965730b8ac48d5f0fa",
      "bytes": 1456
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "65892110351fce017f8020b13720d8c5e71418799da1db239060ea308ecc01e4",
      "bytes": 235501
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6b47fe87c9a41708c30eb9ac996922da8be6540f2d9876bea343823dc02997de",
      "bytes": 759
    },
    {
      "path": "characters/Jamukha.md",
      "sha256": "e8e9b9029f3e12e61c25cb1ba2a6846d5ba582bac2e963711beacfa8a3d5073f",
      "bytes": 574
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "7611b173ef38304751330eed53c9b5ae4a3c62ca9f1235b46506c7aa3a763e76",
      "bytes": 1291
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9c8c19215413407e76a1f5c62ddbaa94c316d782fda7acfaaa73f8f3f6613001",
      "bytes": 1481
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "7d9d4b1c005aa777940c622f6ab028afb99e8c0ac1edb9e5101b7c87dbc26430",
      "bytes": 622
    },
    {
      "path": "characters/Ju Gongsan.md",
      "sha256": "31aa2192942ec2fc383e463b574b5289c969111c46a3603314daf8d17dac17f1",
      "bytes": 900
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "c262bdaf429a3910d069dcdfddb559c83dae31e0f3569a1263392e038bdd21de",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4ab770334cae05e602b597ac621bf33ba47f4c3e433b466c45967edfdcdd594f",
      "bytes": 271188
    }
  ],
  "estimated_tokens": 10697
}
-->

# Durable State Update — Chapter 975

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
1 and safe_through 975. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 975. Profile updates may replace only one
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
  "chapter": 975,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 975,
    "continuity_sources": [975],
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
    "The North Heaven Demon Lord, Murong Baek, has taken a Temporary Strength Pill and is fighting Taekyung and Jeok Cheongang alongside Jamukha.",
    "Jeok Cheongang is badly wounded in the hands while holding off the Demon Lord’s spear; a razor-sharp gust has just shot toward his back, with its source and outcome unknown.",
    "Jamukha has vowed to deliver Jin Taekyung’s head and victory in exchange for the Hebei Peng Family’s lands and lives.",
    "The conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu remain unknown.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved."
  ],
  "continuity_sources": [
    973,
    974
  ],
  "open_questions": [
    "Who sent the razor-sharp gust toward Jeok Cheongang, and what happens to him?",
    "How will the renewed confrontation with Murong Baek and Jamukha unfold?",
    "Can the Hebei Peng Family withstand the pill-enhanced Keshiks?",
    "What are the conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 974,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 주공산 | **Ju Gongsan** | Former head and founder of the Yongbong Escort Bureau. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 이형환위 | **Shifting Form and Position** | Supreme Peak movement or evasion technique used by Jeok Cheongang. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 진태경 | 북천마군 | hostile opponents | you | casual, taunting, and profane | Taekyung teases and insults him during their standoff. |
| 적천강 | 북천마군 | former battlefield adversaries | you; you pup | blunt, familiar, and taunting | Jeok addresses him informally while challenging his alliance with Dark Heaven. |
| 북천마군 | 자무카 | lord to subordinate | my lord | formal-deferential | Jamukha answers the Demon Lord’s command with 하명하십시오. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 974
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jamukha.md

# Jamukha (자무카)

- **Safe through:** Chapter 974
- **Aliases:** None
- **Role:** Jamukha is the ruler of the western steppe and a former eastern-steppe chieftain recruited into Dark Heaven by Murong Baek.
- **Personality:** Patient and driven by a long-standing desire to avenge his defeat by Peng Cheolhu.
- **Voice:** Not established
- **Relationships:** Peng Cheolhu defeated him more than fifty years ago; Murong Baek spared him, recruited him into Dark Heaven, and commands him as a subordinate.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 974
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 974
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and learning to trust his allies rather than carry every burden alone.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 974
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Gongsan.md

# Ju Gongsan (주공산)

- **Safe through:** Chapter 954
- **Aliases:** Escort King
- **Role:** Founder and former head of the Yongbong Escort Bureau; during the Great Faction War, he was a wandering escort who refused to surrender a pregnant woman of the Guangdong Chen Family to the Demonic Cult after accepting her escort fee, carried her from Guangdong through Jiangxi and Hubei to Henan over two years, and became known as the Escort King; he later founded an escort bureau in his hometown of Shaanxi and died from internal injuries sustained during the war.
- **Personality:** Remarkably skilled, chivalrous, principled, and unwavering in his obligations.
- **Voice:** Not established.
- **Relationships:** Ju Hogun was his only blood child and successor as head of the Yongbong Escort Bureau; Ju Hwaran is his granddaughter.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 950
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃975화



제아무리 잘 훈련받은 사냥개라고 해도 홀로 맹수를 쓰러트릴 수는 없다.

타고난 태생의 차이는 어쩔 수 없는 법이니까.

그러나 맹수로 태어나, 원하는 목적을 위해 사냥개가 된 자무카는 달랐다.

그는 훈련받은 맹수였다.

어떤 적과도 맞설 수 있는 포식자의 힘과 사냥개로서의 충성심을 고루 갖춘.

그렇기에 주인의 부름이 들려온 그 순간, 단 한 치의 망설임 없이 몸을 날릴 수 있었다.

“자무카!”

기다렸던 신호가 떨어지기 무섭게, 자무카는 온 힘을 다해 곡도를 흩뿌렸다.

콰앙!

허공에서 격돌하는 두 갈래의 강기.

잠력단의 효능으로 더욱 어둡고 거대해진 암녹빛 도강(刀罡)이 청백색의 불꽃을 잠시나마 밀어 낸 그때, 자무카의 발끝이 화살처럼 쏘아졌다.

쉭.

순간 흐릿해지는 신형.

찰나의 시간 속에서 발휘된 이형환위(移形換位)와 함께, 자무카는 한 줄기 바람이 되어 십여 장의 공간을 가로질렀다.

지금껏 만난 그 어떤 사냥감들보다도 흉포하고 강력한, 화왕(火王)이라는 맹수를 향해.

‘단 일격. 일격이면 충분하다.’

자무카의 몸놀림에는 확신에 가까운 자신감이 스며들어 있었고, 그것은 결코 근거 없는 허세가 아니었다.

하북팽가의 패도적인 무공에 맞서기 위해 극쾌(極快)만을 추구해 온 세월이 장장 오십여 년.

제아무리 신룡(神龍)이라 불리는 진태경이라 하더라도 그 장구한 세월의 차이를 따라잡기에는 한계가 있다는 것을, 자무카는 믿어 의심치 않았다.

더군다나…….

‘이 힘이라면, 무엇이든 할 수 있다.’

모든 것이 달라졌다. 한 꺼풀을 벗고 새롭게 태어난 애벌레처럼 온 세상이 새롭게 보였다.

지면을 스치듯 나아가는 발끝도, 양손 가득 그러쥔 애병도 그 어느 때보다 가볍다.

모든 힘을 한계 이상으로 끌어낸 잠력단의 효능은, 이 순간조차도 자무카의 전신 깊숙한 곳에서 쉴 새 없이 들끓고 있었다.

오감(五感)을 넘어 개방된 여섯 번째 감각이, 등 뒤에서 들이닥치는 한 줄기의 불꽃마저 손쉽게 회피할 수 있게 만들었다.

쐐애애액!

자무카는 달려가는 속도를 더하며 고개를 틀었다. 진태경의 손을 떠나 공간을 가로지르며 쏘아진 창날이 그의 목덜미를 스쳐 암벽에 틀어박혔다.

꽈아앙!

날카로운 암석의 파편이 사방으로 튀었다. 일어나려는 먼지구름 위를 뛰어넘은 자무카의 신형이 바람을 지우며 치달았다.

‘쓰러트린다. 반드시.’

자무카가 품은 각오는 주인을 향한 사냥개의 충성심 따위가 아니었다.

아니, 그것은 처음부터 충성심이라 부를 수도 없었다.

마음에서 진정으로 우러나온 것이 아닌, 상대의 무력과 그의 목적이 맞물려 굴복이라는 결과를 낳았으니.

하지만 그것만으로도 충분했다.

비록 꾸며 내고 거짓된 충성이라 해도 북천마군은 확실한 대가를 약속했고, 암천(暗天)이 지닌 힘은 그를 초원의 왕이자 북방의 패자로 만들기에 충분했다.

그리고 바로 지금, 힘차게 내리그어지는 자무카의 일격은 그의 원대한 야망에 성큼 다가가고 있었다.

슈확.

느려진 세상 속, 제대로 된 반응조차 하지 못한 듯 여전히 북천마군과 대치 중인 적천강의 뒷모습은 무주공산(無主空山) 그 자체.

소리마저 앞질러 들이닥친 암녹색 강기가 자무카의 눈동자를 물들였다.

‘끝났다.’

자무카는 마음속으로 확신했다.

이건 그 누구도 피할 수 없는 일격이라고.

설령 그 상대가 화왕 적천강이라는 거인이라 해도, 죽음이라는 결과는 달라지지 않는다고.

하지만 느낌표처럼 떠오른 그 확신이 물음표로 뒤바뀌는 데에는 고작 찰나의 시간만이 필요했을 뿐이었다.

화악.

불현듯 등 뒤에서 전해지는 끔찍한 열기.

그와 동시에 섬광처럼 뻗어 나온 누군가의 손끝이, 초원의 풍습에 따라 변발(辮髮)로 땋아 올린 자무카의 기다란 머리카락에 닿았다.

아니, 닿았다고 느낀 순간 그의 머리는 이미 뒤로 젖혀지고 있었다.

덥석.

우악스러운 힘으로 머리카락을 잡아채는 손길. 동시에 젖혀진 상반신을 따라 본래의 궤적을 잃고 휘청이는 곡도.

순간 엄습하는 고통과 경악 속에서, 자무카는 문득 깨달았다.

이토록 위협적인 상황 속에서 적천강이 고개조차 돌리지 않았던 이유를.

‘반응하지 못했던 것이 아니었어.’

틀림없다.

적천강은 처음부터 알고 있었다.

아니, 믿고 있었다.

자신의 하나뿐인 제자를.

세월로는 판별할 수 없는, 제자의 신위(神威)를.

쉭!

적천강의 머리 위를 아슬아슬하게 스쳐, 텅 빈 허공을 베어 가르는 암녹색 강기.

고통과 아쉬움으로 이를 악문 자무카의 귓가로, 나직한 음성이 닿았다.

“머리 예쁘게 땋았네.”

“……!”

“딱 뜯어내기 좋게.”

우직, 콰드득!

순간, 자무카의 눈앞이 새하얗게 물들었다.

머리카락과 두피가 통째로 뜯겨 나가는 격통에 소리 없는 비명을 내지른 그는 신형을 돌려세우며 곡도를 휘둘렀다.

후우웅!

엄청난 고통 속에서도 꺼지지 않은, 아니 오히려 더욱 거세게 솟구친 암녹색 강기가 공간을 찢어발겼다.

반세기가 넘는 세월에 걸쳐 완성한 극쾌의 도법.

그러나 자무카는 까맣게 몰랐다.

정확히는, 예상조차 할 수 없었다.

섬광과도 같은 일격으로 광활한 초원을 평정한 그의 힘과 속도가, 진태경이 지난 이 년간 끊임없이 사선(死線)을 넘나들며 얻은 깨달음과 보상보다 뒤떨어진다는 것을.

퍼엉!

화염신장(火焰神掌).

찰나의 순간 공기마저 불사르며 들이닥친 그 강대한 화염에 자무카의 상반신이 들썩였다. 상상할 수도 없던 열기가 전신의 혈도를 불사르고 헤집었다.

‘아.’

아득해진 시야 속, 자무카는 단전 깊숙한 곳에서 울컥 솟구치는 핏물을 삼켰다.

하지만 동시에, 이 끔찍하리만치 강한 일격을 허용하고도 아직 사그라지지 않은 희망의 불씨를 느낄 수 있었다.

잠력단.

끊임없이 샘솟는 힘의 원천.

진작 허물어지고도 남았을 자무카의 전신을 지탱하는 생명력의 근원.

‘아직, 아직……!’

자무카는 이를 악물었다.

온 힘을 다해 손아귀에서 미끄러지려던 도파를 말아쥐고, 진태경의 가슴을 향해 내리찍었다.

카득, 퍼걱!

허공에서 뒤섞이는 상반된 두 줄기의 소음.

그리고.

“아, 더럽게 아프네.”

검붉은 핏물을 뒤집어쓴 채 고통 어린 신음을 토해 내는 진태경의 모습을 바라보며, 자무카는 목소리를 쥐어짜 냈다.

“어떻, 게.”

개울가의 징검다리처럼 군데군데 끊어진 음성.

이해할 수 없었다.

다른 모든 것을 떠나 진심으로 묻고 싶었다.

어떻게 이 일격을 막을 수 있었는지.

도대체 무슨 조화를 부렸기에, 조금 전까지만 하더라도 넝마가 된 옷자락 사이로 비치던 맨살 위에 붉은빛이 도는 갑옷이 나타난 것인지.

“이건. 쿨럭, 이건 말도…….”

콰드득.

소리 없는 비명과 함께 흩어지는 목소리.

마치 갈고리처럼 자무카의 옆구리에 쑤셔 박은 다섯 개의 손가락을 비틀며, 진태경이 피곤한 얼굴로 대답했다.

“서로 쉽게 쉽게 가면 되지, 왜 끈질기게 버티고 그러냐. 이건 나중에 쓰려고 아껴 뒀던 건데.”

무슨 말일까.

어찌 이런 일이 가능한 것일까.

해결되지 못한 의문과 함께, 자무카는 홀린 듯이 손아귀에 힘을 주었다.

파도처럼 넘실거리던 강기도, 예리하기 그지없던 도신도 이제는 온통 꺼지고 무뎌졌다는 사실도 잊은 채.

그극. 철그렁.

끝끝내 화룡갑(火龍甲)을 뚫지 못한 곡도가 주인의 미련을 대신하듯 갑옷의 표면을 긁으며 손에서 미끄러진 그 순간.

퍼엉.

다시 한번 터져 나온 화염신장의 열기와 함께, 자무카는 자신의 몸속 깊숙한 곳에서 울려 퍼진 폭발음을 들을 수 있었다.

“커……헉!”

아득하게 물드는 시야. 먹먹해진 귓가.

남의 것처럼 낯설다.

수백 리 밖에서 지켜보는 것처럼 멀게만 느껴졌다.

입술 사이로 흘러나오는 핏물의 뜨거움도, 북천마군의 것이 분명한 외침도.

그럼에도 불구하고 단 한 가지.

전신을 끊임없이 두드리고 부수는 손길만이 선명했다.

펑. 펑. 퍼어엉.

자무카의 신형이 휘청였다. 무시무시한 힘에 휩쓸리면서도 뒷걸음질조차 칠 수 없었다.

영혼이 새하얗게 불타는 듯한 격통 속.

옆구리에 틀어박힌 다섯 개의 손가락이 그의 몸뚱어리를 갈고리처럼 옭아매고 있었다.

하나하나가 가공할 만한 위력을 지닌 일권(一拳), 일장(一掌)이 그의 시야를 뒤덮으며 청백색의 소나기가 되어 쏟아지고 있었다.

잠력단으로부터 비롯된 모든 것이 힘을 다할 때까지.

영원히 샘솟을 것만 같던, 그 거대한 기운의 바다가 메마를 때까지.

그리고 어느 순간, 자무카는 더 이상의 고통이 느껴지지 않는다는 것을 깨달았다.

털썩.

가을 끝자락에 떨어지는 낙엽처럼, 자무카는 허물어졌다.

힘없이 위를 향해 움직인 그의 눈동자에는 끝없이 펼쳐진 어두컴컴한 밤하늘이, 거인처럼 우뚝 선 진태경의 모습이 비치고 있었다.

‘너는, 너는…….’

도대체 무엇이냐.

미처 머릿속에서 완성되지 못한 한 줄기 생각과 함께, 자무카의 세상이 기울었다.

털썩.

아지랑이처럼 피어오르는 열기 속, 까맣게 그을린 채 숨이 끊어진 초원의 왕을 내려다보던 진태경이 참았던 숨을 내뱉었다.

후우.

나직하게 흘러나오는 숨결.

그러나 막대한 공력이 실린 일격을 연달아 쏟아부었음에도, 하얗게 질려 있던 그의 입술은 불그스름하게 달아오르고 있었다.

마치 시간을 역행하는 것처럼.

소진되고, 닳아 없어졌던 모든 것을 원래대로 되돌리는 것처럼.

띠링. 띠링. 띠링.



- [Lv.173 자무카]를 처치하셨습니다!

- 막대한 경험치를 획득하셨습니다!

- 막대한 명성치를 획득하셨습니다!

- 당신의 명성이 [대초원]을 떨어 울립니다!

.

.

.

오직 한 사람의 귓가에만 울려 퍼지는 맑은 종소리와 함께 허공을 물들이는 반투명한 글자들.

그 끝에, 누군가가 그토록 기다렸던 세 글자가 있었다.



- 레벨 업!



“이제야 좀 살맛 나네.”

제때 찾아온 행운을 전신으로 느끼며, 진태경은 잘게 몸을 떨었다.

그리고 태산처럼 굳건하게 버티고 선 적천강의 어깨너머, 눈을 부릅뜬 채 이곳을 바라보는 북천마군을 향해 웃어 보였다.

“둘이었는데, 이제 혼자네?”

으득.

부서질 듯이 이를 악문 북천마군이, 온 힘을 다해 적천강을 밀어 냈다.

콰드득! 쾅!

거대한 힘의 충돌과 함께, 서로 다른 방향을 향해 튕겨 나가는 두 개의 신형.

충격파를 상쇄하는 대신 오히려 속도를 더해 물러나는 북천마군의 모습에, 그 의도를 즉시 간파한 적천강이 일갈을 내질렀다.

“놈-!”

그러나 북천마군은 멈추지 않았다.

바람을 가르고 공간을 지워 내며, 비좁은 협곡의 출구를 향해 쏘아졌다.

쐐애애액! 쾅!

협곡 곳곳을 메운 거대한 암석들이 가볍게 내지른 일권에 박살 난다. 빈틈없이 앞을 가로막은 장애물과 막강한 충돌의 여파로 나아가지 못하고 있던 산서인들을 향해, 북천마군은 창을 뻗었다.

고오옹.

일그러지는 공간. 그 중심에서 불길하리만치 눈부신 섬광을 토해 내는 창날.

그러나 미증유의 기운이 실린 그 일격이 산서인들을 휩쓰는 일은 벌어지지 않았다.

슈확!

거대한 빛의 화살이, 허공을 가르며 북천마군을 향해 내리꽂혔다.
```

## Final English reading copy

```markdown
# Chapter 975

No matter how well trained a hunting dog was, it couldn’t take down a predator on its own.

The difference in what they were born to be was unavoidable.

But Jamukha was different. Born a predator, he had become a hunting dog to achieve his own ends.

He was a trained beast.

He possessed both the strength of a predator who could face any enemy and the loyalty of a hunting dog.

That was why, the moment he heard his master call, he could throw himself into action without a second’s hesitation.

“Jamukha!”

The signal he’d been waiting for came, and Jamukha immediately unleashed his curved blade with all his might.

*BOOM!*

Two waves of Force collided in midair.

The dark green Force of his blade, made darker and larger by the effects of the Temporary Strength Pill, pushed back the blue-white flames, if only for a moment. Just then, Jamukha’s foot shot forward like an arrow.

*Whoosh.*

His figure blurred in an instant.

With Shifting Form and Position, unleashed in the space of a heartbeat, Jamukha became a streak of wind and crossed more than a dozen *zhang*.

He was heading for the Fire King—a predator more ferocious and powerful than any quarry he’d ever faced.

*One strike. One strike is all it takes.*

Near-certainty filled Jamukha’s movements, and it was no baseless boast.

For more than fifty years, he had pursued nothing but the utmost speed, honing his martial arts to counter the Hebei Peng Family’s overbearing style.

Jamukha had no doubt that even Jin Taekyung, called the Divine Dragon, had his limits. He couldn’t make up for the difference of all those long years.

And besides…

*With this power, I can do anything.*

Everything had changed. It was as if he’d shed a layer and been reborn like a caterpillar emerging as a butterfly. The whole world looked new.

His feet, skimming over the ground, and the beloved weapon gripped in both hands felt lighter than ever.

The Temporary Strength Pill had drawn out every ounce of his power and then some. Even now, it seethed ceaselessly in the depths of his body.

His sixth sense, opened beyond the five, let him easily evade even a single streak of flame striking from behind.

*Shweeeee!*

Jamukha increased his speed and turned his head. A spearhead that had left Jin Taekyung’s hand tore through the air, grazed the back of his neck, and buried itself in the cliff face.

*KABOOM!*

Sharp fragments of rock flew in every direction. Jamukha leaped over the rising cloud of dust, his figure rushing onward as if erasing the wind itself.

*I’ll bring him down. No matter what.*

The resolve in Jamukha’s heart wasn’t the loyalty of a hunting dog toward its master.

No—he couldn’t have called it loyalty from the start.

It hadn’t come from his heart. The other man’s strength and his own ambitions had simply combined to force him into submission.

But that was enough.

Even if his loyalty was false and feigned, the North Heaven Demon Lord had promised him a sure reward. The power of Dark Heaven was enough to make him king of the steppe and ruler of the north.

And right now, Jamukha’s mighty downward slash was bringing him one step closer to his grand ambition.

*Shwack.*

In the slowed world, Jeok Cheongang’s back remained turned to him, as if he couldn’t even react. Still facing the North Heaven Demon Lord, the old man was utterly exposed.

Dark green Force, arriving before its own sound, filled Jamukha’s eyes.

*It’s over.*

Jamukha was certain of it.

No one could dodge this strike.

Even if his opponent was the giant known as the Fire King, Jeok Cheongang, the outcome would be the same: death.

But it took only a heartbeat for that certainty, which had appeared like an exclamation point, to turn into a question mark.

*Fwoosh.*

A terrible heat suddenly washed over him from behind.

At the same time, someone’s fingertips flashed out and touched Jamukha’s long hair, braided into a queue in the custom of the steppe.

No—by the time he felt them touch, his head was already being wrenched backward.

*Grab.*

A hand seized his hair with brutal force. His upper body bent backward, and the curved blade in his grip wavered off its original course.

Amid the sudden pain and shock, Jamukha finally understood why Jeok Cheongang hadn’t even turned his head in the face of such danger.

*He wasn’t unable to react.*

No doubt about it.

Jeok Cheongang had known from the beginning.

No—he’d trusted him.

His one and only Disciple.

His Disciple’s might, something no number of years could measure.

*Whoosh!*

The dark green Force skimmed past Jeok Cheongang’s head by a hair and slashed through empty air.

A quiet voice reached Jamukha’s ear as he clenched his teeth against the pain and frustration.

“Nice braid.”

“……!”

“Looks easy to rip right off.”

*Krrk, krrrunch!*

The world before Jamukha’s eyes turned white.

The pain of having his hair and scalp torn off together drew a silent scream from him. He spun around and swung his curved blade.

*Whoooosh!*

The dark green Force hadn’t died out despite his terrible pain. If anything, it surged even more fiercely, tearing through space.

A blade technique perfected over more than half a century, its speed unsurpassed.

But Jamukha had no idea.

More precisely, he could never have anticipated it.

That the strength and speed with which he’d subdued the vast steppe in a flash were inferior to the enlightenment and rewards Jin Taekyung had gained over the past two years, constantly crossing the line between life and death.

*Poom!*

Flame Divine Palm.

The tremendous blaze swept in at that instant, burning even the air. Jamukha’s upper body lurched. Heat beyond anything he could imagine burned through and ravaged the acupoints all over his body.

*Ah.*

Through his fading vision, Jamukha swallowed the blood surging up from deep in his dantian.

But even as he endured that horrifically powerful strike, he could still feel a spark of hope that hadn’t gone out.

The Temporary Strength Pill.

An inexhaustible source of power.

The wellspring of vitality keeping Jamukha’s body upright, though it should have already crumpled.

*Not yet. Not yet…!*

Jamukha gritted his teeth.

With all his might, he tightened his grip around the hilt as it began to slip from his hand and drove the blade toward Jin Taekyung’s chest.

*Ka-drrk, crack!*

Two opposing sounds mingled in midair.

And then—

“Ah, that hurt like hell.”

Looking at Jin Taekyung, who was drenched in dark red blood and groaning in pain, Jamukha forced out a question.

“How…?”

His voice broke apart like stepping-stones in a stream.

He couldn’t understand it.

Setting everything else aside, he genuinely wanted to know.

How had Jin Taekyung blocked that strike?

What kind of sorcery had he used to make a red-tinged suit of armor appear over the bare skin that had been showing through his tattered clothes just moments ago?

“This… *cough*, this doesn’t make—”

*Krrrunch.*

His voice scattered with a silent scream.

Twisting the five fingers he’d driven hooklike into Jamukha’s flank, Jin Taekyung answered with a tired expression.

“Why don’t we both make this easy and get it over with? Why are you so damn stubborn? I was saving this for later.”

What did he mean?

How was any of this possible?

With his unanswered questions, Jamukha tightened his grip as if in a daze.

He’d forgotten that the Force, once surging like waves, and the blade, once so razor-sharp, had both dulled and died away.

*Scrape. Clang.*

At last, the curved blade failed to pierce Fire Dragon Armor. It scraped across the armor’s surface, as if giving voice to its owner’s regret, then slipped from his hand.

*Poom.*

With another burst of heat from Flame Divine Palm, Jamukha heard an explosion reverberate from deep within his body.

“Guh—!”

His vision dimmed. His ears went muffled.

Everything felt strange, as if it belonged to someone else.

It seemed so far away, like he was watching from hundreds of miles off.

The heat of blood spilling from his lips. The shouts that could only belong to the North Heaven Demon Lord.

And yet one thing remained vivid.

The blows that kept pounding and breaking his body.

*Poom. Poom. Pooom.*

Jamukha’s figure staggered. Even as he was battered by terrifying force, he couldn’t even step back.

Amid pain so intense it felt as if his soul were burning white, the five fingers buried in his flank held his body fast like a hook.

One punch, one palm strike—each carrying terrifying power—filled his vision, raining down in a blue-white torrent.

They kept coming until everything the Temporary Strength Pill had given him was spent.

Until the vast sea of power, which had seemed as if it would spring forth forever, had dried up.

And at some point, Jamukha realized he couldn’t feel any more pain.

*Thud.*

Like a leaf falling at the end of autumn, Jamukha crumpled.

His eyes weakly rolled upward. Reflected in them were the endless, dark night sky and Jin Taekyung, standing tall as a giant.

*You… What are…*

What are you?

With that unfinished thought, Jamukha’s world tilted.

*Thud.*

The heat rose like a wavering haze. Jin Taekyung looked down at the King of the Steppe, blackened and lifeless, then let out a breath he’d been holding.

*Hoo.*

A quiet sigh.

But despite unleashing one powerful strike after another, each infused with tremendous internal energy, his lips, which had gone white, were beginning to flush red.

As if time were running backward.

As if everything that had been spent and worn away were returning to its original state.

*Ding. Ding. Ding.*

> **System**
>
> You have defeated Lv. 173 Jamukha!
>
> You have gained a tremendous amount of EXP!
>
> You have gained a tremendous amount of Fame!
>
> Your Fame makes the Great Steppe tremble!
>
> .
>
> .
>
> .

Clear chimes rang in only one person’s ears as translucent letters filled the air.

At the end of them were the words he’d been waiting for so long.

> **System**
>
> Level Up!

“Now I’m finally feeling alive.”

Feeling the well-timed stroke of luck through his whole body, Jin Taekyung trembled.

Then, over Jeok Cheongang’s shoulder, standing firm as Mount Taishan, he smiled at the North Heaven Demon Lord, who was staring at him with wide eyes.

“There were two of you. Now you’re alone.”

*Crack.*

The North Heaven Demon Lord clenched his teeth hard enough to break them, then forced Jeok Cheongang back with all his might.

*Krrrunch! Bang!*

With a tremendous clash of power, the two figures were flung in opposite directions.

Rather than slow himself to absorb the shock wave, the North Heaven Demon Lord used it to speed up his retreat. Jeok Cheongang immediately saw through his intent and shouted.

“You—!”

But the North Heaven Demon Lord didn’t stop.

He cut through the wind and seemed to erase the space around him as he shot toward the narrow gorge’s exit.

*Shweeeee! Boom!*

The massive rocks filling the gorge shattered with a casually thrown punch. Then, toward the people of Shanxi who were unable to advance because obstacles blocked their way at every turn and the force of the collisions kept them pinned down, the North Heaven Demon Lord thrust out his spear.

*Rrrrrum.*

Space warped. At its center, the spearhead gave off a blindingly ominous flash.

But that strike, carrying an unprecedented force, never swept across the people of Shanxi.

*Shwack!*

A gigantic arrow of light tore through the air and plunged toward the North Heaven Demon Lord.
```
