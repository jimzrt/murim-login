<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0959.txt",
      "sha256": "6402c42ee2edb4bada0ab93c833ee081b25c87de3db9824b431ff83cc6ec6db8",
      "bytes": 13280
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "737e386828b1b692c5274ab008efeb43313c7893b0a6517fd0efbc8a36a64a96",
      "bytes": 2048
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "20371f25af24d91e5b8a7c6910beb6b4a1e6fff660c4b2daeab3b43bcac6800c",
      "bytes": 234923
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "497bb468abfcc3cc2a8efec14258150aa68eb63d30767bcceb7a657e6cc41fe5",
      "bytes": 1007
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "0447e5fe0df94a00ed02050c4da4cfb5e16da53297662dc43a6645c2e111b591",
      "bytes": 659
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8c8a1c698d15f9ce51ecf3173ff5f33e4c5e6fd554b4fffd6a4c0fef9ff0198d",
      "bytes": 759
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "775205148e1ad09c0327b61de436100a0738a7c2e6e145900a06107767e30ade",
      "bytes": 874
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "3215c3fbb83ee591e5f4abb7baba483fbc792a0f30fc14a02f38ddabc0de2acd",
      "bytes": 1343
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "f96c721338280b628fb24ca8de24f327a81f0bcd2f4f57786d836484ac517b34",
      "bytes": 1119
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "b021ad74bd02628e1e7087a56418f7ec2281d6b8c3a235be9fbfed00bccadb13",
      "bytes": 1446
    },
    {
      "path": "characters/Temur.md",
      "sha256": "5598f90adc9086336331a2f5adfde93af3f067c81d8fd675ecab0c950c93dea5",
      "bytes": 676
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "d619b6802a19c5f5b8fbd50e9ae23810033fe681d9de123cb5226e4d16222856",
      "bytes": 954
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ae380d93c75553af72479e87151ad9e37a2657326197311b6ef472e0603f3571",
      "bytes": 268838
    }
  ],
  "estimated_tokens": 11760
}
-->

# Durable State Update — Chapter 959

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
1 and safe_through 959. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 959. Profile updates may replace only one
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
  "chapter": 959,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 959,
    "continuity_sources": [959],
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
    "The assault at Eight Spring Gorge remains unresolved; Jin Mukyung is fighting the Chinggen impostor.",
    "Jamukha has ordered the Keshik in the gorge to wear down the defenders while limiting further losses to his personal guard; three of his commanders of a hundred have died.",
    "Temur chose survival over loyalty and now recognizes with guilt that his actions have led his followers to slaughter; Jamukha has threatened him into obedience.",
    "The real Chinggen is dead; an impostor wearing his face continues to fight the Jin defenders.",
    "The Emperor remains gravely ill with Blood Soul Gu; saving him requires him to die once, and Taekyung’s effort to treat him remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "The Dongting Fisherman seeks revenge on Dark Heaven and owes the Jin Family of Taiyuan for saving his life twice.",
    "Taekyung resolved to trust his allies rather than bear every burden alone."
  ],
  "continuity_sources": [
    957,
    958
  ],
  "open_questions": [
    "How will the battle at Eight Spring Gorge end, and who will prevail in Jin Mukyung’s fight with the Chinggen impostor?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will become of Temur and the followers he led into the battle?"
  ],
  "safe_through": 958,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 철무백    | **Cheol Mubaek**   |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 일신     | **One God**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 역용술 | **disguise technique** | Technique used by the Third Fiend to conceal his identity. |
| 흑목조간 | **black-wood fishing rod** | The Dongting Fisherman's distinctive weapon; the broken rod is his only known trace. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 축골공 | **Bone-Shrinking Technique** | A martial art that stretches and shrinks bone and flesh to alter the user's appearance. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 케식 | **Keshik** | Elite warriors serving the Golden Clan. |
| 검귀 | **Sword Demon** | Title used for the kind of swordsman Mukyung is said to resemble. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 철무백 | 진위경 | sect_elder_to_lesser_family_head | Lesser Family Head | formal-deferential | Cheol Mubaek formally greets Jin Wikyung as the Lesser Family Head of the Jin Family of Taiyuan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 칭겐 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | The impostor wearing Chinggen’s face addresses Jamukha with deference. |
| 테무르 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | Temur affirms Chinggen’s public praise of Jamukha. |
| 진위경 | 동정어옹 | Younger ally addressing an older martial arts senior | Senior | Respectful | Jin Wikyung addresses him as 노 선배. |
| 동정어옹 | 진위경 | Older martial arts senior addressing a younger ally | you | Familiar and informal | He addresses Jin Wikyung as 자네. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 499
- **Aliases:** Tiger of Mount Heng
- **Role:** Cheol Mubaek is the ninth-generation successor of the Shura Annihilating Fist and the Peak master known as the Tiger of Mount Heng, now out of seclusion and active in the rebuilding of the Mount Heng Sword Sect.
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; considers Jin Taekyung, Jin Mukyung, and Hyuk Mujin Benefactors for protecting Seowol and enabling the Mount Heng Sword Sect's survival, and vows to repay them even at the cost of his life; feared and respected by the Mount Heng Sword Sect's senior figures

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 958
- **Aliases:** None
- **Role:** The real Chinggen, a Khan of the eastern grasslands and Temur’s sworn brother, is dead; the impostor wearing his face has reached Eight Spring Gorge and now fights Jin Mukyung.
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur was Chinggen’s cousin and sworn brother through the anda oath; an impostor wearing Chinggen’s face now accompanies Jamukha and deceives Temur.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 958
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 957
- **Aliases:** None
- **Role:** The Dongting Fisherman is an unaffiliated previous-generation Supreme Peak master whose water arts rival the Seafaring King; after recovering from severe injuries, he fights the Jin Family of Taiyuan’s enemies with his black-wood fishing rod.
- **Personality:** The Dongting Fisherman is fiercely confident and sardonic, and he is determined to repay the Jin Family of Taiyuan and avenge himself on Dark Heaven.
- **Voice:** He speaks in measured, old-fashioned phrasing, calling himself 노부 and using fishing metaphors in dry taunts.
- **Relationships:** The Dongting Fisherman owes the Jin Family of Taiyuan for restoring his mind and treating his severe injuries, and seeks revenge on Dark Heaven.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 958
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Peak-level swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and seeks strength in service of his family.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and Mukyung cherishes his promise to reunite with him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 957
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he can agonize over costly decisions but commits firmly once resolved.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and the people of Shanxi—including many commoners the Jin Family once aided—are willing to help defend their home alongside him.

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 946
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest; had fled from the steppe and commanded nearly four hundred subordinates before his death
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 958
- **Aliases:** None
- **Role:** Temur is a Khan of the northern grasslands, ruling alongside Chinggen over tens of thousands of horses and warriors.
- **Personality:** Hot-tempered and proud of his khan lineage, Temur chose survival over loyalty and now recognizes with guilt that his actions have led his followers to slaughter.
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** The real Chinggen was Temur’s cousin and sworn brother through the anda oath, but he was killed; an impostor wearing Chinggen’s face now deceives Temur.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 954
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung. He has fought beside the Jin Family in major battles, including the conflict with Mount Heng, and remains alert to threats connected with Dark Heaven. The Human Butcher has claimed him as a personal target in a planned attack.

## Korean source

```text
＃959화



세상에 존재하는 모든 만물은 저마다의 색깔을 지니고 있고, 사람 역시 예외는 아니다.

눈빛이, 표정이, 온몸을 둘러싼 특유의 기운이 누군가를 설명하고 증명한다.

그리고 그런 의미에서, 진무경은 눈앞의 사내를 본 순간 본능적으로 깨달을 수밖에 없었다.

‘마인(魔人).’

머릿속을 스쳐 지나간 두 글자.

틀림없었다.

살기에 취해 있는 눈빛과 느슨하게 올라간 입꼬리.

거기에 더해 사내의 전신에서 배어나는 혈향(血香)은 마주 선 것만으로도 코끝이 저릴 지경이었으니.

‘이놈은…… 도대체 뭐지?’

진무경은 가라앉은 눈빛으로 사내를 응시했다.

이미 피부로 느꼈다. 머리로 이해했다.

느닷없이 나타난 새로운 적이 평범한 악인(惡人)과는 차원이 다르다는 사실을.

과거 항산검문을 기습하고, 생각지도 못한 무위로 그에게 상당한 내상을 안겨 주었던 적풍단주 풍양조차 저자에 비하면 일개 마적에 지나지 않는다고 생각될 정도였다.

결이 다르고, 격이 다르다.

지금껏 쌓아 올린 살업(殺業)은 물론, 일신의 무위(武威)까지도.

그리고 그런 진무경을 바라보며, 칭겐은 씩 웃었다.

“역시, 눈빛이 좋아.”

저벅. 쉭!

칭겐이 산책하듯 가볍게 발걸음을 내디딘 순간, 신형을 날려 뒤로 훌쩍 물러난 진무경이 비스듬히 검신을 곧추세웠다.

“기감도 쓸 만하고.”

칭겐이 만족스럽게 고개를 끄덕였다.

아주 미세한 살기를 흘렸을 뿐이건만, 단 한 치의 망설임조차 없는 반응 속도.

비록 적이기는 하나, 그는 눈앞의 젊은 검귀(劍鬼)가 생각 이상으로 썩 마음에 들었다.

단순한 사냥감으로 생각하기에는 아까울 정도로.

“분위기가 다 죽어 가는 늙은이처럼 어두컴컴하긴 해도 아직 한참 어린놈 같은데……. 너, 누구냐? 내 제자 할래?”

그 누구도 예상치 못했던 한마디에, 칭겐의 등장으로 잠시 소강 상태에 빠져 있던 전장의 분위기가 술렁였다.

그중에서도 특히 무너진 바위 틈새에서 신음하고 있던 백여 명의 유목민은 눈과 귀를 의심하며 자신들의 대족장을 부릅뜬 눈으로 바라보았다.

테무르와 칭겐이 다스리는 서부 초원에 속한 그들은 두 젊은 대족장에 대해 잘 알고 있었고, 그렇기에 지금 이 상황이 더욱더 믿어지지 않았다.

일신의 무위보다는 지략과 통치력으로 칸의 자리에 오른 칭겐이 그 비범한 무위를 통해 단신으로 초원의 형제들을 수백이나 도륙한 적에게 이런 제안을 하다니.

“카, 칸이시여!”

“이 무슨 말도 안 되는……!”

사방에서 터져 나오는 경악 어린 외침.

칭겐과 케식들의 등장에 기뻐하던 기색은 이미 한참 전에 사라졌다.

각기 크고 작은 부상을 입은 채, 부릅뜬 눈으로 자신을 바라보는 유목민들의 모습에 칭겐이 입맛을 다셨다.

“하긴, 역시 이런 상황에 제안하기엔 좀 많이 이상하지? 아직 주위에 보는 눈도 있고.”

바로 그때였다.

칭겐의 왼손에 들려 있던 소검(小劍)이 흐릿해진 것은.

서걱, 쿠구궁!

서늘한 절삭음과 함께 간신히 맞물린 채 쌓여 있던 바위 더미가 무너지며 유목민들을 덮쳤다.

구조를 기다리던 그들의 비명이 굉음에 파묻히더니 이내 완전히 지워졌다.

“하등 도움도 안 되는 쓸모없는 것들이, 하여간 말은 많아서 문제라니까.”

“……!”

“자, 이제 보는 눈이 없어졌으니 아까 하던 이야기나 마저 해 보자고. 응?”

순간 내려앉은 정적 속, 깊숙이 가라앉은 눈빛으로 칭겐을 응시하던 진무경이 불현듯 입술을 뗐다.

“칭겐이라고, 네놈이?”

“어허, 네놈이라니?”

작게 혀를 찬 칭겐이 말을 이었다.

“아무리 애새끼라고 해도 그렇지, 스승님한테 못 하는 말이 없구나. 확 그냥 혓바닥을 뽑아 버릴라.”

건들거리는 태도와 숨길 수 없는 강자의 여유.

진무경은 유목민 특유의 변발을 한 눈앞의 사내가, 수많은 비밀로 이루어진 존재라는 것을 어렵지 않게 알아차릴 수 있었다.

“역용(易用)을 했군. 진짜 칭겐은 어디에 있나?”

곰곰이 생각하던 칭겐이 대답했다.

“글쎄, 아마 지금쯤이면 독수리 배 속이 아닐까?”

“또 다른 한 명은?”

“다른 한 명? 아, 테무르 그놈은 살려 뒀지. 둘 중 하나는 살려 둬야 서부 놈들을 제대로 통제할 수 있으니까.”

칭겐은 거리낌 없이 대꾸했다.

어차피 반경 수십여 장은 케식이 통제하고 있는 상황.

자무카가 오랜 세월 공들여 키워 낸 친위대인 그들은 결코 주인을 배반하지 않는다.

그 어떤 흉포한 사냥개라도 제 주인은 물지 않듯이.

“뭐, 이 정도면 네 궁금증은 충분히 해결해 준 것 같은데……. 이 몸의 관대한 제의는 어떻게 생각하나?”

칭겐이 몹시 기대하는 눈빛으로 진무경을 바라본 그 순간.

“불가(不可).”

낮게 깔린 목소리가 불쑥 울려 퍼졌다.

진무경의 어깨 너머로 보이는 한 사람의 얼굴에 칭겐이 눈살을 찌푸렸다.

“안 된다니, 어째서? 아니, 그 전에 네놈이 뭔데?”

이야기를 방해한 불청객이 담담하게 대꾸했다.

“늑대가 어떻게 개새끼 밑으로 들어가겠나. 친자식처럼 애지중지 키운 아우인데, 형님으로서 그런 꼴은 못 보지.”

“아우? 형님?”

살짝 커진 눈으로 불청객, 진위경을 바라보던 칭겐이 피식 웃었다.

“진씨 형제라……. 이거, 생각보다 훨씬 큰 월척이 걸려들었네.”

월척.

그 두 글자에 진위경의 눈빛이 무거워졌다.

전투가 벌어지기 전, 월척을 낚아 오겠다며 껄껄 웃던 늙은 낚시꾼이 떠올라서였다.

“노 선배께서는 어찌 되셨느냐.”

내심 짐작은 하고 있으나, 그래도 놈의 입으로 직접 듣고 싶었다.

땅바닥에 나뒹굴고 있는 저 묵빛 낚싯대의 주인이, 태원진가를 위해 기꺼이 목숨을 걸고 나서 준 동정어옹이 어찌 되었는지.

그리고, 불길한 예감은 늘 빗나가는 법이 없다.

“아, 그 늙은이.”

칭겐이 흐릿한 웃음과 함께 말을 이었다.

“낚는 솜씨는 제법이었는데, 힘이 부족했어. 분수에 안 맞는 큰 걸 낚아 버리는 바람에 그대로 부러져 버렸지. 저 낚싯대처럼.”

“……!”

“아니, 부러진 정도가 아니라 으스러졌겠군. 자그마치 삼십여 장 아래로 처박혔으니.”

진위경은 침음성을 삼켰다.

검붉은 핏물에 흠뻑 젖은, 군데군데 균열이 간 흑목조간은 동정어옹이 얼마나 치열하게 싸웠는지 알려 주는 증거였다.

자신이 죽으면 푸른 강물에 유골을 뿌려 달라며 입버릇처럼 말했던 늙은 낚시꾼은 오늘, 바로 이 잿빛 협곡에서 뼈를 묻었다.

태원진가에 빚진 목숨을 태원진가를 위해 내던지며.

그리고 이제는 태원진가가 그에게 갚을 빚이 생겼다.

동정어옹뿐만 아니라, 지금까지 죽어 간 모든 이들을 향한 빚이.

“이름과 별호를 대라.”

“뭐?”

“네놈의 정체를 알아야, 훗날 망자들을 위한 제를 올릴 때 당당하게 말할 수 있지 않겠느냐.”

진위경이 서늘한 눈빛으로 칭겐을 응시하며 말을 이었다.

“감히 산서성을 침범하고 당신들을 해한 그 개새끼를, 우리가 직접 찢어 죽였노라고.”

“……!”

“제아무리 세상이 개같이 돌아간다 한들, 그것이 사람 된 도리가 아니겠느냐?”

크게 뜬 두 눈을 깜빡이던 칭겐이, 문득 크게 소리 내어 웃었다.

“으하, 으하하하하!”

쩌렁쩌렁하게 울려 퍼진 웃음소리가 사방을 짓눌렀다.

아니, 그것은 더 이상 단순한 소리라 부를 수 있는 것이 아니었다.

우웅. 드드드득!

부풀어 오르는 공기.

막강한 압력과 함께 지진이라도 난 것처럼 땅과 절벽이 뒤흔들렸고, 참지 못한 신음이 곳곳에서 새어 나왔다.

“흡……!”

만약 거인의 손아귀에 붙잡힌다면 이런 기분일까.

앙천대소(仰天大笑)에 실린 거대한 기운에 가까이에 있던 사람들이 중심을 잃고 비틀거렸다.

공력이 일천한 하급 무인들 중에는 창백한 얼굴로 토혈(吐血)하는 이마저 있었다.

“초, 초절정 고수……!”

누군가의 입술 사이로 탄식처럼 흘러나온 한 마디. 그 안에 담긴 경악의 감정이 모두의 마음을 대변한다.

아니, 그것으로도 부족했다.

수십 개의 산봉우리에도 높낮이의 차이가 존재하듯이, 칭겐의 모습을 한 눈앞의 사내 역시 초절정이란 말로 다 설명할 수 있는 자가 아니었다.

스아아아아.

그 순간, 산서성의 무인들은 자신들의 눈을 의심했다.

마치 보이지 않는 실과 연결된 것처럼, 여기저기 깨지고 부서진 암석의 파편이 허공에 떠오르고 있었다.

그 숫자가 무려 백여 개.

뾰족한 단면은 그 자체로 암기와 같았고, 그 중심에 우뚝 선 사내의 모습은 괴물이나 다름없었다.

실로 변화무쌍한, 인간의 거죽을 뒤집어쓴 괴물.

우둑. 뿌드드득!

뼈가 어긋나고 살이 짓눌리는 섬뜩한 소리와 함께 시시각각 변해가는 모습.

모두가 그 놀라운 광경을 멍하니 바라만 보고 있던 그때, 어디선가 세 줄기의 섬광이 번뜩였다.

슈확!

갈라지는 바람.

케식들조차 제때에 미처 반응하지 못할 만큼, 한 줄기의 벼락이 되어 공간을 가로지른 세 사람은 약속이라도 한 것처럼 동시에 출수(出手)했다.

후웅, 쉭!

거력이 실린 일권(一拳)과 두 자루의 검신이 휘황한 빛줄기를 내뿜으며 칭겐을 향해 쇄도한 그 순간.

“감히!”

콰아아앙!

노호성과 함께 용암처럼 터져 나온 거대한 기운이 주위의 모든 것을 밀어 냈다.

미친 듯이 휘몰아치는 광풍과 함께.

화아아악!

한 치 앞도 내다볼 수 없을 만큼 희뿌연 먼지구름.

항거할 수 없는 힘에 부딪혀 삼 장에 달하는 거리를 밀려난 세 사람이 깊게 가라앉은 눈빛으로 서로를 바라보던 그때.

퍼엉!

날카로운 파공성과 함께 칭겐이, 아니 그 누구도 본 적 없는 생소한 누군가가 모습을 드러냈다.

쿵.

묵직한 발걸음.

어지간한 장정 두셋을 합친 것만큼이나 비대한 체구를 지닌 노인은, 이마에 맺힌 땀을 소매로 훔치며 중얼거렸다.

“빌어먹을, 이건 도무지 적응이 안 된단 말이지.”

조금 전까지만 하더라도 칭겐이라 불렸던 그는 오랜만에 되찾은 자신의 얼굴과 당장이라도 터질 듯한 살집을 더듬었다.

늙고, 추했다.

이것만으로도 불쾌하기 짝이 없는데, 역용술과 축골공을 되돌리는 고통스러운 과정 속에서 기습까지 당했다는 사실은 노인의 기분을 최악으로 치닫게 만들었다.

“이런 천하의 배은망덕한 놈을 봤나…….”

노인은 살에 파묻혀 잘 보이지도 않을 것 같은 실눈으로 감히 자신을 기습한 쥐새끼들을 노려보았다.

지금 이 순간, 그는 진심으로 분노하고 있었다.

저들 중, 오랜만에 자신의 마음에 쏙 든 진무경이 있다는 점에서 더더욱.

“감히 스승을 기습하다니, 넌 파문(破門)이다.”

노인의 선언에 진무경은 문득 생각했다.

만약 이 자리에 자신의 골칫덩어리 동생이 있었다면, 저 헛소리에 뭐라고 대꾸했을지.

그리고 이내 그럴듯한 정답을 찾아냈다.

“개좆이나 빨아라.”

“……!”

“아. 돼지 새끼도 추가.”

분노로 인해 삽시간에 붉어진 노인의 눈동자에, 진무경의 좌우에서 웃고 있는 두 사내의 모습이 비쳤다.

“네놈들은 뭐냐?”

각기 젊고 늙은 두 사내가 선선히 입을 열었다.

“귀검(鬼劍) 위팽.”

“항산호(恒山虎) 철무백.”

태원진가와 항산검문을 대표하는 두 절정 고수의 대답에, 노인은 덩치와는 달리 날렵한 혀로 입술을 핥았다.

“곧 죽어서 귀신이 될 놈과 항산의 개새끼였구먼. 잘 알았다.”

스르릉.

서늘한 마찰음.

노인은 양손에 쥔 두 자루의 검을 교차시키며 입을 열었다.

“저승에 가거든, 마조(魔鳥)가 보냈다 하거라.”

그 한 마디가 신호탄이었다.

멈췄던 전장의 시간을, 아슬아슬하게 남아있던 심지를 핏빛 불꽃으로 내던지는 신호탄.

와아아아아!

깊은 밤을 깨우는 거대한 함성과 함께, 두 개의 파도가 서로를 향해 부딪혔다.
```

## Final English reading copy

```markdown
# Chapter 959

Everything in the world had its own color, and people were no exception.

Their eyes, their expressions, the distinctive energy surrounding them—all of it described and revealed who they were.

And in that sense, the moment Jin Mukyung saw the man before him, instinct told him what he was.

*A demon.*

The two syllables flashed through his mind.

There was no mistake.

The eyes drunk on killing intent. The corners of his mouth, curled in a lazy smile.

And the scent of blood seeping from every inch of the man’s body was so strong it stung the tip of Mukyung’s nose just standing near him.

*What… is this bastard?*

Jin Mukyung stared at the man with a steady gaze.

He could feel it in his skin. He understood it in his mind.

This new enemy who had appeared out of nowhere was on an entirely different level from an ordinary villain.

Even Pung Yang, the Red Wind Band Leader, who had once raided the Mount Heng Sword Sect and dealt Mukyung a serious Internal Injury with a level of skill no one had expected, seemed like nothing more than a mounted bandit compared to this man.

A different breed. A different class.

Not only in the slaughter he had wrought, but in his own martial prowess.

Looking back at Mukyung, Chinggen grinned.

“Just as I thought. You’ve got good eyes.”

*Step. Whish!*

The instant Chinggen took a casual step forward, as if out for a stroll, Mukyung sprang back a great distance and raised his sword at an angle.

“Your Qi Sense is useful, too.”

Chinggen nodded with satisfaction.

He had let only the faintest trace of killing intent slip—and Mukyung had reacted without a moment’s hesitation.

Though they were enemies, Chinggen rather liked the young Sword Demon before him. More than he should like mere prey.

“You’ve got the gloomy air of an old man on his last legs, but you’re still a young brat… Who are you? Want to be my Disciple?”

At those words, which no one could have expected, the battlefield—briefly stilled by Chinggen’s arrival—stirred.

More than anyone, the hundred or so nomads groaning amid the gaps in the collapsed rocks stared wide-eyed at their Great Chieftain, doubting their own eyes and ears.

They belonged to the western grasslands ruled by Temur and Chinggen. They knew the two young Great Chieftains well, which made this all the harder to believe.

Chinggen had taken the position of Khan through his strategy and ability to rule, rather than his personal martial prowess. And now he was making such an offer to the man who had slaughtered hundreds of their brothers on the grasslands all by himself, using an extraordinary level of martial skill.

“K-Khan!”

“What are you saying…?!”

Shocked cries rang out from every direction.

The joy they’d felt at the arrival of Chinggen and the Keshik had vanished long ago.

Chinggen smacked his lips at the sight of the nomads staring at him with wide eyes, each nursing injuries of varying severity.

“Though I guess it’s a pretty strange time to make an offer, huh? Especially with so many people watching.”

It happened then.

The short sword in Chinggen’s left hand blurred.

*Shk. Rrrrrumble!*

With a cold, slicing sound, the piled rocks—barely holding together—came crashing down on the nomads.

Their screams as they waited for rescue were swallowed by the roar, then disappeared completely.

“Useless, worthless things. Always running their mouths. That’s the problem with them.”

“……!”

“Now that there’s no one watching, let’s get back to what we were talking about. Hmm?”

In the sudden silence, Jin Mukyung fixed Chinggen with a deep, steady gaze and spoke.

“So you’re Chinggen, you bastard?”

“Hey, now. ‘You bastard’?”

Chinggen clicked his tongue and continued.

“Even if you’re a brat, that’s no way to speak to your Master. I ought to rip that tongue right out.”

His easygoing manner, and the confidence of a master he couldn’t hide.

Mukyung had no trouble realizing that the man before him, with his hair tied in the distinctive nomad style, was a being made up of countless secrets.

“You’re using a disguise technique. Where is the real Chinggen?”

Chinggen considered the question before answering.

“Who knows? Maybe inside an eagle’s belly by now.”

“And the other one?”

“The other one? Oh, I left Temur alive. One of them had to survive if we were going to keep the westerners under control.”

Chinggen answered without hesitation.

The Keshik controlled everything within a radius of several dozen *jang*. Jamukha had spent many years raising them into his personal guard, and they would never betray their master.

Even the fiercest hunting dog wouldn’t bite its owner.

“Well, I think I’ve answered enough of your questions. So, what do you say to my generous offer?”

Chinggen was looking at Mukyung with great anticipation when—

“Impossible.”

A low voice rang out unexpectedly.

Chinggen frowned at the face he saw over Mukyung’s shoulder.

“Impossible? Why not? No, first—who the hell are you?”

The uninvited guest who had interrupted the conversation answered calmly.

“How could a wolf serve under a mangy dog? He’s my little brother, whom I’ve cherished like my own son. As his older brother, I can’t let that happen.”

“Little brother? Older brother?”

Chinggen looked at the uninvited guest, Jin Wikyung, his eyes widening slightly, then gave a quiet laugh.

“Brothers from the Jin Family… Well, that’s a much bigger catch than I expected.”

*A big catch.*

At those words, Jin Wikyung’s expression grew grave.

He remembered the old fisherman who had laughed heartily before the battle and promised to bring back a big catch.

“What happened to Senior?”

He had an idea, but still wanted to hear it from the man’s own mouth.

What had happened to the Dongting Fisherman, who had risked his life for the Jin Family of Taiyuan—the owner of that dark fishing rod lying on the ground?

And foreboding was rarely wrong.

“Oh, that old man.”

Chinggen continued with a faint smile.

“He was pretty good at fishing, but he didn’t have the strength for it. He hooked something way too big for him and snapped. Just like that fishing rod.”

“……!”

“Actually, ‘snapped’ isn’t enough. More like crushed to pieces. He was slammed more than thirty *jang* down.”

Jin Wikyung swallowed a groan.

Soaked in dark red blood and cracked in several places, the black-wood fishing rod showed how fiercely the Dongting Fisherman had fought.

The old fisherman, who had always said he wanted his ashes scattered in a blue river when he died, had buried his bones here today, in this gray gorge.

He had given his life for the Jin Family of Taiyuan, repaying the life he owed them.

And now the Jin Family owed him a debt in return.

Not only to the Dongting Fisherman, but to everyone who had died so far.

“Give me your name and title.”

“What?”

“I need to know who you are, so I can speak with my head held high when we offer a memorial rite for the dead in the future.”

Jin Wikyung fixed Chinggen with a cold gaze and continued.

“So we can say we personally tore apart and killed the bastard who dared invade Shanxi Province and harm you all.”

“……!”

“No matter how badly the world’s gone to hell, isn’t that the proper thing for people to do?”

Chinggen blinked his wide-open eyes, then suddenly burst into loud laughter.

“Ha! Hahahahaha!”

His laughter boomed through the gorge, pressing down on everything around it.

No—it could no longer be called a mere sound.

*Vrrrrm. Rrrrattle!*

The air swelled.

A tremendous pressure shook the earth and cliffs as if an earthquake had struck, and groans escaped from all around.

“Urgh…!”

Was this what it would feel like to be caught in a giant’s grasp?

The immense energy carried by Chinggen’s uproarious laughter made those nearby lose their balance and stagger.

Some of the lower-level martial artists, with only a little internal energy, went pale and even spat blood.

“A Supreme Peak master…!”

The words slipped from someone’s lips like a groan. The shock in them spoke for everyone.

No. Even that wasn’t enough.

Just as dozens of mountain peaks varied in height, the man before them, wearing Chinggen’s face, could not be fully described by the words Supreme Peak.

*Sssssss.*

At that moment, the martial artists of Shanxi Province could hardly believe their eyes.

Shattered fragments of rock, large and small, were rising into the air as if attached to invisible threads.

There were more than a hundred of them.

Their jagged edges were hidden weapons in their own right, and the man standing tall at their center was nothing less than a monster.

A monster of endless change, wearing human skin.

*Crack. Crrrunch!*

Bone shifted, flesh crushed—the man’s appearance changed with a series of chilling sounds.

Everyone stared, stunned by the sight. Then three streaks of light flashed from somewhere.

*Shwaaa!*

The air split.

Three people crossed the space like bolts of lightning, so fast even the Keshik couldn’t react in time. As if they’d rehearsed it, all three attacked at once.

*Whoom. Whish!*

A mighty punch and two swords blazed with brilliant light as they rushed toward Chinggen—

“How dare you!”

*KABOOM!*

With an enraged shout, an enormous force burst out like lava and drove everything around him away.

A violent gale whipped through the gorge.

*Fwoooooosh!*

A thick cloud of pale dust rose, obscuring everything beyond arm’s reach.

The three attackers were thrown back three *jang* by the irresistible force. They exchanged deep, steady looks—when—

*Pop!*

With a sharp crack of displaced air, Chinggen—or rather, someone entirely unfamiliar, whom none of them had ever seen—appeared.

*Thud.*

A heavy footstep.

The old man, whose body was as big as two or three ordinary men, wiped the sweat from his brow with his sleeve and muttered,

“Damn it. I just can’t get used to this.”

The man who had been called Chinggen moments before ran his hands over his own face, returned to him after so long, and his flesh, which seemed ready to burst at any moment.

Old and ugly.

That alone was more than unpleasant enough, but being ambushed while painfully reversing his disguise technique and Bone-Shrinking Technique had put him in the foulest of moods.

“You ungrateful little bastard…”

The old man glared at the rats who had dared to ambush him. His eyes were so narrow and buried in fat they seemed impossible to see.

At this moment, he was truly furious.

All the more so because Jin Mukyung, who had won his heart for the first time in a long while, was among them.

“How dare you ambush your Master? You’re expelled.”

At the old man’s declaration, Jin Mukyung found himself wondering what his troublesome younger brother would have said to such nonsense, had he been here.

And soon enough, he found a plausible answer.

“Go suck a dick.”

“……!”

“Oh. And you’re a fat pig, too.”

The old man’s eyes, reddening in an instant with anger, reflected the two men grinning on either side of Jin Mukyung.

“And who are you two?”

The two men, one young and one old, answered readily.

“Ghost Sword Wipeng.”

“Tiger of Mount Heng, Cheol Mubaek.”

At the answers from the two Peak masters representing the Jin Family of Taiyuan and the Mount Heng Sword Sect, the old man licked his lips with a nimble tongue that didn’t match his size.

“So, one of you’s about to die and become a ghost, and the other’s a dog from Mount Heng. Good to know.”

*Shing.*

The cold scrape of metal.

The old man crossed the two swords in his hands and spoke.

“When you get to the underworld, tell them the Demon Bird sent you.”

Those words were the signal.

A signal that threw the stopped time of the battlefield, and the wick that had barely remained, into a blaze of blood-red flame.

“Waaaaaah!”

With a great roar that woke the deep night, two waves crashed into each other.
```
