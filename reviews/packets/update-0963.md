<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0963.txt",
      "sha256": "c238a8b326aaca59e18a3729a296f3cb9944d41a3d02722271399899b93cbd33",
      "bytes": 13173
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e40ac9828b714ea1f9e30e0bb77d94d8f4abd8e13ead9c031ad8bb06a4773b71",
      "bytes": 1664
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a9abc25b921cbdce05f090e91781cabe86a577757b8e253bfe7473b3c6a55ce2",
      "bytes": 235304
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "70e35baed6d70da498cfe20f9d83400b782de16fc2826f94108fb6534a702024",
      "bytes": 1005
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7ce0215974856f291b1303cc1339a0d0a3aad9966277bab8db3efce21d104308",
      "bytes": 759
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "83f4cf775545e82046312e7da44a360fda558ee7687f44b4293747a97e868f22",
      "bytes": 1345
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "526852646fee59bb2090f821b1680370fd3fe35a9727cf8fb67180172483121c",
      "bytes": 954
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "61539fa3c7a5bffe310bcd11125da2b97e0b99af8ca3198417d8586fa6465cf9",
      "bytes": 269140
    }
  ],
  "estimated_tokens": 9794
}
-->

# Durable State Update — Chapter 963

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
1 and safe_through 963. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 963. Profile updates may replace only one
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
  "chapter": 963,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 963,
    "continuity_sources": [963],
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
    "Jin Mukyung reached Supreme Peak and killed the Demon Bird, also known as the Blood Soul Fat Demon, at Eight Spring Gorge; he is severely injured but continues fighting.",
    "The Shanxi forces have regained momentum and are routing the Keshik at Eight Spring Gorge; horns sound for Jamukha as the Keshik prepare to retreat.",
    "The Emperor remains gravely ill with Blood Soul Gu; saving him requires him to die once, and Taekyung’s treatment remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "Taekyung resolved to trust his allies rather than bear every burden alone."
  ],
  "continuity_sources": [
    962,
    961
  ],
  "open_questions": [
    "How will the battle at Eight Spring Gorge end, and what will Jamukha do after the horns sound?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will become of Temur and the followers he led into battle?"
  ],
  "safe_through": 962,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 철무백    | **Cheol Mubaek**   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 절정고수                | **Peak master** / **Peak martial artist** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 정파     | **orthodox faction**                             |                                                       |
| 대주     | **Squad Leader** / **Commander**             |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 신병이기 | **divine weapon** | Jin's description of White Flame. |
| 육부 | **Six Ministries** | The central government ministries. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 케식 | **Keshik** | Elite warriors serving the Golden Clan. |
| 검귀 | **Sword Demon** | Title used for the kind of swordsman Mukyung is said to resemble. |
| 마조 | **Demon Bird** | Title given by the revealed impostor who wore Chinggen’s face. |
| 청파낙조 | **Blue Wave, Falling Bird** | Technique name coined by the Demon Bird for Jin Mukyung’s strike. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 진무경 | 마조 | hostile opponents | you | blunt and insulting | Mukyung directly insults the Demon Bird, refusing to call him Master. |
| 마조 | 진무경 | hostile opponents | you | familiar and blunt, with admiration | Calls him a young Sword Demon and speaks to him with growing respect. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 962
- **Aliases:** Tiger of Mount Heng
- **Role:** Cheol Mubaek is the ninth-generation successor of the Shura Annihilating Fist and the Peak master known as the Tiger of Mount Heng, now out of seclusion and active in the rebuilding of the Mount Heng Sword Sect.
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** His master, the Fist Hero, was a great fist master whose arms were severed by the Blood Soul Fat Demon; he is a close friend and peer of Lee Cheonbaek, a paternal uncle and protector of Lee Seowol, and considers Jin Taekyung, Jin Mukyung, and Hyuk Mujin Benefactors for protecting Seowol and enabling the Mount Heng Sword Sect's survival.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 962
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 962
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and seeks strength in service of his family.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and Mukyung cherishes his promise to reunite with him.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 962
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung. He has fought beside the Jin Family in major battles, including the conflict with Mount Heng, and remains alert to threats connected with Dark Heaven. The Human Butcher has claimed him as a personal target in a planned attack.

## Korean source

```text
＃963화



부우우우!

밤공기를 뚫고 울려 퍼지는 의미 모를 뿔피리 소리를 들으며, 진무경은 문득 생각했다.

지금 이 순간, 자신의 몸뚱어리를 움직이는 것이 의지인지 본능인지.

서걱!

허공을 가로지르는 섬광.

빛을 뿌리며 휘둘린 검에 또 하나의 적이 쓰러진다.

헤아릴 수도 없이 숱한 반복에 따라 전신에 각인된 움직임은, 핏물을 흘리며 비틀거리는 와중에도 정확한 궤적을 그려 내고 있었다.

쉭, 푹!

등 뒤에서 쏘아진 돌격창을 피해 내고, 역수(逆手)로 쥔 검을 옆구리 사이로 찔렀다.

“커헉.”

귓가에 닿은 단말마.

진무경은 억눌린 신음을 토해 내는 적의 가슴에서 검을 뽑아냈다.

허물어지는 시체를 뒤로한 채 또 다른 먹잇감을 찾아 달려 나가는 그의 눈은, 믿을 수 없게도 고요하게 감겨 있었다.

그러나…….

‘선명하다.’

보이지 않아도 느껴진다.

아니, 보이지 않기에 오히려 주위의 모든 것이 더욱 생생하게 와닿았다.

어둠.

빛 한줄기 스며들지 않았던 그 칠흑 같은 어둠 속에서 이 년이라는 시간을 보냈다.

강해지기 위해서, 때로는 미치지 않기 위해서 검을 휘둘러야 했다.

시각이 무뎌진 만큼 다른 감각들은 이루 말할 수 없이 예리해졌고, 그것은 곧 기감(氣感)의 비약적인 상승을 뜻했다.

“주, 죽여!”

“고작 한 놈이다! 놈을 쓰러트린다면……!”

퍼걱!

섬뜩한 파육음과 함께 외침이 뚝 끊긴다. 끝없는 아수라장 속, 이제는 몇 번째인지도 모를 적을 쓰러트린 진무경은 거칠어진 호흡을 가다듬었다.

어지럽다.

몸뚱어리는 물에 젖은 솜처럼 무겁고, 정신은 꿈이라도 꾸는 것처럼 몽롱하다.

그가 마조라는 강적을 상대하며 얻은 것은 찰나의 깨달음뿐만이 아니었다.

극심한 내상.

온통 뒤틀리고 찢어진 오장육부와 혈도가 내지르는 비명이 귓전에 울리는 듯했다.

물론 진무경 자신도 알고 있었다.

마조를 쓰러트린 것은 천운(天運)에 가까웠다는 것을.

목숨을 도외시한 철무백과 위팽의 도움과 두 번 다시 펼칠 수 있을지 의문이 들 정도로 완벽한 일격.

그리고 마지막으로 강기와 맞설 수 있는 신병이기(神兵利器)의 존재까지.

셋 중 하나라도 어긋났다면, 지금 이 자리에 서 있는 것은 진무경이 아닌 마조였을 것이다.

하지만…….

‘빌어먹을.’

아무런 대가 없이 주어지는 결과는 없다.

울컥, 솟구치는 핏물을 삼키며 진무경은 숨을 삼켰다.

자꾸만 손아귀에서 미끄러지려는 검자루를 다시 한번 굳게 말아쥐고, 자신을 포위한 채 두려움과 분노가 섞인 숨결을 토해 내는 적들을 모든 감각으로 느꼈다.

쉴 새 없이 울려 퍼지는 쩌렁쩌렁한 함성과 비명 너머에서 들려온, 누군가의 희미한 목소리도 함께.

“어서, 어서 가게.”

늙수그레한 그 음성의 주인이 누구인지, 진무경은 이미 알고 있었다.

“안 갑니다. 아니, 못 갑니다.”

진무경은 감았던 눈을 떴다. 이마에서 흐른 피로 붉게 물든 시야 속, 한쪽 무릎을 꿇은 채 헐떡이는 철무백과 위팽의 모습이 보였다.

“돌아갑니다. 모두 함께.”

굳은 의지가 담긴 진무경의 대답에 위팽이 너털웃음을 흘렸다.

“거보십시오. 제가 뭐랬습니까. 진씨 가문 사람들 고집 하나는, 흡.”

쿨럭. 투두둑.

말을 잇지 못하고 핏물을 쏟아내는 위팽의 모습에 진무경의 눈빛이 깊게 가라앉았다.

같은 토혈(吐血)도 색과 내용물에 따라 위급함이 다르다.

그런 의미에서 현재 위팽의 상태는, 정신을 잃지 않는 것만으로도 기적에 가까웠다.

“젠장. 피만 몇 됫박을 쏟았더니 이제는 고작해야 한 줌이구먼.”

아무렇지 않은 듯 천연덕스럽게 말해 보지만, 사태의 위급함은 위팽 그 자신도 안다. 그는 자꾸만 감기려는 눈동자에 애써 힘을 주며 진무경을 바라보았다.

“이 공자. 한마디만 해도 되겠습니까?”

“아닙니다. 더 이상 말씀하지 마십시오. 최대한 기력을…….”

“무경아.”

“……!”

순간 덜컥 굳은 진무경을 바라보며, 위팽은 피에 젖은 이빨을 드러내며 웃었다.

“가라. 고집 그만 부리고.”

“…….”

“나도, 여기 계신 철 대협께서도, 그리고 너 스스로도 알 것이다. 무엇이 최선인지는.”

진무경은 이를 악물었다.

“아직, 아직 늦지 않았습니다. 돌아갈 수 있습니다.”

“그래, 돌아갈 수 있다.”

위팽이 부드럽게 덧붙였다.

“너 혼자서라면.”

“그게 무슨……!”

“더 늦기 전에 떠나라. 지금이라면 충분히 퇴로를 뚫을 수 있을 거다.”

아군의 피해를 최대한 줄이기 위해 적진 깊숙이 파고들어 전투를 벌인 것은 옳은 선택이었으나, 한편으로는 뼈아픈 패착이기도 했다.

지금 이 순간에도 수백의 적들이 주위를 둘러싼 채, 호시탐탐 때를 노리고 있었으니까.

그리고 위팽과 철무백은 그 잔인한 현실을 정확히 직시하고 있었다.

항산을 호령하던 늙은 호랑이도, 귀신 같은 검술을 펼치던 절정의 검객도 더는 없다.

호랑이의 발톱은 부러졌고, 귀검의 검술은 으스러진 팔과 함께 사라졌기에.

그것이 단 한 순간, 일세를 풍미했던 전대의 마두(魔頭)의 손을 묶기 위해 그들이 각오한 대가였기에.

하지만…….

“너는, 무경이 너만큼은 살아야 한다.”

“자네가 태원진가의 이공자이기 때문이 아닐세.”

위팽과 철무백은 금방이라도 꺼질듯한 눈을 들어 진무경을 바라보았다.

지금 그들의 눈동자에 비친 청년의 이름은 진무경이 아니었다.

자신들의 목숨을 바쳐서라도 살려야 할 희망이요, 언젠가 수십, 수백 배로 적들에게 되돌아갈 복수 그 자체였다.

“살아라. 어떻게든 살아남아.”

“그리고 돌아오게. 우리에게, 저놈들에게.”

봄. 여름. 가을. 겨울.

사계(四季)는 변함없이 반복된다. 그 시간 속에서 사라지는 것은 사람뿐이다.

그렇기에 위팽은 믿었다. 철무백은 확신했다.

오늘 자신들에게 일찍 찾아온 이 겨울이, 언젠가는 적들에게도 찾아갈 것이라고.

앞으로 수많은 이들을 지켜낼 태원진가의 젊은 검귀가, 놈들을 쓰러트릴 것이라고.

“그러니…….”

위팽은 희미한 미소와 함께 진무경을 바라보았다.

과거 청년이 소년이었던 시절, 검을 가르쳐 달라며 찾아왔던 그 모습을 떠올리며.

“당장 이 자리를 떠나라. 진무경, 아니 진천대주.”

“……!”

“이건 본가의 상급자로서 내리는 명령이다.”

순간 말문이 막힌 진무경은 눈을 질끈 감았다.

그도 안다.

무엇이 최선인지. 더 많은 이들을 살리기 위해서라면 어떤 선택을 해야 하는지.

하지만 발걸음은 떨어지지 않았다.

처음 검을 들었을 때, 무(武)와 함께 배웠던 그 가르침을 진무경은 여전히 기억하고 있었으니까.

‘의협(義俠).’

강자를 누르고 약자를 돕는다.

불의를 외면하지 않으며, 신의를 목숨처럼 지킨다.

그것이 협객이라 했다. 올바름을 외치는 정파의 무림인이 가져야 할 자세라고 배웠다.

그저 검이 좋아서, 강해지기 위해서 무공을 익혔으나 그 두 글자에 실린 무게와 의미는 잊어 본 적이 없었다.

‘무엇이 최선인가.’

위팽과 철무백이 말하고, 진무경 스스로도 적을 쓰러트리면서도 마음속으로 끝없이 되뇌었던 그 생각.

그리고 진무경은 불현듯 깨달았다.

“두 분이 하신 말씀은 틀렸습니다.”

스륵.

감았던 눈을 뜬 그의 발끝이 피에 젖은 땅을 짓눌렀다.

피로와 고민이 뒤섞여 파르르 떨리던 검 끝은 한 치의 흔들림도 없이 적들을 향해 겨누어졌다.

“무엇이 최선이며 최악이냐를 생각하기 이전에, 한 가지를 잊어서는 안 됩니다.”

쉭, 서걱!

조심스럽게 접근해 오던 유목민의 상반신이 비스듬히 갈라진다. 돌격창과 함께 주인의 몸뚱어리를 베어 낸 새하얀 검신을 타고 핏방울이 굴러떨어졌다.

“무엇이 옳은가.”

진무경은 물 흐르듯 움직였다. 찰나의 깨달음이 서서히 녹여진 검을 타고 흐릿해졌던 푸른 검기가 넘실거렸다.

촤아악!

몽글몽글한 피 안개가 맺힌다. 단 일 검으로 세 명의 케식을 베어 낸 진무경은 숨이 끊긴 시체의 손에 들려 있던 신월도를 빼앗아 흩뿌렸다.

“무엇이 후회하지 않을 선택인가.”

쐐액! 푹!

공간을 가로지르는 한 줄기의 빛. 그 끝에 남은 비명조차 들리지 않는 죽음.

각궁에 활시위를 매기고 있던 누군가의 죽음을 신호탄 삼아, 주변을 빽빽하게 포위하고 있던 적들이 억누르고 있던 두려움과 분노를 터트리며 일제히 달려들었다.

쉬쉬쉬쉭!

슈확! 캉!

어둠 속에서 번뜩이는 섬광.

날아드는 비도를 쳐낸 진무경을 향해 십여 자루의 돌격창과 신월도가 짓쳐 들었다.

피핏!

뜨겁다. 나부끼는 바람에 핏방울이 뒤섞인다.

머리로는 피할 수 있었으나 몸이 그것을 거부한다. 전신 곳곳을 스쳐 지나간 날붙이의 흔적에서 불같은 통증이 일었다.

아니, 그것은 어쩌면 진무경이 스스로에게 느낀 실망과 분노일지도 몰랐다.

아주 잠시나마, 올바름이 아닌 최선에 대해 생각했던 자신에 대한 부끄러움.

‘이것만이, 옳은 선택이다.’

복잡하던 머릿속이 맑게 갠다. 진무경은 온 힘을 다해 이를 악물었다.

으적.

입 안에 감도는 피비린내.

고통이 또 다른 고통으로 잊혀진다. 조금씩 흐려지던 정신이 되돌아온다.

그리고 그와 동시에.

츠츠츠.

작은 파도처럼 넘실거리던 푸른 검기가 하나로 뭉쳤다.

검을 쥔 자의 의지에 따라 잇고, 융화되고, 이내 하나가 되어 아름다운 궤적을 그렸다.

이제는 망자가 되어 버린 어느 늙은 마두가 보았다면, 크게 소리 내어 웃었을 만큼 완벽한 궤적을.

솨아아악.

바람이 지워졌다. 서늘한 한기(寒氣)가 어둠 속을 갈랐다.

진무경을 향해 쏘아지던 열 명의 케식 십인장은 약속이라도 한 것처럼 눈을 부릅떴다.

더불어, 마침내 이해할 수 있었다.

마지막 순간, 마조가 무엇을 보았는지.

그 강대한 무위를 지닌 괴물이 어떤 감각을 느꼈는지.

스릉.

유형화된 기운으로 빛나던 돌격창이, 신월도가 신음했다.

힘없이 사그라지는 각자의 기운과 함께 토막난 애병의 파편을 바라보며, 열 명의 절정고수는 기울어지는 시야를 느꼈다.

“거, 검귀(劍鬼)…….”

푸화아악!

허공을 물들이는 짙은 피 분수.

투두둑. 소나기처럼 쏟아져 내리는 찐득한 핏물 아래, 푸른 파도와 같은 일격으로 열 마리의 새를 떨어트린 진무경은 나직이 뇌까렸다.

“그 약속, 지켜 주마.”

청파낙조(靑波落鳥).

이름 없던 일격의 첫 먹잇감이 된 늙은 마두를 떠올리며, 진무경이 얼어붙은 적들을 향해 발걸음을 내디딘 그 순간이었다.

“누구와 무슨 약속을 했는지, 나도 들어 볼 수 있겠나?”

“……!”

진무경의 전신이 덜컥 굳었다.

갑작스럽게 들려온 낯선 목소리의 주인은, 불과 일장밖에 되지 않는 거리에서 그를 바라보고 있었다.

“네놈은…….”

“자무카 칸이시여!”

누군가의 외침이, 아니 너나 할 것 없이 사방에서 터져 나온 그 부름이 진무경의 목소리를 파묻는다.

‘자무카.’

목소리와는 달리 익숙한 이름이었다.

본대보다 앞서 산서성을 침범한 일천의 선봉대를 궤멸시켰던 그 날, 가장 강했던 유목민 전사가 죽음을 맞이하며 남긴 말은 아직도 뇌리에 또렷하게 남아 있었으니까.



‘그분께서, 자무카 칸께서 네놈을 벌할 것이다. 혈육, 친구, 터전. 모든 것을 빼앗고 불태울 것이다.’



그리고 지금 이 순간, 마침내 자무카를 대면한 진무경은 깨달았다.

그 저주나 다름없던 말에는, 일말의 과장조차 없었음을.

“자네로군. 그 검귀가.”

자무카.

초원의 절대자가 진무경을 향해 걸음을 뗀 바로 그 순간.

드드드득.

작지만 또렷한 진동이, 모두의 발끝을 통해 전해졌다.
```

## Final English reading copy

```markdown
# Chapter 963

*Boooooo!*

Listening to the meaningless horn echo through the night, Jin Mukyung suddenly wondered:

Was it his will or his instinct that was moving his body right now?

*Shhk!*

A flash swept through the air.

Another enemy fell beneath the sword that scattered light as it swung.

The movements carved into his whole body through countless repetitions still traced their paths with precision, even as he staggered and bled.

*Shhk, thud!*

He dodged a thrusting spear from behind, then drove the sword in his reverse grip between the enemy’s ribs.

“Guh!”

The death rattle reached his ears.

Jin Mukyung pulled his sword from the chest of the enemy who had let out the stifled groan.

Leaving the crumpling corpse behind, he raced off to find another target. His eyes were—impossibly—calmly closed.

And yet…

*It’s all so clear.*

He could feel everything, even without sight.

No—with his eyes closed, everything around him seemed all the more vivid.

Darkness.

He had spent two years in that pitch-black darkness, where not a single ray of light could seep in.

He had to swing his sword to grow stronger—and sometimes, to keep himself from going mad.

As his sight dulled, his other senses had sharpened beyond measure. That meant his Qi Sense had improved by leaps and bounds.

“K-kill him!”

“He’s only one man! If we take him down…!”

*Crunch!*

A grisly sound of flesh being torn cut off the shout. Amid the endless carnage, Jin Mukyung took down yet another enemy—he had lost count of how many—and steadied his ragged breathing.

He was dizzy.

His body was as heavy as waterlogged cotton, and his mind was hazy, as if he were dreaming.

The fierce battle against the Demon Bird had given him more than a moment of enlightenment.

A severe Internal Injury.

His innards and acupoints were twisted and torn, their cries of pain seeming to ring in his ears.

Of course, Jin Mukyung knew it, too.

Defeating the Demon Bird had been close to a stroke of heavenly luck.

Cheol Mubaek and Wipeng had helped him, heedless of their own lives. He had landed a perfect strike—one he might never be able to perform again.

And finally, there had been a divine weapon capable of standing up to Force.

If even one of those three things had gone differently, the man standing here now would have been the Demon Bird, not Jin Mukyung.

But…

*Damn it.*

Nothing came without a price.

Jin Mukyung swallowed the blood surging into his mouth and caught his breath.

He tightened his grip on the hilt, which kept slipping from his grasp, and felt the enemies surrounding him with every sense. They breathed in fear and rage.

Beyond the ceaseless shouts and screams, he also heard someone’s faint voice.

“Hurry. Go on.”

Jin Mukyung already knew who owned that hoarse, elderly voice.

“I’m not going. No—I can’t go.”

Jin Mukyung opened his eyes. Through his vision, stained red with blood running down his forehead, he saw Cheol Mubaek and Wipeng gasping on one knee.

“We’re going back. All of us.”

At Jin Mukyung’s firm reply, Wipeng let out a hearty laugh.

“See? What did I tell you? Jin Family people are stubborn as hell, hu—”

He broke off, coughing up blood that pattered onto the ground. Jin Mukyung’s gaze sank as he watched.

The severity of coughing up blood depended on its color and what came with it.

By that measure, Wipeng’s condition was so dire that it was a miracle he hadn’t lost consciousness.

“Damn it. I’ve coughed up bucketfuls of blood, and now all I can manage is a handful.”

He tried to sound casual, but Wipeng himself knew how dire things were. He forced open his eyes, which kept wanting to close, and looked at Jin Mukyung.

“Second Young Master. May I say one thing?”

“No. Don’t say anything more. Save your strength as much as you can—”

“Mukyung.”

“……!”

Wipeng smiled at Jin Mukyung, who had gone rigid in an instant, showing his teeth stained with blood.

“Go. Stop being so stubborn.”

“……”

“I know it, Great Hero Cheol here knows it, and you know it yourself. What the best choice is.”

Jin Mukyung clenched his teeth.

“It’s not too late. We can still go back.”

“Yes. We can go back.”

Wipeng added gently:

“If you go alone.”

“What are you—!”

“Leave before it’s too late. You can still break through and make your escape.”

It had been the right choice to push deep into enemy territory and fight there, to minimize the casualties among their allies. But it had also been a bitter mistake.

Even now, hundreds of enemies surrounded them, waiting for a chance to strike.

Wipeng and Cheol Mubaek saw that cruel reality clearly.

The old tiger who had once commanded Mount Heng, and the Peak swordsman with his ghostly swordplay, were gone.

The tiger’s claws were broken, and the Ghost Sword’s art had disappeared along with his shattered arm.

That was the price they had accepted to tie down, for just one moment, the hand of a fiend who had once shaken an entire age.

But…

“You, Mukyung—you, of all people, have to live.”

“It’s not because you’re the Second Young Master of the Jin Family of Taiyuan.”

Wipeng and Cheol Mubaek looked at Jin Mukyung through eyes that seemed ready to go dark at any moment.

The young man reflected in their eyes now was not Jin Mukyung.

He was the hope they had to save, even if it cost them their lives—the very revenge that would one day come back at their enemies tenfold, a hundredfold.

“Live. Survive, no matter what.”

“And come back. To us—and to them.”

Spring. Summer. Fall. Winter.

The seasons passed in an unchanging cycle. In all that time, only people disappeared.

That was why Wipeng believed. Cheol Mubaek was certain.

The winter that had come early for them today would one day come for their enemies, too.

The young Sword Demon of the Jin Family of Taiyuan, who would protect countless people in the years to come, would bring them down.

“So…”

Wipeng looked at Jin Mukyung with a faint smile.

He remembered the young man back when he was a boy, coming to ask him to teach him the sword.

“Leave this place right now. Jin Mukyung—no, Commander of the Heaven Shaking Squad.”

“……!”

“This is an order from your senior in the family.”

Jin Mukyung was struck speechless. He squeezed his eyes shut.

He knew.

What the best choice was. What he had to do to save more people.

But his feet wouldn’t move.

Because Jin Mukyung still remembered the lesson he had learned alongside martial arts when he first picked up a sword.

*Chivalry.*

Suppress the strong and help the weak.

Never turn away from injustice, and uphold one’s word as dearly as one’s life.

That was what it meant to be a chivalrous hero. It was the way of life a martial artist of the orthodox faction, one who stood for what was right, was supposed to follow.

He had learned martial arts because he loved the sword, because he wanted to grow stronger. But he had never forgotten the weight and meaning behind those two words.

*What is the best choice?*

Wipeng and Cheol Mubaek had said it, and Jin Mukyung had endlessly repeated it in his heart even as he cut down his enemies.

And then, suddenly, Jin Mukyung understood.

“You’re both wrong.”

*Shhk.*

He opened his eyes. His toes pressed into the blood-soaked earth.

The tip of his sword, which had trembled with fatigue and doubt, now pointed at the enemy without the slightest wavering.

“Before thinking about what’s best or worst, there’s one thing you mustn’t forget.”

*Shhk, shhk!*

A nomad who had approached cautiously was cut diagonally in half. Blood trickled down the white blade that had sliced through his body and the thrusting spear with it.

“What is right?”

Jin Mukyung moved like flowing water. Blue Sword Energy, faint moments before, rippled along his sword, now slowly steeped in his moment of enlightenment.

*Shwaaash!*

A thick blood mist bloomed. Jin Mukyung cut down three Keshik with one stroke, then snatched the crescent saber from the hand of a corpse and flung it.

“What choice will I have no regrets about?”

*Whoosh! Thud!*

A single streak of light cut through the air. At its end, death came without even a scream.

The death of the one stringing a bow on his composite bow became the signal. The enemies packed tightly around them erupted with pent-up fear and rage, charging all at once.

*Shhk-shhk-shhk!*

*Fwoosh! CLANG!*

Flashes glinted in the darkness.

Jin Mukyung knocked away the throwing blades, but a dozen thrusting spears and crescent sabers came down on him.

*Pit, pit!*

It was hot. Blood droplets mingled with the wind whipping past.

He knew he could avoid them, but his body refused. The places all over his body where blades had grazed him burned with pain.

No—perhaps it was the disappointment and anger he felt toward himself.

The shame of having thought, even for a brief moment, about what was best instead of what was right.

*This is the only right choice.*

His muddled thoughts cleared. Jin Mukyung clenched his teeth with all his might.

*Crack.*

The stench of blood filled his mouth.

One pain drove out another. His fading consciousness returned.

And at the same time—

*Tsutsutsu.*

The blue Sword Energy, rippling like small waves, came together as one.

Following the will of the swordsman holding it, it joined, blended, and finally became one, tracing a beautiful arc.

An arc so perfect that the old fiend, now among the dead, would have laughed out loud if he had seen it.

*Shwaaaash.*

The wind disappeared. A chill cleaved through the darkness.

The ten Keshik squad leaders charging toward Jin Mukyung opened their eyes wide as if on cue.

And at last, they understood.

What the Demon Bird had seen in his final moments.

What the monster with such overwhelming martial prowess had felt.

*Shing.*

The thrusting spears, shining with tangible energy, groaned. So did the crescent sabers.

As the energy in each weapon faded away, the ten Peak martial artists watched fragments of their beloved weapons fall to pieces. They felt their vision tilt.

“S-Sword Demon…”

*Fwoosh!*

A dense fountain of blood stained the air.

Beneath the sticky blood pouring down like a shower, Jin Mukyung had felled ten birds with a single strike, like a blue wave. He murmured softly.

“I’ll keep that promise.”

*Blue Wave, Falling Bird.*

Remembering the old fiend who had become the first prey of that once-nameless strike, Jin Mukyung stepped toward the frozen enemies.

And at that very moment—

“May I ask who you made that promise to?”

“……!”

Jin Mukyung’s whole body went rigid.

The owner of the unfamiliar voice that had suddenly spoken stood only about ten feet away, looking at him.

“You…”

“Jamukha Khan!”

Someone shouted. No—the call erupted from every direction, all at once, drowning out Jin Mukyung’s voice.

*Jamukha.*

Unlike the voice, the name was familiar.

The words spoken by the strongest nomad warrior as he died—the day Jin Mukyung annihilated the thousand-man vanguard that had invaded Shanxi Province ahead of the main force—were still vivid in his mind.

*He will punish you—Jamukha Khan will. He’ll take everything from you and burn it: your family, your friends, your home.*

And now, as Jin Mukyung finally faced Jamukha, he understood.

There hadn’t been even the slightest exaggeration in those words, which were little more than a curse.

“So it’s you. The one they call the Sword Demon.”

Jamukha.

The supreme ruler of the grasslands took a step toward Jin Mukyung.

*Rrrumble.*

A small but unmistakable tremor traveled through everyone’s feet.
```
