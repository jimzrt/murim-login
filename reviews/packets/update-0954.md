<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0954.txt",
      "sha256": "22cee0957e35a68e87bdb7e66b76835c2a71bf7f15b833773f6b51676d4052aa",
      "bytes": 13550
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0e3ed74ddc1d7f71c029dad0f3365833979243ce83bbf1cf47950d8b516d44bc",
      "bytes": 2025
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0d79489be8294ad7b5e3ad31b79c1f4c256c70b671beefaa94baf9584937b909",
      "bytes": 234136
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "d58609fcdef46e90a5da3973d7489bf5454962a735f2a33c274eb2cfaa1b9007",
      "bytes": 598
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1b6a7e618cc135c5e5ede19217660a3dd240afbfd6569fc4ae4b1e6b6b1a2aaa",
      "bytes": 759
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "e58dd230fbef09a2eda94ebdbdb481aec9178de637e34f6ad3572ab48de3070e",
      "bytes": 1343
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "16477f94296cbc1848e2a216ddd1057adf23080ff74ac29e7f866b448f14d1e9",
      "bytes": 1119
    },
    {
      "path": "characters/Ju Gongsan.md",
      "sha256": "e3f6cbaafeb4d08aba3b1bdf55543b2f7911bb9ed26314eebd80d241064fcfc4",
      "bytes": 900
    },
    {
      "path": "characters/Temur.md",
      "sha256": "5a8bc0cf8d123a0fabc32148368dd7fbf4c71fd05b00858f66247d9de6ec7879",
      "bytes": 617
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "89f453f47f2375a8a02471ac6ab575d228d8a0682961cf7879e1a27c6f2e62b7",
      "bytes": 954
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a20f593116af26c44513a62978f9565dd0243e9d8b9b1d44d682a18b3511712e",
      "bytes": 267908
    }
  ],
  "estimated_tokens": 10832
}
-->

# Durable State Update — Chapter 954

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
1 and safe_through 954. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 954. Profile updates may replace only one
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
  "chapter": 954,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 954,
    "continuity_sources": [954],
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
    "Jin Mukyung’s Heaven Shaking Squad annihilated the enemy vanguard of one thousand, including one hundred elite troops, suffering twenty-three deaths and thirty-seven wounded.",
    "The enemy has arrived at Eight Spring Gorge. Jin Wikyung has ordered the defenders to prepare for battle.",
    "Jin Wikyung evacuated northern Shanxi’s people and troops, ordered the near-harvest fields burned, and prepared traps and iron caltrops on detours other than Jeongyang.",
    "Five earthen forts are being built at Eight Spring Gorge; thousands of commoners are helping defend Shanxi, many out of gratitude for the Jin Family’s past aid.",
    "The Emperor remains gravely ill from Blood Soul Gu; the Divine Physician says saving him requires him to die once, and Taekyung’s quest to remove the Gu and treat him remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "The real Chinggen was killed; an impostor wearing his face continues to accompany Jamukha."
  ],
  "continuity_sources": [
    952,
    953
  ],
  "open_questions": [
    "How will the defense at Eight Spring Gorge fare against the arriving enemy?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will the Chinggen impostor do, and what is their purpose?"
  ],
  "safe_through": 953,
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
| 태원진가   | **Jin Family of Taiyuan**        |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 주공산 | **Ju Gongsan** | Former head and founder of the Yongbong Escort Bureau. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 평화 | **Peace Guild** | Guild name. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 게르 | **ger** | Traditional nomadic dwelling contrasted with Central Plains wooden buildings. |
| 화주 | **strong liquor** | Liquor stored and consumed by the dark-path swordsmen. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 중양절 | **Double Ninth Festival** | Festival used as the expected date for the invasion of the Central Plains. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 전령 | 진위경 | military messenger to Lesser Family Head | Lesser Family Head | formal-polite and deferential | Uses 소가주님 when confirming Wikyung's identity. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |
| 칭겐 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | The impostor wearing Chinggen’s face addresses Jamukha with deference. |
| 테무르 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | Temur affirms Chinggen’s public praise of Jamukha. |

## Listed compact profiles

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 952
- **Aliases:** None
- **Role:** The real Chinggen was a Khan of the eastern grasslands and Temur’s brother, but he was killed in the attack on their gathering; an impostor now wears his face.
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur was Chinggen’s brother and fellow Khan; an impostor wearing Chinggen’s face now manipulates Temur.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 953
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 953
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Peak-level swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and seeks strength in service of his family.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and Mukyung cherishes his promise to reunite with him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 953
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he can agonize over costly decisions but commits firmly once resolved.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and the people of Shanxi—including many commoners the Jin Family once aided—are willing to help defend their home alongside him.

### Ju Gongsan.md

# Ju Gongsan (주공산)

- **Safe through:** Chapter 624
- **Aliases:** Escort King
- **Role:** Founder and former head of the Yongbong Escort Bureau; during the Great Faction War, he was a wandering escort who refused to surrender a pregnant woman of the Guangdong Chen Family to the Demonic Cult after accepting her escort fee, carried her from Guangdong through Jiangxi and Hubei to Henan over two years, and became known as the Escort King; he later founded an escort bureau in his hometown of Shaanxi and died from internal injuries sustained during the war.
- **Personality:** Remarkably skilled, chivalrous, principled, and unwavering in his obligations.
- **Voice:** Not established.
- **Relationships:** Ju Hogun was his only blood child and successor as head of the Yongbong Escort Bureau; Ju Hwaran is his granddaughter.

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 951
- **Aliases:** None
- **Role:** Temur is a Khan of the northern grasslands, ruling alongside Chinggen over tens of thousands of horses and warriors.
- **Personality:** Hot-tempered, reckless, proud of his khan lineage, and inclined to dismiss distant threats while indulging in celebration.
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** The real Chinggen was Temur’s brother and fellow Khan, but he was killed; an impostor wearing Chinggen’s face now manipulates Temur.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 949
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung. He has fought beside the Jin Family in major battles, including the conflict with Mount Heng, and remains alert to threats connected with Dark Heaven. The Human Butcher has claimed him as a personal target in a planned attack.

## Korean source

```text
＃954화



해가 서산으로 기울고 사방에 어둠이 내려앉으면, 고요해진 세상은 지금껏 들을 수 없었던 것들을 바람에 실어 귓가로 전해 준다.

풀벌레들의 울음소리. 나뭇잎이 스치는 소리.

더불어 수백여 장 밖에서 울려 퍼진, 공력이 담긴 누군가의 외침 같은 것들을.

“어떤 놈인지는 몰라도 목청 한번 좋군. 안 그런가?”

귓가를 파고든 나직한 목소리에 테무르가 마른침을 삼켰다.

파르르 떨리는 그의 눈동자에는 흐릿한 달빛 아래서 웃고 있는 한 사람의 모습이 비치고 있었다.

칭겐.

기억조차 흐릿한 어린 시절부터 함께 성장한 자신의 혈육.

비록 같은 부모 아래에서 태어난 것은 아니나, 친형제보다도 가까웠던 사촌이자 ‘안다의 맹세’로 맺어진 의형제.

그리고…… 이제 더는 이 세상 사람이 아니게 된 망자(亡者).



‘마냥 웃고 떠들 때가 아닐세, 테무르.’



유난히도 서늘한 초원의 바람이 게르의 입구를 밀어젖히기 전, 근심 어린 표정으로 말을 건네던 칭겐의 모습이 문득 눈앞을 스쳤다.

‘형제여, 미안하다. 네 말이 옳았어.’

테무르는 참담한 심정으로 고개를 떨구었다.

왜 칭겐의 말을 귀담아듣지 않았던 것일까.

떠올리는 것만으로도 몸서리치게 만드는 참극(慘劇)이 벌어졌던 그 날 이전에도, 칭겐은 이미 여러 번에 걸쳐 전령을 통해 연락을 취해 왔었다.

초원의 기류가 심상치 않게 흘러가고 있다고.

자신들의 손이 닿지 않는 곳에서, 알 수 없는 무언가가 시작된 것 같다고.

하지만 테무르는 대수롭지 않게 한 귀로 흘려 넘겼다.

교역로를 통해 흘러들어온 온갖 진귀한 보물들로 게르를 가득 채우고, 수하들과 함께 마음껏 술과 고기를 들이켰다.

그것이 어떤 결과를 불러올지는 꿈에도 모른 채.

“또 무슨 생각에 그리 잠겨 있나, 형제.”

순간, 눈앞에 어른거리던 칭겐의 얼굴이 사라졌다.

막 잠에서 깬 사람처럼 화들짝 놀라 고개를 쳐든 테무르가 떨리는 목소리로 대답했다.

칭겐을 죽인, 그리고 이제는 칭겐이 되어 버린 그를 향해.

“아무것도, 아무것도 아니야.”

“저런, 아무래도 전투를 앞두고 긴장한 모양이군. 내 말을 듣지 못했던 것도 그　때문인가?”

“그게 무슨…….”

“조금 전에 들려온 그 외침. 자네도 아는 목소리 아냐?”

뒤늦게 그 말의 의미를 깨달은 테무르가 황급히 대답했다.

“마, 맞아. 태원진가의 소가주. 바로 그자가 틀림없어.”

“아, 그렇군. 어디서 들어 본 목소리다 싶었지.”

물론 혹시 모를 주위의 의심을 피하기 위한 거짓말이었다.

단순한 테무르라면 모를까, 매사에 철두철미했던 칭겐이 몇 번이나 만났던 중요 인물에 관한 것을 잊을 리는 없을 테니까.

“진위경이라…… 그래, 그렇단 말이지.”

만족스럽게 입맛을 다신 칭겐이 힐끗 등 뒤를 곁눈질했다.

모종의 의미가 담긴 그의 눈짓에, 시종일관 담담한 얼굴로 말을 몰아 나아가는 자무카가 살짝 고개를 끄덕였다.

- 목청만 큰 게 아니라 간도 크군요. 태원진가의 소가주는.

어둠 속에서 은밀히 퍼져나가는 전음(傳音).

자무카의 입가에 흐릿한 미소가 맺혔다.

- 처음부터 도망칠 속셈이었다면, 번거롭게 그런 헛수작까지 부리지는 않았겠지.

- 헛수작치고는 제법이었습니다. 덕분에 생각지도 못한 피해를 입었으니까요.

눈살을 찌푸린 칭겐은 흔들리는 말안장 위에서 가래를 탁 뱉었다.

오래전 대륙을 통일한 잔인무도한 황제가 장장 만 리에 걸쳐 쌓은 장성(長城)은 성벽이라 부르기에도 민망한 수준.

그러나 무주공산이어야 할 북부에는, 숱한 장애물들이 도처에 깔려있었다.

- 선봉대가 전멸한 것까지는 그렇다 치더라도, 이 정도로 지저분하게 개판을 쳐 놓을 줄은 몰랐습니다.

개판.

칭겐이 생각하기에는 더할 것도, 뺄 것도 없는 완벽한 표현이었다.

비바람을 뚫고 도착한 산서성 북부는 말 그대로 초토화 상태였으니까.

추수를 앞두고 있어야 할 논밭은 쑥대밭이 되어 있었고, 우물과 개울가는 독과 오물로 뒤덮였으며 심지어 가옥(家屋)들조차 잿더미로 변해 있었다.

- 정신 나간 놈들이 따로 없군요. 얼마 전까지 살던 터전까지 모조리 불태우고 떠나다니.

혀를 내두르는 칭겐의 전음에, 자무카가 담담한 얼굴로 입술을 달싹였다.

- 한 고조(高祖)에 대해 아나?

- 들어는 봤습니다. 항우와 유방할 때 그 유방 아닙니까?

- 그래. 최후의 승자가 된 그도 소싯적 항우에게 밀려 한중으로 떠날 때가 있었지. 그때 책사였던 장량의 조언으로 잔도(棧道)를 불태웠다.

- 스스로 돌아갈 길을 없앴군요.

- 하지만 결국 중원으로 돌아와 항우를 몰아내고 천하의 주인이 되었다. 놈들에게는 이 땅이 바로 그 잔도야. 사람만 남아 있다면 언제든지 다시 만들어 낼 수 있는.

한 명이 홀로 있다면 그건 개인이고, 열 명이 있다면 무리다.

그러나 백 명, 천 명이 모인다면 마을과 도시가 생겨난다.

결국 중요한 것은 사람이다.

비록 북부의 모든 것은 파괴되었으나, 그들은 제 스스로 고향을 불태우며 다짐했을 것이다.

반드시 돌아와 이 땅을 되찾겠노라고.

아득한 과거 자신의 선조들이 그러했듯이, 아무것도 남지 않은 폐허에서 새롭게 시작하겠노라고.

- 물론, 전부 헛된 희망에 불과하지.

자무카는 흐릿하게 웃었다.

항우는 오만했고 우둔했다.

그렇기에 천하를 오시할 무위와 세력을 지녔음에도 끝끝내 유방에게 패배할 수밖에 없었다.

하지만 자무카는 다르다.

그는 수십여 년간 서쪽 초원의 지배력을 공고히 다지며 세력을 길러왔고, ‘그분’의 부름을 기다려 왔다.

그리고 마침내…….

‘때가 왔다.’

자무카는 새카만 어둠 속을 응시했다. 달빛조차 먹구름에 가려져 흐릿한 그곳에서, 떨리는 마음을 애써 억누르며 창칼을 곧추세운 적들이 보이는 듯했다.

“느껴지느냐. 저들의 두려움이.”

나직한 음성이 어둠을 뚫고 울려 퍼진다.

공력이 실린 자무카의 목소리는 모두의 귓가를 선명하게 파고들었고, 그의 안광(眼光)은 형형하게 빛났다.

“적들은 높은 성벽 뒤에 숨어 일평생을 보냈다. 평화에 젖어 식량만 축내는, 소나 돼지와 다를 바 없는 것들이다!”

반면 초원은 어떠한가.

그들은 풀과 흙에서 태어났다.

성벽이 아닌 게르에서 차가운 북풍(北風)을 버텼고, 말과 함께 눈밭을 내달리며 짐승들을 사냥했다.

초원의 유목민들에게 있어 죽음이라는 단어는 헐값이었고, 약탈과 살인은 당연시되었다.

“저들은 모른다. 우리가 어디에서 왔는지, 우리의 선조들이 얼마나 위대한 정복자였는지!”

힘이 실린 음성이 밤공기를 짓누른다.

서리와 얼음으로 뒤덮인 땅을 짓밟고, 끔찍한 열사의 사막을 가로질렀던 선조들의 말발굽 소리가 모두의 귓가에 아스라이 울려 퍼지는 듯했다.

“밝은 눈으로 활시위를 당겨라. 호랑이의 발톱처럼 창을 뻗어라. 독수리의 발톱과도 같은 신월도(新月刀)로 놈들의 육신을 가르고, 거센 말발굽으로 짓밟아라!”

느슨하게 풀어져 있던 유목민들의 눈동자에 서서히 빛이 깃들었다.

보름도 넘게 쉼 없이 이어진 강행군과 사방에 깔린 함정들.

독이 발린 철질려(鐵蒺藜)에 목숨처럼 아꼈던 애마를 잃은 자가 수천이요. 오염된 물을 마시고 쓰러진 이들 또한 수천에 이른다.

뿐인가.

가옥마저 불타고 없으니 밤이슬을 맞으며 노숙을 해야 했고, 신속함을 위해 말안장에 앉아 만든 질긴 육포로 배를 채워야 했다.

그러나 상관없다.

수천의 인마가 쓰러졌어도, 아직 수만의 인마가 남아 있다.

불과 절반도 채 되지 않는 적들을 박살 낸다면, 이 전투에서 승리한다면 모든 것이 끝난다.

짙은 어둠이 내려앉은 저 협곡 너머에서 그들을 기다리고 있는 것은, 나약하기 그지없는 적들뿐만이 아니었다.

부와 명예. 그리고 새로운 시대였다.

“사랑하는 형제들이여, 옛 선조들을 기억하라! 영광만이 가득했던 초원을 떠올려라!”

자무카는 부르짖었다.

마치 초원을 지배하는 맹수들의 왕처럼.

게르를 벗어나 천둥 같은 말발굽 소리와 함께 대륙을 질타했던 과거의 위대한 정복자처럼.

그리고 어느덧 백여 장 앞까지 다가온 협곡을 노려보며, 낮지만 또렷한 목소리로 입을 열었다.

“이제, 정복의 시간이다.”

그 순간.

차차차차창!

무수한 강철의 파도가 어둠을 집어삼켰다.

부드럽게 휘어진 신월도가, 날카로운 돌격창이, 번개처럼 시위에 매겨진 화살이 사방에서 번뜩였다.

와아아아아아아!

깊은 밤을 깨우는 것으로도 모자라 하늘과 땅마저 떨어 울리는 거대한 함성과 함께.

두두두두두!

수십에서 수백으로, 수백에서 수천으로.

마침내 수만으로 불어나 협곡을 향해 바람처럼 쏘아졌다.

듣는 이로 하여금 등골이 오싹해지는 기성(奇聲)을 토해내며, 반동에 따라 말의 꼬리처럼 굽이치는 머리카락을 휘날리며.

거짓으로 점칠 된 참극에 대한 복수를 하기 위해, 선조들이 이룩한 옛 영광을 쟁취하기 위해 온 힘을 다하여 앞으로 나아갔다.

드드드드득!

그리고 흡사 지진이라도 난 것 같은 그 거센 진동을, 협곡 너머의 사람들은 피부로 느끼고 있었다.

“결국, 이렇게 되는군.”

작게 뇌까린 진위경은 문득 자신의 손을 내려다보았다.

검 자루를 힘껏 말아쥔 그의 손은 어느덧 잘게 떨리고 있었다.

어째서일까.

지금 이 순간에도 엄청난 기세를 내뿜으며 들이닥치는 적들이 두려워서?

아니다.

그가 두려워하는 것은 적이 아니라, 이 자리에서 수없이 죽어 갈 아군이었다.

더불어 그들 모두를 지키지 못할 자신 스스로였다.

‘그렇기에…… 반드시 승리해야 한다.’

이미 가능한 모든 조치를 취했다.

더는 돌이킬 수도, 물러설 수도 없다.

진인사대천명(盡人事待天命).

사람이 할 수 있는 일은 다했으니, 남은 것은 하늘에 맡기라는 그 격언을 진위경은 문득 떠올렸다.

누구보다 그 말을 싫어했던, 지금은 이 자리에 없는 누군가도 함께.



‘아니, 결국 하늘에 맡길 거면 뭐하러 그 개고생을 해요? 온갖 생지랄을 떨어서라도 하늘도 뜻을 바꾸게 만들어야지.’



그래, 녀석이라면 분명 그렇게 말했겠지.

불현듯 귓가에 울려 퍼지는 그 생생한 목소리에, 진위경은 자신도 모르게 실소를 터트렸다.

그리고 다음 순간, 어느새 손의 떨림이 멎었다는 것을 깨달았다.

“위팽.”

천둥 같은 말발굽 소리를 뚫고 흘러나온 나직한 부름에, 그의 오랜 충복이 대답했다.

“하명하십시오.”

촌각 후면 수만의 인마가 들이닥치는 상황.

거친 숨소리가 사방에서 흘러나온다.

모두의 이목이 총사령관인 진위경을 향해 쏠린 그때, 생각지도 못한 한 마디가 들려왔다.

“내년 중양절은 항산(恒山)에서 보내는 것이 좋겠네.”

“……!”

“모두가 함께 국화주를 마시고, 풍악을 울리며 웃고 즐기자고.”

“주, 주군.”

“왜, 별로인가. 내 제안이?”

희미한 미소를 띤 채 웃고 있는 진위경을, 위팽을 비롯한 모두가 멍하니 바라보았다.

그리고 약속이라도 한 듯, 동시에 진위경과 닮은 웃음을 입가에 머금었다.

울컥 솟구치는 격동을 억누르며.

‘내년 중양절에는, 모두가 함께.’

그 짧은 말에 담긴 의미에 가슴 한구석이 일렁인다.

미소를 머금자 두려움이 사라지고, 소리 내어 웃으니 굳어 있던 몸이 부드럽게 풀렸다.

사방에 드리운 짙은 어둠이, 더는 불안하게 느껴지지 않았다.

저벅.

유난히도 또렷하게 울려 퍼진 발걸음 소리. 모두의 앞으로 나선 누군가가 입을 열었다.

“꽤 즐거울 것 같군요. 내년 중양절은.”

진무경은 웃고 있었다.

어느덧 협곡을 집어삼킨 진동과 함성 속에서.

지난 이 년간 그의 유일한 벗이 되어 주었던 어둠 속에서.

그리고 다음 순간.

두두두두, 화악!

마치 장막이 벗겨지듯, 칠흑 같은 암흑 속에서 뛰쳐나온 수십의 인마(人馬)를 향해 돌아섰다.

슈확!

허리춤에서 솟구친 눈부신 섬광이, 흐릿한 달빛을 갈랐다.
```

## Final English reading copy

```markdown
# Chapter 954

When the sun dipped toward the western mountains and darkness settled all around, the quiet world carried things you’d never been able to hear before on the wind, right to your ears.

The cries of crickets. Leaves brushing against one another.

And, from hundreds of *jang* away, something like a shout from someone whose voice carried internal energy.

“I don’t know who that bastard is, but he’s got a set of lungs on him. Don’t you think?”

At the low voice that pierced his ears, Temur swallowed nervously.

His trembling eyes reflected the sight of someone smiling in the faint moonlight.

Chinggen.

His blood relative, who had grown up alongside him since childhood—so long ago that even those memories had grown hazy.

Though they hadn’t been born to the same parents, Chinggen was his cousin, closer to him than a blood brother, and his sworn brother, bound to him by the anda oath.[^1]

And… now he was dead. No longer one of the living.

*This is no time to laugh and chatter, Temur.*

Before the unusually cold steppe wind pushed open the entrance to the ger, Chinggen had spoken to him with a worried look on his face. The memory suddenly flashed before his eyes.

*Brother, I’m sorry. You were right.*

Temur lowered his head, his heart heavy.

Why hadn’t he listened to Chinggen?

Even before that day—the day of the tragedy that made his whole body shudder just to remember it—Chinggen had sent word through messengers several times.

The mood on the grasslands was turning strange.

It seemed something unknown was beginning to unfold somewhere beyond their reach.

But Temur had dismissed his words without a second thought.

He had filled his ger with all manner of rare treasures brought in along the trade routes, then drank and feasted to his heart’s content with his men.

Never once dreaming what it would lead to.

“What’s got you so lost in thought this time, brother?”

In an instant, Chinggen’s face, wavering before his eyes, disappeared.

Temur jerked his head up, startled like a man just woken from sleep, and answered in a trembling voice.

To the man who had killed Chinggen—and had now become Chinggen.

“It’s nothing. Nothing at all.”

“Goodness. You must be nervous before the battle. Is that why you didn’t hear me?”

“What do you mean…?”

“That shout we just heard. Don’t you recognize the voice?”

Only then did Temur grasp what he meant, and hurriedly answered.

“Y-yes. It’s the Lesser Family Head of the Jin Family of Taiyuan. It can only be him.”

“Ah, I see. I thought I’d heard that voice somewhere.”

Of course, it was a lie to avoid arousing suspicion from anyone nearby.

Temur might have been simple, but there was no way the meticulous Chinggen would forget an important figure he’d met several times.

“Jin Wikyung… So that’s who it is.”

Chinggen smacked his lips in satisfaction, then glanced over his shoulder.

At the meaningful glance, Jamukha, who had been riding ahead with an impassive expression, gave a slight nod.

*He’s not just loud. The Lesser Family Head of the Jin Family of Taiyuan has some nerve.*

Sound Transmission spread discreetly through the darkness.

A faint smile touched Jamukha’s lips.

*If he’d planned to run from the start, he wouldn’t have gone to the trouble of pulling off that trick.*

*It was quite a trick for a mere ruse. We took losses we never expected, thanks to it.*

Chinggen frowned and spat out a mouthful of phlegm from the swaying saddle.

The Great Wall, built across a full ten thousand *li* by a cruel and merciless emperor who had unified the continent long ago, was hardly worthy of being called a wall.

Yet the north, which should have been unoccupied, was littered with obstacles everywhere.

*I can accept that the vanguard was wiped out, but I never expected them to turn the whole place into such a filthy shitshow.*

A shitshow.

In Chinggen’s view, it was the perfect word.

Northern Shanxi Province, where they had arrived after braving wind and rain, had been utterly devastated.

The fields, which should have been on the verge of harvest, had been laid to waste. Wells and streams were covered in poison and filth. Even the houses had been reduced to ashes.

*Those lunatics. They burned down every last thing they’d called home until just recently, then left.*

At Chinggen’s Sound Transmission, Jamukha’s lips moved, his expression still calm.

*Do you know of Emperor Gaozu of Han?*

*I’ve heard of him. The Liu Bang from the story of Xiang Yu and Liu Bang, right?*

*That’s right. Even the man who became the final victor was once driven back by Xiang Yu and forced to retreat to Hanzhong. At the time, his strategist Zhang Liang advised him to burn the plank roads.*

*He cut off his own way back.*

*But he eventually returned to the Central Plains, drove out Xiang Yu, and became its ruler. To them, this land is that plank road. As long as people remain, they can rebuild it whenever they want.*

One person alone was an individual. Ten people made a group.

But when a hundred or a thousand gathered, villages and cities came into being.

In the end, people were what mattered.

Though everything in the north had been destroyed, they must have burned their own homes and vowed to themselves:

*We’ll return and reclaim this land.*

*Just as our ancestors did in the distant past, we’ll begin anew from these ruins, with nothing left.*

*Of course, all of it is nothing but a vain hope.*

Jamukha smiled faintly.

Xiang Yu had been arrogant and foolish.

That was why, despite having the might and power to look down on all under Heaven, he had ultimately been defeated by Liu Bang.

But Jamukha was different.

For decades, he had steadily strengthened his hold over the western grasslands and built his forces, waiting for that person to call for him.

And at last…

*The time has come.*

Jamukha gazed into the pitch-black darkness. There, where even the moonlight was dimmed by dark clouds, he could almost see the enemy holding their spears and swords upright, struggling to master their trembling hearts.

“Can you feel it? Their fear.”

His low voice rang through the darkness.

Jamukha’s voice, charged with internal energy, pierced clearly into everyone’s ears, and his eyes shone fiercely.

“Our enemies have spent their entire lives hiding behind tall walls. They’re no different from cows and pigs, wallowing in peace and doing nothing but consuming food!”

But what of the grasslands?

They had been born from grass and earth.

They had endured the cold north wind in gers, not behind walls, and raced with their horses across snowy fields to hunt beasts.

To the nomads of the grasslands, the word *death* came cheap. Plunder and murder were taken for granted.

“They don’t know where we came from, or how mighty our ancestors were as conquerors!”

His forceful voice pressed down on the night air.

It was as if the sound of their ancestors’ hooves, trampling across lands covered in frost and ice and crossing the dreadful, scorching desert, were faintly echoing in everyone’s ears.

“Draw your bows with clear eyes. Thrust your spears like a tiger’s claws. Slice through their flesh with your crescent sabers, sharp as an eagle’s talons, and trample them under your horses’ thundering hooves!”

A light slowly kindled in the nomads’ slack eyes.

More than half a month of relentless marching, and traps scattered everywhere.

Thousands had lost their beloved horses to iron caltrops coated in poison. Thousands more had collapsed after drinking contaminated water.

And that wasn’t all.

With even their homes burned down, they had to sleep outside beneath the night dew, and fill their stomachs with tough jerky made in the saddle, all in the name of speed.

But it didn’t matter.

Even if thousands of men and horses had fallen, tens of thousands remained.

If they crushed the enemy—who numbered less than half their own force—and won this battle, it would all be over.

Beyond that gorge, shrouded in deep darkness and waiting for them, lay more than just their weak and helpless enemies.

Wealth and honor. And a new age.

“My beloved brothers, remember our ancestors! Remember the grasslands, where nothing but glory awaited us!”

Jamukha cried out.

Like the king of beasts ruling the grasslands.

Like the great conquerors of the past, who had left their gers and thundered across the continent with the sound of their horses’ hooves.

Then, glaring at the gorge, now less than a hundred *jang* away, he spoke in a low but clear voice.

“Now, it’s time to conquer.”

At that moment—

*Clang-clang-clang-clang!*

Countless waves of steel swallowed the darkness.

Gently curved crescent sabers, sharp lances, and arrows nocked to bowstrings like lightning flashed all around them.

“Waaaaah!”

With a tremendous roar that not only shattered the deep night but made heaven and earth themselves seem to tremble—

*Thududududu!*

Dozens became hundreds. Hundreds became thousands.

At last, tens of thousands surged toward the gorge like the wind.

They let out eerie cries that sent chills down the spines of those who heard them. Their hair, waving like horses’ tails with every bounce, streamed behind them.

They charged forward with all their might, to avenge the tragedy built on lies and seize the ancient glory their ancestors had won.

*Rrrrummmble!*

And the people beyond the gorge could feel the fierce shaking beneath their feet, as if an earthquake had struck.

“So it comes to this, after all.”

Jin Wikyung murmured, then looked down at his hand.

His fingers, clenched tight around his sword hilt, had begun to tremble.

Why?

Was he afraid of the enemies bearing down on them, radiating a tremendous aura even now?

No.

What he feared was not the enemy, but the countless allies who would die here.

And himself, unable to protect them all.

*That’s why… we have to win.*

He had already taken every measure he could.

There was no turning back, no retreating now.

*Do everything within your power, then leave the rest to Heaven.*

Jin Wikyung suddenly remembered the old saying: people should do all they can, then leave what remains to Heaven.

And with it, someone who had hated those words more than anyone, and was no longer here.

*No. If you’re just going to leave it to Heaven in the end, why go through all that hell? You’ve got to make Heaven change its mind, even if you have to raise all kinds of hell to do it.*

Yes, that was exactly what the guy would have said.

At the vivid voice ringing in his ears, Jin Wikyung let out a laugh before he knew it.

Then, the next moment, he realized his hand had stopped trembling.

“Wipeng.”

At the low call that cut through the thunder of approaching hooves, his longtime loyal retainer answered.

“Yes, my lord.”

Tens of thousands of men and horses would arrive in mere moments.

Ragged breaths sounded all around them.

Everyone’s eyes were fixed on their commander-in-chief, Jin Wikyung, when an unexpected remark reached their ears.

“Next year, I think we should spend the Double Ninth Festival on Mount Heng.”

“……!”

“Let’s all drink chrysanthemum wine together, play music, laugh, and enjoy ourselves.”

“M-my lord.”

“What? Don’t you like my suggestion?”

Everyone, Wipeng included, stared blankly at Jin Wikyung, who was smiling faintly.

Then, as if they’d agreed in advance, they all wore smiles that resembled his.

They held back the surge of emotion welling up inside them.

*Next year, we’ll all be together for the Double Ninth Festival.*

The meaning contained in those few words stirred something in their hearts.

As smiles touched their lips, fear disappeared. When they laughed aloud, their stiff bodies loosened.

The deep darkness hanging all around them no longer felt unsettling.

*Step.*

A footfall rang out, unusually clear. Someone stepped forward before them all and spoke.

“Next year’s Double Ninth Festival sounds like it’ll be quite enjoyable.”

Jin Mukyung was smiling.

Amid the vibration and shouts that had swallowed the gorge.

In the darkness that had been his only friend for the past two years.

And the next moment—

*Thudududu—whoosh!*

As if a curtain had been drawn aside, he turned toward the dozens of men and horses bursting out of the pitch-black darkness.

*Shing!*

A dazzling flash leapt from his waist and cleaved through the faint moonlight.

[^1]: An *anda* is a sworn brother in Mongolian tradition; the oath binds two people as brothers.
```
