<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1029.txt",
      "sha256": "256aad66dd69b32573170b13ac552ab96e3581beb62be0fb7d155ec0e7ac77bf",
      "bytes": 13075
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d62a79b71e85082f619647076807000e1c93bb0894242498fbabd9542da296a4",
      "bytes": 1073
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a66501f684135b54b6631e5c2962356b020be649c6bbbe0bb070c85ef55335cd",
      "bytes": 239693
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "a6e9224f792b1a21f43d5a5a01b7ab99f32068f495710d98d1ec6807536a2d90",
      "bytes": 875
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1477fe717b7f08cab6a2261f9e384612bb6d9d1888c6804c28a8bb698869df79",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "6aa66db0068d254369edd14bca07cda6ef24666b4c85759d58f8726c9cbdbf5e",
      "bytes": 1502
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "799f210f4817c10447e848c473cf391912c4c82c7622bcf1ecd0df07082ff7c6",
      "bytes": 1069
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "03a1c1209fa03435949a49d66244a6dda23347dc500c510ad3bf1c1650d99d34",
      "bytes": 279013
    }
  ],
  "estimated_tokens": 9896
}
-->

# Durable State Update — Chapter 1029

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
1 and safe_through 1029. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1029. Profile updates may replace only one
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
  "chapter": 1029,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1029,
    "continuity_sources": [1029],
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
    "The Blood-Sword Demon Lord once served the Heavenly Demon as a favored guard dog and now serves the Lord of Heaven.",
    "The Blood-Sword Demon Lord killed a thousand people with a gesture and watched Jin Taekyung with eager fascination.",
    "Jin Taekyung has reached the realm of the Ten Kings and is recognized as its eleventh giant.",
    "The First Elder of the Three Elders of Tianshan is alive but wounded after the fight; Taekyung killed the Second Elder and Sama Pyo killed the Third.",
    "Sama Pyo used hidden daggers to kill the Third Elder while Taekyung engaged the three elders."
  ],
  "continuity_sources": [
    1027,
    1028
  ],
  "open_questions": [
    "When did Dark Heaven and the Lord of Heaven emerge, and did Dark Heaven cause the Great Faction War?",
    "Who were the thousand people killed by the Blood-Sword Demon Lord, and what became of the rest of the meeting party?",
    "What is the Lord of Heaven’s identity and purpose?"
  ],
  "safe_through": 1028,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 열화문    | **Fire Gate Clan**               |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 선배     | **Senior**                                   |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 민첩               | **Agility**                    |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 삼노 | **Three Old Men** | Mocking designation used by the Western Heaven Demon Lord for the aged Qilian Three Fiends. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 기경팔맥 | **Eight Extraordinary Meridians** | The eight extraordinary meridians of wuxia physiology. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 천산삼노 | **Three Elders of Tianshan** | The three former Demonic Cult fiends serving the Blood-Sword Demon Lord. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 혈검마군 | 삼노 | former Demonic Cult fiend to subordinate | Elder Three | familiar and contemptuous | Addresses the wounded elder as 삼노 while asking how he compares to the Fire King. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 사마표 | 삼노 | enemy addressing an elder of the Three Elders of Tianshan | you | casual and taunting | Sama Pyo answers the Third Elder’s accusation and taunts him while attacking. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1028
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Contemptuous of his former master and certain of his new cause, he treats the weak with ruthless disdain yet takes sincere delight in being recognized and openly admires formidable opponents.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He once served the Heavenly Demon and now serves the Lord of Heaven; he has been ordered not to kill Jin Taekyung and wants to meet him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1028
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1028
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1028
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and calculating, he is protective of Taishan and pragmatic in combat; he recognizes that his father's ruthless, survival-driven worldview shaped him, even as its influence weighs on him.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan and is Sima Gong's son and heir; his father's ruthless treatment of family shaped his rise and remains a source of inner constraint. He joined the Fire Dragon Pavilion intending to use Jin Taekyung, and Sima Gong has now ordered him to spy on Taekyung's group. He was Ju Hwaran's former fiancé in a political engagement and is openly hostile toward fellow member Song Ilseom.

## Korean source

```text
＃1029화



툭. 투두둑.

뜨겁고, 축축하다.

분수처럼 높게 솟구쳤던 핏물이 정수리를 적시며 떨어져 내리고 있었다.

이미 목이 잘린 시체가 된 누군가는, 앞으로 영영 느낄 수 없는 감각이다.



- [Lv.135 고궁보]를 처치했습니다!

- 대량의 명성을 획득했습니다.

- 대량의 경험치를 획득했습니다!



철퍽!

뒤늦게 중심을 잃은 신형이 고여 있던 피 웅덩이 위로 허물어졌다.

앞서 미처 반응할 새도 없이 몸뚱어리에서 떨어져 나온 이노(二老)의 머리는, 어리둥절한 표정으로 자신의 의형제를 올려다보고 있었다.

정확히는, 이제 이승에 남아 있는 유일한 의형제를.

“이제 한 놈, 아니. 둘.”

때맞춰 들려온 적천강의 한마디가 삼노의 최후를 알린다. 고개를 돌려 바라보니, 썩은 통나무처럼 엎어진 놈의 뒤통수에 삐죽 튀어나와 있는 은빛 날붙이가 보였다.

푸슉.

바람 빠지는 소리와 함께 점점이 떨어지는 핏물.

숨이 끊어진 삼노의 미간 사이에 박혀 있던 비수를 회수하던 사마표가, 나와 눈이 마주치자 어깨를 으쓱해 보였다.

“혹시 내가 괜한 짓을 한 건가?”

내가 대답했다.

“그래.”

“각주 몫이었다면 미안하군. 살려두면 화근이 될 것 같…….”

“그거 말고.”

사마표의 시선에 의문이 깃든 그때, 나는 불덩이처럼 뜨거운 숨결을 내뱉으며 말을 이었다.

“그렇게 손쉽게 죽이지는 말았어야지.”

경험치 따위는 중요하지 않다. 누구의 손에 죽느냐도 마찬가지다.

놈은 더욱 큰 고통을 느꼈어야 했다.

이렇게 편하게, 한순간에 이승을 떠나선 안 됐다.

가장 먼저 쇄골이 뜯겨 나가고, 곧이어 한쪽 팔이 잘리고, 결국은 몸 안의 기경팔맥(奇經八脈)이 갈기갈기 찢어진 후에야 목이 잘려 나간 이노가 그랬던 것처럼.

“더는 나서지 마. 단 한 걸음도.”

마치 남의 것처럼 낯선, 황량한 목소리.

지금 이 순간 내가 어떤 모습을 하고 있는지, 나 스스로도 잘 모르겠다.

다만 침잠하게 굳은 사마표와 적천강의 표정이, 그리고 악귀를 마주한 듯이 얼어붙어 있는 일노의 모습이 조금이나마 그 사실을 짐작하게 만들었다.

“괴, 괴물…….”

파르르 떨리는 신형과 음성.

나는 눈 깜짝할 새에 평생을 동고동락한 두 의제(義弟)를 잃은 늙은 마두의 눈빛에서, 숨길 수 없는 분노와 그보다 더욱 짙고 깊은 두려움을 보았다.

철벅.

느릿하게 나아가는 걸음.

어느덧 지면을 축축하게 적신 핏물 때문일까, 유난히도 크게 울려 퍼진 걸음 소리에 일노가 화들짝 놀라며 뒷걸음질 쳤다.

아니, 두 팔을 지지대 삼아 엉덩이를 뒤로 끌었다.

이미 양쪽 무릎이 산산이 부서진 놈으로서는, 오직 그것만이 나로부터 조금이라도 멀어질 수 있는 유일한 방법이었으니까.

“오, 오지 마! 오지 말란 말이다!”

비명 같은 외침과 함께 일노가 팔을 흩뿌렸다.

퍼엉!

파공성이 들리기도 전에 고개를 틀었다. 유형화된 장력(掌力)이 조금 전까지 내 머리가 있던 공간을 터트린다.

비록 이미 반병신이 되었지만, 놈의 몸 안 깊숙이 흐르는 강대한 공력은 꺼지지 않는 불꽃처럼 타오르고 있었다.

물론…….

“더 해봐.”

내 눈에 비친 그 움직임은 이루 말할 수 없이 투박하고, 형편없이 느렸으며, 그랬기에 모든 것이 곧 허점투성이였다.

“으아아아아!”

비명인지, 기합인지 분간이 되지 않는 외침.

펑! 펑! 퍼엉!

혼비백산한 일노가 뻗어 낸 장력에 압축된 공기가 연달아 터져 나간다.

맹렬하게 쏘아지는 장력의 여파에 머리카락이 나부끼고, 옷깃과 함께 피부가 찢겨 나갔다.

그리고 그것이, 일노가 할 수 있었던 최후의 발악이었다.

덥석, 우두둑!

번개처럼 놈의 손목을 움켜쥐고, 그대로 꺾었다.

이건 복잡한 묘리가 스며든 금나수(禁拿囚)도, 공력이 담겨 있는 한 수도 아니다.

순수한 근력과 민첩성.

인간에게 부여된 한계를 아득히 벗어난 그 힘과 속도는, 나약한 뼈와 살을 우습게 짓뭉개 버렸다.

“크……헉!”

엄청난 격통으로 일그러진 얼굴과 억눌린 신음.

하지만 나는 안다.

눈앞의 늙은 마두가 이 정도로 모든 것을 포기할 만한 인물이었다면, 천산삼노라는 별호는 이미 오래전에 잊혔으리라는 것을.

슈확! 쾅!

갈고리처럼 휘어진 다섯 개의 손가락이 섬광처럼 지면을 찍었다.

단 한 걸음.

상대의 움직임을 읽고 그보다 앞서 물러난 나는, 아슬아슬하게 옷깃을 스치고 지면 깊숙이 틀어박힌 일노의 손등을 발로 짓밟았다.

콰드득!

천근의 무게가 실린 발바닥을 타고 뼈마디가 으스러지는 감각이 전해진다.

상상치도 못한 격통과 두려움으로 부릅떠진 일노의 눈동자에, 담담한 표정을 한 내 모습이 비치고 있었다.

“그렇게 보지 마.”

퍽.

정확히 턱을 가격당한 놈의 고개가 돌아간다. 핏물과 함께 싯누런 이빨이 사방으로 튀었다.

“그런 눈으로 쳐다보면.”

퍽.

한 번 더.

“지금 당장.”

퍽.

다시 한번 더.

“죽이고 싶어지잖아.”

뻑!

찐득한 핏물이 주먹에 달라붙었다.

나는 이제 미동조차 하지 않는 일노의 머리카락을 휘어잡은 채, 천천히 허리를 펴고 일어섰다.

“이제 겨우 시작인데, 안 그래?”

이건 일노를 향한 말이 아니다.

상기 어린 얼굴로 십여 장 밖에서 이 모든 사태를 지켜보던, 단 한 번의 손짓으로 천 명의 목을 떨어트린 괴물에게 건네는 말이다.

짝. 짝. 짝.

느릿한 박수 소리와 함께, 혈검마군이 경탄 어린 눈빛으로 나를 바라보았다.

“멋지군. 아니, 아름다워.”

그 대답을 듣자 몸 안의 피가 차갑게 식는 듯했다.

극도의 분노가 머릿속을 지배한 지금 이 순간에도, 놈의 반응은 예상했던 기준을 아득하게 초월하고 있었다.

“그래, 무림인이라면 응당 이래야지. 잔인하고 철저하게 짓밟아야 그게 진짜 싸움이지. 안 그런가?”

혈검마군은 싱글벙글 웃고 있었다.

중요한 전력이자 자신의 수족인 천산삼노 중 둘이 죽고, 하나가 불구가 되었음에도 그는 오히려 조금 전보다 훨씬 더 즐거워 보였다.

“미친……놈.”

“내가? 아니면 자네가?”

“뭐?”

“아니, 그렇잖은가.”

나를 향해 눈을 깜빡이던 혈검마군이 두 팔을 활짝 펼친 채 빙그르 돌았다.

“내 모습을 보게. 복색이 영 칙칙해서 그렇지, 지금 자네에 비하면 아주 점잖아 보이지 않나?”

“……!”

“아, 오해하지는 말게. 보기 흉하다는 소리는 절대 아니니까. 오히려 내 입장에서는 꽤 친숙하기도 하고…… 뭐, 여러모로 보기 좋은 광경이었네.”

흡족하게 웃고 있는 혈검마군의 모습에, 나는 문득 숨이 막혔다.

친숙하다고 했다. 보기 좋다고 했다.

다름 아닌 혈검마군이. 늙고 악랄한 대마두가.

머리부터 발끝까지 피를 뒤집어쓴 지금의 내 모습을.

단순한 복수가 아닌, 더욱 큰 고통을 안겨 주는 것에 미쳐 있던 조금 전의 나를.

“이건. 이건 그러니까…….”

“그만.”

더없이 익숙한, 동시에 평소와는 달리 착 가라앉은 목소리가 내 뒷말을 가로막았다.

“그만하면 됐다.”

성큼 앞으로 나선 적천강을 향해, 나는 불현듯 묻고 싶어졌다.

누구에게 하는 말인지.

내게? 아니면 혈검마군에게?

그도 아니면 둘 모두에게?

하지만 묻지 않았다. 아니, 묻지 못했다는 표현이 정확했다.

차마 조금 전의 내 모습이, 피와 복수에 미친 마두(魔頭)와 닮아 있었느냐 묻기에는 순간 겁이 났으니까.

그러나 나도 모르게 경직되어 버린 몸과 마음을 다시 다잡을 수 있었던 이유는, 아이러니하게도 바로 그 마두 덕분이었다.

“이런 상황에서 맥을 끊다니, 선배도 너무 하시는구려. 나름 뜻깊은 대화를 나누고 있었는데.”

고개를 절레절레 내젓는 혈검마군을 향해, 적천강이 가래를 탁 뱉었다.

“좆이나 까거라. 노부는 네놈 같은 후배 둔 적 없으니.”

“그건 나도 알고 있소만, 오랫동안 선배를 흠모해 온 터라 어쩔 수 없소. 짝사랑으로라도 만족해야지.”

“산 채로 숯덩이가 되어야 그 주둥이를 닥치겠느냐?”

“아마도 그럴 거요. 사실, 그 부분 때문에 살짝 실망하긴 했소. 최소한 저 셋 중 한 놈은 그렇게 될 줄 알았거든.”

짐짓 한숨을 내쉰 혈검마군이 말을 이었다.

“오래전, 구화산에서 있었던 일을 듣고 내가 어찌나 설레었는지 모를 거요. 말로만 들었던 열화문의 후예라니! 감히 선배를 건드린 그 멍청한 것들이 죄다 잿가루가 되었다는 소식을 듣고 얼마나 통쾌하던지.”

“뭐라?”

“그렇지 않소? 산 채로 타들어 갔으니 그 얼마나 고통스러웠을 것이며, 그만큼 확실하고 처절한 보복이 어디 있겠소?”

“……!”

“주위의 모두가 미친 늙은이라며 치를 떨었지만, 나만큼은 아니었소. 그날부터 줄곧 선배를 흠모하게 되었지.”

샛별처럼 눈을 반짝이는 놈의 모습에 적천강도, 나도, 침착하게 상황을 주시하던 사마표마저도 말문이 막힌 듯했다.

마두.

지금까지 본 그 누구보다, 혈검마군은 마두라는 단어에 어울리는 미친놈이었다.

혈(血)이라는 글자가 왜 별호에 들어갔는지 가장 확실하게 이해가 되는.

그리고 그런 혈검마군에게 있어, 천산삼노의 존재는 그저 곁에 두고 기르던 가축에 지나지 않았다.

“저 머저리들도 마찬가지지. 정마대전 때만 해도 조금만 전세가 기울어지면 도망치기 바쁘다가, 오늘은 제 주제들도 모르고 나섰으니 응당 죽어 마땅…… 아, 그러고 보니 아직 한 놈은 살아 있군.”

쌔액, 쌕.

“마, 마군…….”

아직 숨이 붙어 있는 채로, 얕은 숨결을 내뱉고 있는 일노를 힐끗 바라본 혈검마군이 나를 향해 물었다.

“이건 노파심에 묻는 건데, 자네 혹시 그놈 살려 둘 생각인가?”

“그건 왜 묻는 거지?”

“아까부터 계속 거슬려서. 이건 뭐, 산 것도 아니고 죽은 것도 아니고…… 뭐든 확실한 게 좋지 않겠나.”

“……!”

“죽일 거면 빨리 죽이고, 포로로 쓸 거면 옆에 있는 젊은 친구 시켜서 돌려보내게. 물론 아는 게 그리 많지 않아서 딱히 별다른 쓸모도 없겠지만.”

사마표를 가리키며 말한 혈검마군이 문득 입맛을 다셨다.

“아, 이제는 그럴 시간도 부족하려나?”

둥, 둥, 두웅.

갈수록 그 크기와 울림을 더해 가는 전고(戰鼓) 소리가 가까워지고 있었다.

혈검마군과 우리.

각각 등 뒤로 수많은 군세가 토해내는 기세가 사방을 떨어 울리고 있었다.

‘이제, 시작이다.’

나는 직감했다.

대설산 일대를 피로 물들인 혈전이, 피할 수 없는 대전투가 드디어 첫걸음을 떼었다는 것을.

그리고…….

‘바로 이 자리에서, 끝낼 수 있다.’

지금으로서는 혈검마군이 어느 정도의 고수인지 정확히 알 수 없지만, 나와 적천강만 있다면 충분하다.

천산삼노라는 핵심 전력이 소멸한 지금, 이 전투의 무게추는 아군을 향해 한껏 기울어져 있었다.

분명.

분명 그럴 터였다.

‘그런데 왜…….’

혈검마군은 왜 지켜만 보았던 것일까.

그토록 중요한 전력을, 세 명이나 되는 초절정 고수의 존재를 가축 취급했던 것일까.

‘이건.’

생각이 거기까지 미친 그 순간. 나는 문득 눈을 크게 떴다.

화아아악.

어느샌가 먹구름이 몰려들고 있었다. 대설산이 지니고 있던 것보다 더한, 얼음과도 같은 냉기가 바람을 얼리며 다가오고 있었다.

그리고 그 모든 것의 중심에, 거무스름한 안개처럼 들이닥치는 한 무리의 인마(人馬)가 있었다.

스아아아아.

거센 말발굽 소리조차 없이, 유령과 같은 움직임으로 쇄도하는 그 모습을 보며 나는 떠올렸다.

이곳에, 무림에 나타나서는 안 되는 이계의 존재들을.

“데스 나이트(Death Knight)……?”
```

## Final English reading copy

```markdown
# Chapter 1029

Tap. Patter-patter.

Hot and damp.

Blood that had shot high like a fountain was falling onto my head, soaking my scalp.

For someone already reduced to a headless corpse, it was a sensation they would never feel again.

> **System**
> Defeated Lv. 135 Gungongbo!
>
> Acquired a large amount of Fame.
>
> Acquired a large amount of EXP.

Splatter!

The body, losing its balance a moment later, crumpled onto the pool of blood.

The Second Elder’s head had been severed from his body before he’d had a chance to react. With a bewildered expression, it looked up at his sworn brothers.

Or, more precisely, the only sworn brother still in this world.

“One down. No—two.”

Jeok Cheongang’s timely words announced the Third Elder’s end. I turned to look and saw a silver blade sticking out of the back of the man sprawled like a rotten log.

Pssht.

Blood dripped in little spurts with a deflating hiss.

Sama Pyo was retrieving the dagger lodged between the Third Elder’s brows. When our eyes met, he shrugged.

“Did I do something I shouldn’t have?”

I answered.

“Yeah.”

“If he was yours to deal with, I’m sorry. I thought leaving him alive might cause trouble…”

“That’s not what I mean.”

A question crept into Sama Pyo’s gaze. I exhaled a breath as hot as a ball of fire and continued.

“You shouldn’t have killed him so easily.”

EXP didn’t matter. Neither did whose hand killed him.

He should have suffered more.

He shouldn’t have been allowed to leave this world so comfortably, in a single instant.

Like the Second Elder, whose collarbone had been torn away first, then one arm had been severed, and finally his Eight Extraordinary Meridians had been ripped to shreds before his head was cut off.

“Don’t step in again. Not one step.”

My voice sounded strange and desolate, as if it belonged to someone else.

I didn’t even know what I looked like right now.

But the grim, hardened expressions on Sama Pyo and Jeok Cheongang—and the First Elder, frozen as if face-to-face with a fiend—gave me some idea.

“M-monster…”

His body and voice trembled.

In the eyes of the old fiend who’d lost his two sworn brothers, the companions of his entire life, in the blink of an eye, I saw rage he couldn’t hide—and fear, even deeper and darker.

Splosh.

I took a slow step forward.

Maybe it was because the blood had soaked the ground. The sound of my footfall rang unusually loud, and the First Elder jumped and stumbled backward.

No—he dragged his rear backward, using both arms to brace himself.

With both knees already shattered, it was the only way he could get even a little farther from me.

“D-don’t come any closer! I said don’t!”

With a scream, the First Elder flung out his arms.

Boom!

I turned my head before I even heard the rush of air. The manifested palm force exploded through the space where my head had been a moment earlier.

Though he was already half-crippled, the powerful internal energy flowing deep within his body still burned like an inextinguishable flame.

Of course…

“Do it again.”

To my eyes, his movements were clumsy beyond words, hopelessly slow—and, because of that, full of openings.

“Aaaaaah!”

It was impossible to tell whether his cry was a scream or a battle shout.

Bang! Bang! Boom!

The First Elder, panicking out of his mind, unleashed palm force after palm force, making the compressed air burst.

The force of his frenzied attacks whipped my hair around and tore at my skin along with my collar.

And that was the First Elder’s final struggle.

Grab—crack!

I seized his wrist like lightning and twisted.

This wasn’t a grappling technique steeped in complex principles, or even a move powered by internal energy.

Just raw Strength and Agility.

That power and speed, far beyond the limits of a human being, made short work of frail flesh and bone.

“Ghk…!”

His face contorted with pain. A groan forced its way out.

But I knew.

If the old fiend in front of me were the sort to give up everything at a pain like this, the title of the Three Elders of Tianshan would have been forgotten long ago.

Whoosh! Crash!

Five fingers, curled like hooks, flashed down and struck the ground.

Just one step.

I read his movement and stepped back before he could act. His hand narrowly grazed my collar before plunging deep into the earth. I stomped on its back.

Crack!

The sensation of his bones shattering traveled up through my sole, the full weight of a thousand catties behind it.

His eyes, wide with unimaginable pain and terror, reflected my calm expression.

“Don’t look at me like that.”

Thud.

A precise blow to the jaw turned his head. Yellow teeth flew in every direction with the blood.

“When you look at me…”

Thud.

One more.

“Like that…”

Thud.

Again.

“I feel like killing you right now.”

Crack!

Sticky blood clung to my fist.

Gripping the hair of the First Elder, who no longer moved at all, I slowly straightened up.

“We’re only just getting started, aren’t we?”

I wasn’t talking to the First Elder.

I was speaking to the monster watching this whole scene from more than thirty yards away, his face alight with excitement—the one who’d cut a thousand people’s heads off with a single gesture.

Clap. Clap. Clap.

The Blood-Sword Demon Lord gazed at me with admiration, applauding slowly.

“Magnificent. No—beautiful.”

At his answer, it felt as though the blood in my body were turning cold.

Even now, with extreme rage ruling my mind, the man’s reaction was far beyond anything I could have expected.

“That’s how a Murim warrior should be. You have to crush your opponent, cruelly and completely. That’s what makes a real fight, don’t you think?”

The Blood-Sword Demon Lord was grinning from ear to ear.

Despite two of the Three Elders of Tianshan—important fighters and his own right hands—being dead, and the third crippled, he looked far happier than he had a moment ago.

“Crazy… bastard.”

“Me? Or you?”

“What?”

“Isn’t that right?”

The Blood-Sword Demon Lord blinked at me, then spun around with his arms spread wide.

“Look at me. My clothes are a bit drab, but compared to you, don’t I look positively mild-mannered?”

“……!”

“Ah, don’t misunderstand. I’m certainly not saying you look unpleasant. If anything, I find this rather familiar… It’s a good sight, in more ways than one.”

At the Blood-Sword Demon Lord’s satisfied smile, I suddenly felt short of breath.

He’d called it familiar. He’d called it a good sight.

The Blood-Sword Demon Lord, of all people. The old, vicious fiend.

Me, drenched in blood from head to toe.

Me, a moment ago, consumed not just by revenge but by the desire to inflict even greater pain.

“This… This is, I mean…”

“Enough.”

A voice I knew all too well cut me off, settled low in a way it rarely was.

“That’s enough.”

Jeok Cheongang strode forward. I suddenly wanted to ask him something.

Who was he speaking to?

Me? Or the Blood-Sword Demon Lord?

Or both of us?

But I didn’t ask. No—it was more accurate to say I couldn’t.

For a moment, I was afraid to ask whether I’d looked like a fiend mad with blood and revenge.

And yet, somehow, the one who helped me pull my stiffened body and mind back together was that very fiend.

“To interrupt us at a time like this, Senior—you’re too cruel. We were having a rather meaningful conversation.”

The Blood-Sword Demon Lord shook his head. Jeok Cheongang spat onto the ground.

“Fuck off. This old man never had a junior like you.”

“I know that, but I’ve admired you for a long time, so I can’t help myself. I’ll have to settle for an unrequited love.”

“Do I have to turn you into charcoal while you’re still alive to shut that mouth of yours?”

“Probably. To be honest, I was a little disappointed about that. I thought at least one of those three would end up like that.”

The Blood-Sword Demon Lord gave a showy sigh, then continued.

“You can’t imagine how excited I was when I heard what happened at Mount Jiuhua all those years ago. A descendant of the Fire Gate Clan I’d only ever heard about! When I heard those fools who dared lay a hand on you had all been reduced to ash, I was so delighted.”

“What did you say?”

“Isn’t that right? They burned alive—how much pain they must have felt. What could be a surer, more terrible revenge than that?”

“……!”

“Everyone else shuddered and called you a mad old man, but I didn’t. That was the day I started admiring you.”

At the Blood-Sword Demon Lord, his eyes shining like morning stars, Jeok Cheongang, I, and even Sama Pyo—all of us had been watching the situation calmly—seemed at a loss for words.

A fiend.

More than anyone I’d ever seen, the Blood-Sword Demon Lord was a lunatic worthy of the word.

Now I understood better than ever why the character for “blood” was in his title.

And to the Blood-Sword Demon Lord, the Three Elders of Tianshan were nothing more than livestock he’d kept nearby.

“Those idiots were the same. During the Great Faction War, they couldn’t run away fast enough whenever the battle turned against them. Then today, they stepped up without knowing their place, so they deserved to die… Ah, come to think of it, one of them’s still alive.”

Wheeze, wheeze.

“D-Demon Lord…”

The Blood-Sword Demon Lord glanced at the First Elder, who was still breathing faintly, then turned to me.

“I ask only out of concern, but are you thinking of letting him live?”

“Why do you ask?”

“He’s been bothering me for a while now. He’s neither alive nor dead… Wouldn’t it be best to make things definite?”

“……!”

“If you’re going to kill him, do it quickly. If you want him as a prisoner, have the young fellow beside you take him back. Though he doesn’t know much, so he won’t be of much use.”

The Blood-Sword Demon Lord gestured toward Sama Pyo, then smacked his lips.

“Ah, though I suppose there’s not much time for that now.”

Boom. Boom. Bwoom.

The war drums were drawing closer, growing louder and more resonant with each beat.

The Blood-Sword Demon Lord and us.

Behind each of us, the force of countless troops made the air tremble in every direction.

*Now it begins.*

I could feel it.

The blood-soaked battle for the Great Snow Mountain, the inescapable great war, had finally taken its first step.

And…

*I can end it right here.*

I couldn’t tell exactly how powerful the Blood-Sword Demon Lord was, but Jeok Cheongang and I should be enough.

Now that the Three Elders of Tianshan, a core part of their fighting strength, were gone, the balance of this battle had tipped heavily in our favor.

Surely.

Surely that was how it would go.

*Then why…*

Why had the Blood-Sword Demon Lord only watched?

Why had he treated such important fighters—three Supreme Peak masters—as if they were livestock?

*This is…*

The moment my thoughts reached that point, my eyes widened.

Whoosh!

Dark clouds had gathered at some point. A cold fiercer than the Great Snow Mountain’s own swept toward us, freezing the wind as it came.

And at the center of it all was a company of riders, rushing in like a dark, misty fog.

Sssaaaaa.

As I watched them surge forward with ghostlike movements, not a single thunder of hooves, I remembered.

The otherworldly beings who shouldn’t have appeared here, in the Murim.

“Death Knights…?”
```
