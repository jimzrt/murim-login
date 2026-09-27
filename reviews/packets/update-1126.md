<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1126.txt",
      "sha256": "a3f0220d5ef574256d7eb2d0a452b69b6b49323b343b04ded045377cc74147cc",
      "bytes": 13123
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5057a25156eb490206bae89dfca7714b273a8e24479a1ad465311e53b473ec61",
      "bytes": 1083
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "307189767337c5394589bdcaa7f59f3e28cdf1da9d380fecae4d63447025be4b",
      "bytes": 245178
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "dd684c2801b36e477b92080f10aeb4c9151f421e0e1b4ad5c48d2d0e16c7fea4",
      "bytes": 985
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "9d173ebac7d8dbe4d3484ecc19d3380c6ab1170f7866e2fd05800a2152f30707",
      "bytes": 1230
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3f56ae7ace4a67efce4e5d361f8a9a04b44e095f0b1e37668cb0dd6e9bbcb815",
      "bytes": 760
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ece5a063bc7eff519c13c1ab38752b1aec1fff8e98e95545e708f3af9049a3e3",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c1e4743a7aa42f0930fc3d916563126ee9efcc5f64242a5145699718f73ead19",
      "bytes": 623
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "9f8c70648e12b1050a416efb06f7e7d21ffdb87fdc880bd54d2581262416ed90",
      "bytes": 1084
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "8395cfd779fe9dda2184ebe8578acc8b05e235c7acadf3043954865c0b2bb51f",
      "bytes": 779
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "763993ee62ea44b84a02e2f082bcc4346296346d2f6820f6428e7134b40f8872",
      "bytes": 2461
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fbe26e0ec5f89ce57df0b052ec3ff3869882eaa7728f4db5939e2d5122fb744c",
      "bytes": 289919
    }
  ],
  "estimated_tokens": 11615
}
-->

# Durable State Update — Chapter 1126

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
1 and safe_through 1126. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1126. Profile updates may replace only one
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
  "chapter": 1126,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1126,
    "continuity_sources": [1126],
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
    "The Inner City battlefield remains under siege.",
    "The Blood Lord’s palm and body were pierced by White Flame, but Taekyung’s attack missed his heart when Taekyung’s internal energy ran out.",
    "The Blood Lord pulled out White Flame and now wields it.",
    "Jeok Cheongang and Cheongpung intervened to protect Taekyung, but the Blood Lord knocked them aside.",
    "The Blood Lord has crushed Taekyung’s wrist and legs and is choking him.",
    "Taekyung’s vision turned white, then red; the outcome is unresolved.",
    "The Blood Lord intends to kill Taekyung; he resented the Lord of Heaven’s attention to Taekyung and the apparent disregard for the servants’ welfare."
  ],
  "continuity_sources": [
    1125
  ],
  "open_questions": [
    "What happens as Taekyung’s vision turns red?",
    "Can Taekyung survive the Blood Lord’s attack?",
    "Can Jeok Cheongang or Cheongpung continue fighting?",
    "Will the Blood Lord retain White Flame?"
  ],
  "safe_through": 1125,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 월화     | **Wolhwa**         |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 감숙     | **Gansu**              |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 천하제일검 | **Number One Sword Under Heaven** | Mae Jonghak's title. |
| 황하 | **Yellow River** | River along which civilization began. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 매종학 | 혈주 | legendary_martial_master_to_enemy | you | cold and judgmental | After revealing himself, Mae Jonghak condemns the Blood Lord's accumulated sins and orders him to pay the price. |
| 혈주 | 매종학 | enemy_to_revealed_legendary_master | you | shocked and hostile | The Blood Lord addresses Mae Jonghak with 당신 immediately after recognizing him as the Sword Saint. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 결사대 | commander_to_subordinates | you bastards | blunt and commanding | Jin orders the suicide squad to exploit the opening and wipe out the surrounding monsters. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1125
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality; after killing the Grand Mage, he claims command of the Dark Heaven army.
- **Personality:** Cunning and controlling, he trusts his overwhelming power and relishes opponents who survive and resist him; he resents the Lord of Heaven’s attention to Taekyung and rationalizes his intended murder as loyalty, yet believes his choice is right.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He has served the Lord of Heaven but now openly defies his will; he is fixated on killing Jin Taekyung, killed the Grand Mage, and recognizes Cheongpung from his connection to Sword Saint Mae Jonghak.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1125
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1125
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1125
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1125
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1110
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 1115
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 1016
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch with authority to mobilize more than thirty Shanxi branches; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Wolhwa says she likes Taekyung, whose family she supports through a mutually beneficial alliance with Jin Wikyung, and has sent him an unusually affectionate personal missive alongside her professional intelligence.

## Korean source

```text
＃1126화



그것은 아주 낮고 희미한, 평소였다면 누구도 신경 쓰지 않을 소음이었다.

지금 이 순간에도 쉴 새 없이 천지를 떨어 울리는 전장의 그것에 비하면 아무것도 아닌.

그저 어딘가를 스쳐 지나가는 바람과도 같은 소리.

그러나 또 다른 누군가에게 있어, 그것은 불현듯 들이닥친 폭풍이자 막을 수 없는 낙뢰(落雷)와도 같았다.

서걱.

뒤늦게 귓가를 파고든 그 서늘한 절삭음에, 혈주는 자신도 모르게 입술을 달싹였다.

“……어?”

조금 전까지 환희로 물들어 있던 그의 눈동자에는 어느새 짙은 의문이 떠올라 있었다.

어느샌가 자신의 팔을 가로지른, 한 줄기의 미세한 실선을 비추고 있는 핏빛 동공 역시도.

하지만 혈주가 그 의문에 대한 답을 찾기도 전, 살갗 사이로 몽글몽글 피어오른 핏물이 실선을 따라 질주했다.

푸화아아악!

솟구치는 피 분수 속, 혈주는 부릅뜬 눈으로 바라볼 수밖에 없었다.

자욱한 핏물을 흩뿌리며 떨어져 나가는 자신의 팔을.

이 죽음의 끝자락에서 가까스로 목숨을 건진 채, 잘려 나간 팔과 함께 쓰러지는 누군가의 모습을.

철퍽!

이미 불구나 다름없는 진태경의 몸뚱어리가 힘없이 허물어진 그 순간, 멈춰 있던 시간이 흐르기 시작했다.

그러나 그토록 죽이고 싶었던 상대가 발치에 쓰러져 있음에도, 혈주는 제자리에서 움직이지 못했다.

아니, 일순간 움직임을 멈춘 것은 비단 그뿐만이 아니었다.

깊은 피 웅덩이에 잠긴 채, 죽음과 맞닥트린 자신의 제자를 향해 떨리는 손끝을 내뻗던 스승도.

마침내 두 기의 흑귀를 비롯한 무수한 적들을 떨쳐내고, 찰나의 시간을 쪼개며 쇄도하던 궁성과 살성도.

이제는 고작 한 뼘밖에 남지 않은 검신을 지면 깊숙이 박으며, 억지로 몸을 일으켜 세우던 청풍도.

그들 모두는 느꼈고, 동시에 보았다.

공간을 가로막은 비바람의 장막 너머, 흐릿하게 일렁이는 누군가의 인영(人影)을.

솨아아아.

하염없이 쏟아지는 빗줄기 사이로 발걸음을 옮기는, 흑의인(黑衣人)의 손끝을 따라 불현듯 내리그어진 고색창연한 은빛 검신을.

스아악.

동시에. 세상이 갈라졌다.

비와 바람이.

그 안에 스며 있는 공기와 기운이.

그리고, 어둠이.

슈확!

모두의 동공을 물들인 그 휘황한 섬광은 노을보다 짙고, 여명만큼이나 눈부셨다.

지금까지도 혈주의 뇌리에 낙인처럼 아로새겨진 일 년 전의 그 날, 그때처럼.

‘이건.’

시간을 쪼개고 쪼갠 찰나의 순간, 눈을 부릅뜬 채 굳어 버린 혈주의 머릿속에 누군가의 존재가 스쳐 지나갔다.

오늘 이 자리에 나타날 수도, 나타나서도 안 되는 그 이름이.

검으로는 비견할 자가 없기에 천하제일검(天下第一劍)이요.

그 경지가 비로소 하늘에 닿았기에, 검성(劍星)이라 불리는 그가.

“매종학-!”

혈주의 입술 사이로 비명과도 같은 외침이 터져 나온 그 순간.

화아악.

거대하게 부풀어 오른 섬광 속, 수십 갈래로 나뉜 자줏빛 강기가 만개(滿開)하고.

툭.

눈부시게 흩날리는 강기의 꽃잎 아래, 불현듯 내뻗어진 한 사람의 손끝이 혈주의 발치에 닿았다.

아니.

콰득!

황급히 돌아서려는 괴물의 발목을, 온 힘을 다해 움켜쥐었다.

숭산(嵩山)이 피로 물들었던 그 날처럼.

“……!”

일순간 부릅떠진 괴물의 핏빛 동공에, 흐릿하게 웃고 있는 청년의 얼굴이 비쳤다.

마침내 눈앞까지 들이닥친, 자줏빛 섬광도 함께.

콰아아아아!



* * *



고통을 느끼지 못한다는 것은 저주인 동시에 절망이다.

고통이야말로 살아 숨 쉬고 있다는 증거니까.

살아있는 이가 그러한 고통을 느끼지 못한다는 것은, 죽음이 임박했다는 뜻이니까.

하지만 그것은 동전의 일면에 지나지 않는다.

이미 눈앞에 가까워지는 죽음을 직시하고, 마음속 깊이 그 현실을 받아들인 누군가에게는 저주가 아닌 마지막 축복일 수도 있다.

아니, 분명 그럴 것이다.

적어도 지금 이 순간, 진태경은 고통을 느끼지 못한다는 것에 그 어느 때보다 감사하고 있으니까.

두 다리가 으스러져도, 한쪽 팔이 산산조각이 났어도 움직일 수 있다는 사실에 눈물이 나올 만큼 기뻤으니까.

콰득!

도대체 어디서 그런 힘이 솟아난 걸까.

진태경 자신조차도 알 수 없었다.

다만 무언가에 조종이라도 당한 것처럼 홀린 듯 손을 뻗었고, 사지 중 유일하게 망가지지 않은 그것에 담긴 힘은 괴물의 발걸음을 저지할 만큼 강했을 뿐.

‘잡았……다.’

진태경은 웃었다.

흐릿한 시야 너머, 부릅뜬 눈으로 그를 내려다보는 혈주를 향해 입꼬리를 말아 올렸다.

그리고.

콰아아아아!

귓가를 후려치는 거대한 굉음을, 사방을 뒤흔드는 끔찍한 힘의 폭발을 느꼈다.

그와는 반대로 인적 드문 호숫가처럼 평온하게 가라앉은 마음도 함께.

‘이걸로 된 거야.’

시야를 짙게 물들인 섬광 속, 진태경은 조용히 뇌까렸다.

그래, 충분하다.

할 만큼 했고, 미련도 없다.

아니, 한 줌의 미련조차 없어야 한다.

조금이라도 미련이 남는다면 편안하게 떠날 수조차 없게 될 테니까.

보고 싶은 가족과 친구들의 이름을 부르짖고, 끝까지 해내지 못한 스스로를 자책하며 어린아이처럼 엉엉 울고 말 테니까.

하지만 이제는 괜찮다.

그가, 매종학이 와 주었으니.

무신(武神)이라는 하늘이 사라진 지금, 검성 매종학은 가장 높이 떠올라 있는 별이자 당대의 천하제일인(天下第一人)이었으니.

무림 맹주로서 책무를 다하여 중원을 지키고 있어야 할 그가 어찌 이곳에 나타날 수 있었는지, 문득 짐작이 가는 바가 있었으나 진태경은 굳이 생각을 이어 가지 않았다.

단지 이 생각지도 못한 구원자가, 눈앞의 괴물을 쓰러트리고 남은 이들을 살릴 수 있으리라는 희망에 감사할 뿐.

‘다행이야. 정말로.’

마음속 깊이 삼켜 낸 공허한 뇌까림과 함께, 진태경의 눈꺼풀이 감겨가던 그때였다.

우득!

잦아드는 굉음과 섬광 속, 벼락처럼 내뻗어진 누군가의 손이 그의 목줄기를 움켜쥔 것은.

툭, 투두둑.

진태경의 이마를 적시며 떨어져 내리는 뜨겁고 끈적한 액체.

그 위에서는, 아직 꺼지지 않은 괴물의 핏빛 안광이 번뜩이고 있었다.

“감히…… 쿨럭, 네놈 따위가.”

혈주는 상처 입은 맹수처럼 으르렁거렸다.

비록 저 한마디를 내뱉기 위해 몇 움큼이나 되는 핏물을 삼켜야만 했고, 전신 곳곳에는 뼈가 드러날 정도의 극심한 상처가 아로새겨져 있었으나 그는 여전히 살아 있었다.

그리고 죽어 가는 사냥감을 전리품처럼 들어 올리며, 재차 피에 젖은 이빨을 들이밀었다.

“나를, 그분의 강대한 권능을 이어받은 이 몸을 쓰러트릴 수 있을 것 같더냐.”

바로 그 순간이었다.

강하게 옥죄어오는 손아귀의 힘에 새하얗게 질려 가던 입술 사이로, 한 줄기의 희미한 음성이 흘러나온 것은.

“그래. 이 개자식아.”

“……뭐?”

“충분히 그럴 것 같다고.”

진태경은 흐릿하게 웃었다.

말없이 자신을 바라보는 혈주를 향해, 어느샌가 파르르 떨리고 있는 그 핏빛 동공을 향해.

동시에 알 수 있었다.

그 떨림에 담겨 있는 감정은, 분노만이 아니라는 사실을.

“두렵지? 지금 이 상황이.”

“……네놈.”

“그래, 아무리 너 같은 새끼라도 두려울 수밖에 없겠지. 그러니 이런 싸구려 인질극이나 벌이고 있는 거고.”

그 순간.

으득.

혈주는 자신도 모르게 이를 악물었다.

싸구려 인질극이라니.

말도 안 되는 개소리다.

아니, 분명 그래야 했다.

하지만 어째서일까.

혈주는 대답하지 못했고, 오히려 손아귀에 실려 있던 힘이 느슨해졌다.

그리고 그런 그의 귓가로, 조소 섞인 진태경의 음성이 흘러들었다.

“주위를 둘러봐. 그럼 지금의 네 모습이 사냥꾼인지, 사냥감인지 알 수 있을 테니.”

혈주는 대답하지도, 진태경의 말을 따라 주위를 둘러보지도 않았다.

정확히는, 차마 그럴 수 없었다는 것이 옳은 표현이었을 것이다.

어느덧 자신이 검성을 주축으로 한 다섯 명의 초절정 고수에게 포위당했다는 현실을.

그와 더불어 그들의 발걸음을 잠시나마 묶고, 시간을 벌기 위해 진태경을 붙잡았다는 진실을 스스로 인정하고 싶지 않았으니까.

‘이대로라면…… 죽는다.’

피부로 느껴진다. 본능적으로 깨달았다.

믿고 싶지도, 믿을 수도 없는 그 잔인한 사실이 혈주의 폐부를 찌르고 있었다.

‘도대체 어째서.’

혈주로서는 도저히 알 수 없었다.

위대한 주인으로부터 부여받은 권능이, 어찌하여 한 순간에 자신을 떠나갔는지.

사라졌다. 송두리째.

불사(不死)라 칭해도 부족하지 않던 치유력도, 피를 원료 삼아 끝없이 솟구치던 기운도.

다만 그 모든 것이 사라진 뒤에도 남아 있던 힘의 잔재만이 그를 지탱하고 있을 뿐이었다.

‘하지만, 나는 결코 죽지 않을 것이다.’

혈주는 수치심으로 잘게 떨리는 입술을 깨물었다.

아직 그에게 남아 있는 마지막 희망을, 이 끔찍하고도 거대했던 전투의 종지부를 내리찍을 최후의 철퇴를 떠올리며.

“똑똑히 지켜보아라. 오늘 이 자리에서 살아남는 것이 누구인지.”

여전히 웃고 있는 진태경을 향해 혈주가 씹어뱉듯이 뇌까린 그 순간.

부우우우!

전장을 뒤흔드는 힘찬 나팔 소리와 함께, 혈주가 그토록 기다렸던 희망이 마침내 모습을 드러냈다.

드드드드득!

땅을 뒤흔드는 무수한 발걸음에 이어, 하늘을 찌를 듯 힘차게 휘둘려지는 거대한 깃발들.

각양각색의 복색을 한 수만 명의 대군과, 그들의 머리 위로 흩날리는 두 개의 깃발에 적힌 글씨가 모두의 눈동자에 선명히 틀어박혔다.

장강수로맹(長江水路盟).

그리고, 녹림맹(綠林盟).

“……!”

“……!”

일순간, 보이지 않는 격동이 전장을 휩쓸었다.

“아. 아아.”

죽을 힘을 다해 침략자들과 맞서 싸우던 결사대와 백성들은 석상처럼 굳었고. 

“천주시여!”

압도적인 숫자를 바탕으로 펼쳐진 반격에도 팽팽한 전세를 유지하던 암천의 광신도들은 홀린 듯이 천주를 찬양하는 여덟 글자의 교언(敎言)을 읊었다.

환희에 어린 눈빛으로 그 광경을 바라보고 있는 혈주처럼.

“천상천하, 만마앙복……!”

등골을 타고 흘러내리는 전율과 함께, 혈주는 진태경을 향해 시선을 옮겼다.

절망에 빠져 있을 그의 모습을 조금이라도 빨리, 더 오래 지켜볼 수 있도록.

그리고 다음 순간 불현듯 깨달았다.

무언가 잘못되었다는 것을.

자신의 마지막 희망이, 어쩌면 절망이었을지도 모른다는 사실을.

“하청지회(河淸之會).”

“뭐……라고?”

“누가 나한테 그런 서신을 보냈었지. 황하가 맑아질 때를 기다리고 있겠다고. 그때 다시 만나자고.”

진태경은 떠올렸다. 감숙성에 머무를 당시, 월화가 보냈던 한 통의 서신을.

까마득히 잊고 있던 그 한 줄짜리 서신을.



언젠가 하청지회 할 수 있기를 바라며, 월화.



그 어느 때보다 환한 웃음을 머금은 채, 진태경은 파르르 떨리는 손을 들어 동쪽을 가리켰다.

“아무래도, 지금이 그때인가보다.”

정확히는, 선두에 선 두 개의 깃발 뒤로 서서히 몸을 일으켜 세우는 또 하나의 거대한 깃발을.

황하를 맑게 만들 만큼 쏟아져 내리는 무수한 빗줄기 사이로 드러난 세 글자를.

무림맹(武林盟).

“……!”

그리고 눈을 부릅뜬 채 멍하니 굳어 버린 혈주를 향해, 자신이 할 수 있는 마지막 한 수를 펼쳤다.

콰드득!

혈주는 막을 수 없었다.

맹수의 그것처럼 목덜미를 파고드는 진태경의 이빨을.

아득한 고통 속에서, 서서히 기울어지는 세상을.

철퍽.

모든 권능을 잃어버린 괴물의 몸뚱어리가, 마침내 피웅덩이 속에 처박혔다.
```

## Final English reading copy

```markdown
# Chapter 1126

It was a very low, faint noise—one no one would have paid attention to under ordinary circumstances.

Nothing compared to the incessant roar of the battlefield, which shook the heavens and earth even now.

Just the sound of wind brushing past somewhere.

But to someone else, it was a sudden storm, an unstoppable bolt of lightning.

*Shhk.*

At the cold slicing sound that belatedly pierced his ears, the Blood Lord’s lips moved before he knew it.

“……Huh?”

A moment ago, his eyes had been alight with joy. Now, a deep question had surfaced in them.

So had the blood-red pupils that reflected a fine line running across his arm.

But before the Blood Lord could find an answer, blood welled up through his skin and raced along that line.

*PSSSHHH!*

As a fountain of blood shot into the air, the Blood Lord could only stare, eyes wide, at his arm falling away in a spray of crimson.

And at the figure who, having barely escaped death, collapsed beside the severed limb.

*Splatter!*

The moment Jin Taekyung’s already-crippled body crumpled to the ground, time—which had stood still—began to move again.

Yet even with the man he had so desperately wanted to kill fallen at his feet, the Blood Lord couldn’t move.

No—he wasn’t the only one whose movements had stopped for an instant.

Jin Taekyung’s master, reaching a trembling hand toward his disciple, who lay in a deep pool of blood facing death.

The Bow Saint and the Slaughter Saint, who had finally shaken off countless enemies, including two Black Ghosts, and were hurtling forward, slicing through every fraction of an instant.

Cheongpung, driving the blade of his sword—now only a handspan long—deep into the ground as he forced himself upright.

They all felt it. And at the same time, they saw it.

Beyond the curtain of wind and rain blocking the space, a figure flickered faintly.

*Fwoosh.*

Amid the endless rain, an ancient silver blade suddenly swept down, following the fingertips of a black-clad figure walking through the storm.

*Shhhk.*

In that instant, the world split apart.

The rain and wind.

The air and energy that permeated them.

And the darkness.

*SHWAAK!*

The dazzling flash that filled everyone’s eyes was deeper than a sunset and as brilliant as dawn.

Just like that day a year ago, burned into the Blood Lord’s mind like a brand.

*This is…*

In a moment so brief it seemed time had been cut into slivers, the Blood Lord froze, eyes wide. Someone’s presence flashed through his mind.

A name that shouldn’t—or couldn’t—have appeared here today.

A man without peer when it came to the sword, and thus known as the Number One Sword Under Heaven.

A man whose realm had finally reached the heavens, and so was called the Sword Saint.

“Mae Jonghak—!”

The Blood Lord’s cry burst from his lips.

*FWOOSH!*

Within the enormous swelling flash, dozens of branches of purple Force blossomed.

*Tap.*

Beneath the dazzling petals of Force, a hand abruptly reached out and touched the Blood Lord’s foot.

No—

*KRAK!*

It seized the monster’s ankle with all its strength as he hurried to turn away.

Just like that day when Mount Song was stained with blood.

“……!”

In the monster’s blood-red eyes, suddenly wide, a young man’s faintly smiling face was reflected.

And the purple flash that had finally reached him.

*KWA-BOOOOM!*

* * *

Not being able to feel pain is both a curse and a despair.

Pain is proof that you’re alive and breathing.

For the living to feel no pain means death is close.

But that’s only one side of the coin.

For someone who has stared death in the face as it draws near and accepted that truth deep in their heart, it might not be a curse. It might be one last blessing.

No—it must be.

At least right now, Jin Taekyung was more grateful than ever that he couldn’t feel pain.

Even with both legs crushed and one arm shattered to pieces, he could still move. It made him so happy he could cry.

*KRAK!*

Where on earth had that strength come from?

Even Jin Taekyung didn’t know.

He’d reached out as if bewitched, as though something were controlling him. The strength in the only one of his four limbs that wasn’t broken had been enough to stop the monster in his tracks.

*I got him…*

Jin Taekyung smiled.

Through his blurred vision, he curled the corners of his mouth at the Blood Lord, who stared down at him with wide eyes.

And then—

*KWA-BOOOOM!*

He felt the enormous roar batter his ears, the dreadful explosion of power shaking everything around him.

At the same time, his heart had settled into a peaceful calm, like a deserted lakeshore.

*This is enough.*

Within the flash that had swallowed his vision, Jin Taekyung murmured to himself.

That was right. It was enough.

He’d done all he could, and he had no regrets.

No—not a single regret.

If even the smallest regret remained, he wouldn’t be able to leave in peace.

He’d cry like a child, calling out the names of the family and friends he wanted to see, blaming himself for failing to see things through.

But now, it was all right.

He had come. Mae Jonghak had come.

With the Martial God—the heavens—gone, the Sword Saint Mae Jonghak was the highest star in the sky and the greatest under heaven in this era.

Taekyung had a vague idea how Mae Jonghak, who should have been protecting the Central Plains by fulfilling his duties as Alliance Leader, could have appeared here. But he didn’t bother to follow the thought.

He was simply grateful for the hope that this unexpected savior could bring down the monster before them and save those who remained.

*Thank goodness. Really.*

Just as Jin Taekyung’s eyelids began to close, with that empty thought swallowed deep in his heart—

*CRACK!*

Amid the fading roar and flash, someone’s hand shot out like lightning and clamped around his throat.

*Drip. Drip.*

A hot, sticky liquid fell onto Jin Taekyung’s forehead.

Above him, the monster’s blood-red eyes still burned.

“How dare… *cough*… someone like you…”

The Blood Lord growled like a wounded beast.

He’d had to swallow mouthfuls of blood just to get those words out, and his body was covered in terrible wounds, some deep enough to expose bone. Yet he was still alive.

Lifting his dying prey like a trophy, he bared his bloodstained teeth again.

“Did you think you could defeat me—me, who inherited his mighty power?”

It was then.

Between Jin Taekyung’s lips, paling under the strength of the hand squeezing his throat, came a faint voice.

“Yeah. You piece of shit.”

“……What?”

“I think I can.”

Jin Taekyung smiled faintly.

At the Blood Lord, staring at him in silence. At those blood-red eyes, trembling ever so slightly.

At the same time, he understood.

There was more in that tremor than anger.

“You’re scared, aren’t you? Of what’s happening right now.”

“……You.”

“Yeah. Even a bastard like you has to be scared. That’s why you’re pulling this cheap hostage stunt.”

At that moment—

*Grind.*

The Blood Lord gritted his teeth without realizing it.

A cheap hostage stunt?

That was complete bullshit.

No—it had to be.

But why?

The Blood Lord couldn’t answer. Instead, the strength in his grasp loosened.

Taekyung’s voice, edged with mockery, drifted into his ear.

“Look around. Then you’ll see whether you’re the hunter right now—or the prey.”

The Blood Lord didn’t answer. He didn’t look around, either.

More precisely, he couldn’t bring himself to.

He didn’t want to admit that he was now surrounded by five Supreme Peak masters led by the Sword Saint.

And he didn’t want to acknowledge that he had grabbed Jin Taekyung to hold them back, if only for a moment, and buy himself time.

*At this rate… I’ll die.*

He could feel it in his skin. Instinct told him.

That cruel truth—something he didn’t want to believe and couldn’t believe—was stabbing into the Blood Lord’s heart.

*Why?*

The Blood Lord couldn’t understand it.

How could the power bestowed on him by his great master have left him in an instant?

It was gone. Every last bit.

The healing power that had been nearly worthy of the name *immortality*, the energy that had surged endlessly from blood.

Only the remnants of his power remained, just enough to keep him standing.

*But I will not die.*

The Blood Lord bit his lips, trembling with shame.

He thought of the last hope he still had—the final hammer blow that would bring this horrific, momentous battle to an end.

“Watch closely. You’ll see who survives here today.”

The Blood Lord muttered the words at Jin Taekyung, who was still smiling.

Then, at last, the hope he’d been waiting for appeared, accompanied by a powerful trumpet call that shook the battlefield.

*Bwoooooo!*

*Rumble, rumble, rumble!*

Countless footsteps shook the earth, followed by enormous flags waving high enough to pierce the sky.

Tens of thousands of troops in all manner of uniforms. The words inscribed on two flags fluttering above them struck everyone’s eyes.

Yangtze River Channel League.

And Green Forest Alliance.

“……!”

“……!”

An unseen shock swept through the battlefield.

“Ah. Ahhh…”

The suicide squad and civilians, who had fought the invaders with everything they had, froze like statues.

“Lord of Heaven!”

The Dark Heaven fanatics, who had kept the battle at a stalemate despite a counterattack backed by overwhelming numbers, chanted the eight-character invocation praising the Lord of Heaven as if entranced.

Just like the Blood Lord, who watched the scene with joy in his eyes.

“Heaven above, all demons bow…!”

A shiver ran down his spine as the Blood Lord turned his gaze toward Jin Taekyung.

He wanted to see the despair on Taekyung’s face as soon as possible—and for as long as possible.

Then, the Blood Lord suddenly realized.

Something was wrong.

That his last hope might have been despair all along.

“An auspicious meeting after the Yellow River runs clear.”

“What… did you say?”

“Someone once sent me a letter saying she’d wait until the Yellow River ran clear. That we’d meet again then.”

Jin Taekyung remembered a letter Wolhwa had sent while he was staying in Gansu.

A single line he’d long since forgotten.

*Hoping that one day, we can meet when the Yellow River runs clear,  
Wolhwa.*

Wearing his brightest smile yet, Jin Taekyung lifted his trembling hand and pointed east.

“Looks like this is the moment.”

More precisely, he pointed to another enormous flag slowly rising behind the two banners at the head of the army.

Through the countless streams of rain falling hard enough to clear the Yellow River, three characters came into view.

Murim Alliance.

“……!”

Then, facing the Blood Lord, who stood frozen, eyes wide, Taekyung played the last card he had.

*KRAK!*

The Blood Lord couldn’t stop him.

He couldn’t stop Jin Taekyung’s teeth from sinking into his neck like a beast’s.

Through the unbearable pain, the world slowly tilted.

*Splatter.*

The monster, stripped of all his power, finally crashed into the pool of blood.
```
