<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1042.txt",
      "sha256": "f6c437efb80f7b30e8593ab75215c8c96170f3929666e7f11b0aad44788769d4",
      "bytes": 13993
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1323274ef66af04205f05d8e472f6f077c05c9b56d1312bbf166451943496be1",
      "bytes": 1382
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91edff1ea0e7f2d1bdf20f77998a86f250b89f1bc3f043cd106289bea1e118b4",
      "bytes": 240895
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "bc7a3bd5d2192f5d572852604dc94bb2b59d5d89b5bd1615e1e240e166e90fb1",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "efa49bd01994211c2ab3723c4675db54af27df821eed92ce7859683f86d40eb5",
      "bytes": 549
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "c7bcd94d5d5ce9c0534e9640e5f98292618b0b2bed9c82d9dd572894f435f076",
      "bytes": 668
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "364cc56d6ed05cb6e626aca1fef889a85d6dd6756799663ac8a75d9d380f3240",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "eac9b9ca3539e11278eeeb5de1d13bf66605a156b62418c1732228d9d9d80ad8",
      "bytes": 1823
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "50eefa2f90802afcf541636d7e8cb5a0648c8d409d44d9d8104a321fc240ba0a",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ee9dbcd648b70c21fbc70b4353033e59e01581c697fe31051ccacee5e61de61f",
      "bytes": 279732
    }
  ],
  "estimated_tokens": 11199
}
-->

# Durable State Update — Chapter 1042

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
1 and safe_through 1042. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1042. Profile updates may replace only one
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
  "chapter": 1042,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1042,
    "continuity_sources": [1042],
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
    "The Grand Mage’s powerful barrier separates her from Jin; he believes a single failed strike will let her escape.",
    "The Grand Mage has just released an enormous surge of energy."
  ],
  "continuity_sources": [
    1040,
    1041
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?",
    "How were the former Demonic Cult fiends made into Black Ghosts?",
    "What will the Grand Mage’s released energy do?"
  ],
  "safe_through": 1041,
  "temporary_decisions": [
    "Render 대마도사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무인     | **martial artist**                               | Default term                                          |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 일격     | **One Strike**                         |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 본문      | **our sect / this sect**                                        |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 대종남파 | **Great Zhongnan Sect** | Expanded and formal reference to the Zhongnan Sect. |
| 천하삼십육검 | **Heavenly River Thirty-Six Swords** | Zhongnan Sect sword technique used by Song Il. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 노호검객 | 적천강 | senior_martial_artist_to_legendary_elder | Senior Jeok | deferential and cautious | Addresses Jeok as 노 선배 while explaining his actions. |
| 풍운검군 | 적천강 | Zhongnan Sect Leader to legendary martial master | Senior Jeok | respectful | Refers to Jeok as 적 대협. |
| 풍운검군 | 노호검객 | Zhongnan Sect Leader to Senior Brother | Senior Brother | respectful and strained | Addresses him as 사형 while protesting the decision. |
| 풍운검군 | 태을무정검 | Zhongnan Sect Leader to Senior Brother | Senior Brother | respectful and strained | Addresses him as 사형 while protesting the decision. |
| 풍운검군 | 진태경 | martial artist to fellow martial artist | Daoist Friend Jin | respectful and familiar | Thinks of Jin as 진 도우 when recognizing him as a possible turning point in the battle. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1040
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1041
- **Aliases:** None
- **Role:** The Grand Mage leads the white-robed mages and is a formidable mage who has reached the edge of truth.
- **Personality:** She remains composed while taunting Jin and appears pleased and excited to meet him.
- **Voice:** Calm and politely phrased, with teasing remarks and a hint of excitement.
- **Relationships:** She commands the white-robed mages and is an adversary of Jin Taekyung.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 1039
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1039
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1040
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1040
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1042화



고오옹.

대마도사를 중심으로 솟아오른 그 거대한 기운을 느낀 순간, 새하얗게 물든 진태경의 뇌리에 총알처럼 틀어박히는 두 개의 단어가 있었다.

첫 번째는 광범위 마법.

그리고…….

‘일섬(一殲).’

진태경은 본능적으로 직감하고 있었다.

눈앞의 여인이 벌이려는 이 미친 짓을 막기 위해서는, 자신 역시 미친 선택을 해야 한다는 것을.

그 스스로도 두 번 다시 사용할 수 없을 거라 여겼던, 이번에는 회생(回生)의 가능성조차 희박한 필사의 일격이 아니라면 이 광범위 마법의 발동을 막을 수 없으리라는 것을.

그와 동시에 이미 결정을 내린 자신의 마음을 깨닫고, 내심 씁쓸하게 웃었다.

‘빌어먹을.’

아직 죽기 싫었다.

어떻게든, 추하게 발버둥 쳐서라도 써서라도 살고 싶었다.

그러나 방법이 없었다.

아니, 오직 단 한 가지 방법뿐이었다.

지금 당장 대마도사를 둘러싼 강력한 방어막을 부수고, 그 일격으로 상대의 목숨을 앗아 가기 위해서는 진태경 자신의 생명 또한 불태워야 했다.

이 일격이 성공할 거라는 확신?

없다.

다만 가능성이 있을 뿐이다.

생존과 죽음?

후자일 가능성이 농후하다.

하지만 설령 그렇다 할지라도, 그것으로 충분했다.

오직 이것만이 아직 전장에서 분투하고 있는 아군 수만 명과, 그 안에 포함된 소중한 사람들을 지키기 위한 유일한 선택지였으니까.

‘그래.’

그거면 된 거다.

숭고한 희생, 개죽음.

둘 중 어떤 결말을 맞이하게 될지는 모르나, 혼란스러운 시대는 지금 이 순간 진태경에게 영웅이 될 것을 강요하고 있었고 그는 준비되어 있었다.

어쩌면, 아주 오래전부터.

스아아아.

일순간 바람이 멎는다. 대기가 파르르 떨렸다.

마치 모든 것이 멈춘 듯한 시간 속, 수백 개의 혈도가 깨어나고 전신의 근육이 한 가닥, 한 가닥 선명하게 느껴졌다.

그리고…….

새하얀 창날을 타고 흘러 들어가는 기(氣)가 있었다.

깊은 바닷속처럼 어둡고, 벼락처럼 번뜩이며, 불꽃처럼 타오르는.

마침내 하나로 합쳐져 그 어느 때보다 비대하게 부풀어 오른 기운이, 그렇기에 주인의 생명마저 집어삼켜 버릴 강대한 힘이 활시위처럼 젖힌 창날을 따라 휘몰아쳤다.

지금 이 순간, 촘촘한 면사 뒤에 가려진 한 쌍의 눈동자를 물들일 만큼 휘황한 빛을 토해 내며.

‘이건.’

방어막으로도 완전히 가릴 수 없는 그 파괴적인 섬광 앞에서, 대마도사는 불현듯 엄습해 오는 두려움을 느꼈다.

믿을 수 없는 선택을 한, 눈앞의 청년에 대한 경외심도 함께.

‘이대로라면 죽는다. 틀림없이.’

대마도사는 확신했다.

저 무시무시한 일격이 완성되어 쏘아지면, 자신은 방어막과 함께 흔적도 없이 사라질 것이라고.

그와 더불어 진태경의 생명 역시 잿더미처럼 흩어질 것이라고.

하지만 그것은 대마도사도, 그녀가 섬기는 주인도 바라는 결과가 아니었다.

‘운이 좋네. 당신도, 나도.’

감당할 수 없을 정도의 무게를 담은 전낭은 찢어질 수밖에 없다. 그러나 그 무게가 온전히 실리기도 전에 매듭을 묶는다면, 전낭은 찢어지지 않는다.

그런 의미에서 보자면, 그야말로 간발의 차이였다.

대마도사의 마법은 이미 지금보다 한발 앞서 준비되어 있었고, 진태경의 일격은 그보다 한발 늦었으니.

그리고 시간상으로는 찰나에 불과한 그 미세한 차이가, 두 사람 모두의 운명을 바꾸었다.

‘쏟아져라, 지옥의 불길이여.’

화아악!

일순간 대마도사를 중심으로 폭발하는 강대한 기운.

그 힘의 확산은 진태경이 생각했던 것보다도 훨씬 빠르게 시작되었고, 그에게 남아 있는 선택지는 하나뿐이었다.

슈확!

공간을 찢어 발기며 나아가는 창날.

동시에 그 어느 때보다 거대한, 그렇기에 아직 절반도 채 응집되지 못한 일섬이 마침내 두 사람 사이에 놓인 방어막과 맞닿은 그 순간.

고오오옹.

귓가가 먹먹해지는 굉음과 동시에, 새하얀 섬광이 언덕을 물들였다.



* * *



전신 곳곳에서 전해지는 아릿한 통증 속, 노도사는 가빠진 호흡을 가다듬었다.

후우.

단내가 풀풀 풍기는 숨결이 느릿하게 흩어진다.

이마의 상흔에서 흘러내린 핏방울로 붉게 물들어 버린 시야 너머, 철탑처럼 우뚝 선 두 명의 사내가 노도사의 눈동자에 비쳤다.

아니, 비쳤다고 느낀 순간 사라졌다.

쉭.

소름이 끼칠 만큼 미세한 파공성이 귓가를 파고든다.

머릿속에서 울린 경종이 위험을 경고하고, 그와 동시에 판단을 끝마친 두뇌는 몸뚱어리에 명령을 내렸다.

피하라고.

지금 당장 적을 피해 움직여야 한다고.

하지만 이미 적지 않은 부상을 입은 노도사의 육신은, 결코 평소와 같은 움직임을 보일 수 없었다.

서걱!

극심한 격통.

미처 완전히 피하지 못한 두 개의 날붙이가 옆구리와 어깻죽지를 베어 가르고, 강철에 담겨 있던 거대한 기운이 몸속 깊은 곳까지 헤집었다.

‘흡……!’

순간 아득해지는 시야.

그러나 풍운검군은 이내 비틀거리는 신형을 다잡으며 자신의 애검을 흩뿌렸다. 이제는 절반밖에 남아 있지 않은 검신 위로 휘황한 검강이 솟아올랐다.

쾅! 쾅! 콰앙!

번개처럼 이루어진 세 번의 격돌. 그리고 뿌옇게 피어오른 먼지구름을 뚫고 포탄처럼 튕겨 나간 한 사람의 신형.

“장문인!”

암천의 교도들과 뒤섞여 싸우던 종남파의 제자들이 비명을 내지른 그 순간이었다.

어디선가 나타난 두 개의 인영이 세차게 튕겨져 나가던 풍운검군의 신형을 받아 낸 것은.

드드득!

일장을 밀려나고서야 겨우 멈추는 발걸음.

쿨럭, 죽은 핏물을 토해 낸 풍운검군이 흐릿하게 보이는 조력자들을 향해 입술을 달싹였다.

“사형들…….”

“제기랄, 아무 말도 말거라.”

신경질적인 목소리로 대꾸한 대사형 노호검객에 이어, 둘째 사형인 태을무정검이 무거운 얼굴로 입을 열었다.

“이만하면 됐네. 장문 사제.”

이만하면 됐다.

비록 짧은 한마디였지만, 풍운검군은 그 말에 담긴 의미를 즉각 알아차릴 수 있었다.

하지만 그랬기에, 지금 자신이 들은 말을 믿을 수 없었다.

“되었다니, 그게 도대체 무슨…….”

“시간이 없네. 이 상황이 더 지체될수록 본문의 피해만 커질 걸세.”

“사형!”

경악이 담긴 외침.

그러나 그런 사제의 모습에 태을무정검은 입술을 굳게 닫았고, 노호검객은 천천히 걸음을 옮겨 다가오는 두 흑귀(黑鬼)를 바라보며 이를 악물었다.

“둘째의 말이 맞다. 퇴로(退路)는 이미 우리가 확보했으니 네놈은 명령을 내리거라! 어서!”

되려 윽박지르는 듯한 태도.

이 생각지도 못한 상황 속에서, 풍운검군은 자신의 두 사형을 멍하니 바라보았다.

“진심……이십니까?”

그러나 그 물음에 노호검객과 태을무정검은 대답하지 않았다.

차마 크게 뜨여진 사제의 눈을 똑바로 직시하지 못한 채, 두려움이 담긴 눈빛으로 정면의 흑귀들을 응시할 뿐이었다.

그들도 알고 있었으니까.

자신들의 주장이, 얼마나 정도(正道)에서 벗어나 있는 것인지.

그리고 사형들의 그러한 모습에, 풍운검군은 마침내 이 믿기 힘든 현실을 인지했다.

“……진심이었군요. 두 분 모두.”

이 상황을 무어라 말해야 할까.

참으로 이상한 기분이었다.

일평생 함께하며 한 스승 아래에서 동문수학한 사형들인데, 마치 난생처음 보는 듯한 낯선 감각이 그들에게서 느껴졌다.

‘퇴각. 퇴각이라.’

텅 비어 버린 마음속으로 그 두 글자를 뇌까리던 풍운검군은, 문득 지난날을 떠올렸다.

종남파에 처음 입문했던 그 날부터, 지금까지의 기억들을.

이제는 먼지로 뒤덮인 오랜 과거 속에서도 세 사형제는 언제나 함께였다.

그래서 좋았다.

도사보다는 무림인에 가깝고, 간혹 과격한 언동으로 문제를 일으키긴 했어도 사형들이었으니까.

그가 종남파의 장문인으로 임명된 그 날, 자신들이 선택받지 못한 것에 대해 분노하긴 했어도 결국은 인정하고 따라 주었으니까.

정마대전을 치르던 와중 남만야수궁과의 문제가 생겼을 때도.

지금으로부터 불과 일 년 전, 본인들의 과오로 적천강과 진태경에게 차례대로 수모를 당했을 때도.

풍운검군은 그들을 감싸 주었다. 사형들을 비난하는 이들을 막아 세우고 변호했다.

두 사형이 모두의 예상을 벗어나 놀라운 속도로 내상을 회복했을 때도, 가장 기뻐했던 것 역시 그였다.

하지만…….

“어찌하여 이리되셨소.”

풍운검군은 나직한 탄식을 내뱉었다.

부릅뜬 눈으로 자신을 바라보는 두 사형의 부축을 뿌리치며, 이제는 검자루밖에 남지 않은 애검을 으스러져라 움켜쥐었다.

“기억하시오? 스승님께서 이 검을 내려 주시며 그런 말씀을 하셨지. 도사가 되려 애쓸 필요는 없다. 다만 바르게 살거라. 인간으로서의 도리를 지킨다면, 그것이 도사다.”

“……!”

“……!”

“그토록 살고 싶다면, 사형들은 가시오. 나는 남을 테니. 그것이 스승님께 물려받은 대종남파의 이름을 더럽히지 않는 길이니.”

풍운검군도, 노호검객과 태을무정검도.

그리고 이 전장의 모두가 안다.

지금 시점에서 전황의 한 축을 담당하고 있는 종남파가 물러나면, 이 전투는 필패(必敗)라는 것을.

그렇기에 풍운검군은 결코 물러날 수 없었다.

적어도 자신만큼은.

으득.

혀를 깨물자 아릿한 통증과 함께 선명해지는 시야.

풍운검군은 검은 연기를 뭉클뭉클 쏟아내며 다가오는 두 흑귀를 향해 걸음을 내디뎠다.

철벅.

발걸음도, 마음도 무겁다.

어쩌면, 그 자신 역시도 이 자리에서 도망치고 싶었는지도 모른다.

그러나 풍운검군은 멈추지 않았다.

도망칠 수 없었다.

그것이야말로 스승이 가르쳐 주었던, 인간으로서의 도리였기에.

‘돌이켜 보면, 나 또한 그리 훌륭한 도사는 못 되었지.’

늘 앞서가는 화산파를 질시했고, 종남파의 이익만을 추구했다.

권력과 결탁하여 오가는 재물로 세력을 불리고, 품성보다는 재능으로 제자들을 받아들였다.

그것이 종남파를 위한 길이라고 생각했기에.

하지만 그런 와중에도, 정의(情義)라는 두 글자를 잊은 적은 없었다.

그리고 이곳에는 지금 이 순간에도 목숨을 걸고 싸우는 수많은 아군이 있다.

가장 위험한 곳에서, 누구보다 큰 위기와 맞서는 청년이 있다.

부끄러움.

그것이 그가 물러설 수 없는 이유였다.

“오너라. 아니, 이번에는 내가 가도록 하마.”

풍운검군은 피가래가 들끓는 목소리로 내뱉었다.

동시에 그 어느 때보다 맑은 눈동자로 자신을 향해 다가오는 두 괴물을 바라보며, 더는 검이라 부를 수 없는 형태가 된 애검에 남아 있던 모든 기운을 쏟아부었다.

츠츠츠츠!

휘황한 검강(劒罡)이 타올랐다.

종남파의 장문인으로서 보일 수 있는, 한 사람의 무인으로서 피워올릴 수 있는 마지막 불꽃이.

“대종남파를 위하여.”

작게 중얼거린 그 순간, 풍운검군은 온 힘을 다해 신형을 내뻗었다.

“안 돼!”

“장문 사제!”

그리고 등 뒤에서 울려 퍼지는 사형들의 외침을 뒤로한 채, 한 마리의 부나방처럼 날아드는 풍운검군을 기다리고 있던 두 줄기의 섬광이 있었다.

쉭! 쐐애애액!

바람을 부수는 거대한 대부(大斧)와 공간을 베어 가르는 새하얀 검신.

그 파괴적인 힘의 물결을 향해 달려들던 풍운검군은 담담히 직감했다.

끝이라고.

어느 때보다 혼신의 힘을 다한 이 일격으로도, 저들의 숨통을 끊어 놓지 못할 것이라고.

하지만 그 순간 스스로 죽음이라는 운명을 받아들인 풍운검군조차, 아니 전장의 그 누구도 예상치 못했던 이변(異變)이 일어났다.

후웅, 꽈아아아앙!

저 멀리서 들이닥친 아득한 섬광이, 지금껏 거대한 충격파가 일대를 후려쳤다.

폭발. 재앙.

도무지 무엇이라 불러야 할지 몰랐으나, 한 가지만큼은 명확했다.

드드드득!

이 예상치 못한 충격파에 지면에 서 있던 두 흑귀의 자세가 흐트러졌고, 이미 허공을 밟으며 쏘아지던 풍운검군의 일격은 섬광을 비집고 나아갔다는 것.

서걱!

휘황한 빛으로 이루어진 천하삼십육검(天下三十六劍)이 공간을 가른 그 순간.

스아아아아.

바람처럼 두 흑귀를 스쳐 지나간 풍운검군은, 아니 전장의 모두는 본능에 따라 고개를 들었다.

그리고, 마침내 보았다.

화륵.

믿을 수 없을 만큼 거대한, 이 세상의 것이 아닌 것 같은 화염의 구(球)를.

지옥에서 끄집어 올린 겁화, 헬 파이어(Hell Fire)를.
```

## Final English reading copy

```markdown
# Chapter 1042

Gooooom.

The instant he felt the enormous energy surging up around the Grand Mage, two words shot into Jin Taekyung’s mind like bullets, bleaching it white.

The first was wide-area Magic.

And then…

*One Annihilation.*

Jin Taekyung knew it by instinct.

To stop the insane thing the woman before him was about to do, he would have to make an insane choice of his own.

Unless he unleashed a desperate strike he’d thought he could never use again—a strike with barely any chance of bringing him back to life this time—he wouldn’t be able to stop the wide-area Magic from activating.

At the same time, he realized he’d already made his decision, and laughed bitterly to himself.

*Damn it.*

He still didn’t want to die.

He wanted to live, somehow—even if he had to struggle pathetically, whatever it took.

But there was no way.

No—there was only one way.

To break through the powerful barrier surrounding the Grand Mage right now and take her life with that strike, Jin Taekyung would have to burn up his own life, too.

Was he certain the strike would work?

No.

There was only a chance.

Survival or death?

The latter was far more likely.

But even if that was the case, it was enough.

This was the only option left to protect the tens of thousands of allies still fighting on the battlefield—and the precious people among them.

*All right.*

That was enough.

A noble sacrifice, or a pointless death.

He didn’t know which ending awaited him, but these chaotic times were forcing Jin Taekyung to become a hero in this very moment, and he was ready.

Perhaps he had been for a very long time.

Fwoosh.

The wind stopped all at once. The air trembled.

Time seemed to stand still. Hundreds of acupoints awakened, and he could feel every strand of muscle throughout his body, one by one.

And then…

Qi flowed along the white spearhead.

Dark as the deep sea, flashing like lightning, burning like a flame.

At last, the energy merged into one and swelled larger than ever before. A mighty force capable of devouring its owner’s life, it whipped along the spearhead, drawn back like a bowstring.

In that moment, it blazed with such dazzling light that it seemed to color the Grand Mage’s eyes, hidden behind her finely woven veil.

*This is…*

Before that destructive radiance, which even the barrier couldn’t fully conceal, the Grand Mage felt fear suddenly seize her.

Along with awe for the young man before her, who had made such an unbelievable choice.

*At this rate, I’ll die. Without a doubt.*

The Grand Mage was certain.

Once that terrifying strike was complete and launched, she would vanish without a trace along with her barrier.

And Jin Taekyung’s life would scatter like ash, too.

But neither the Grand Mage nor the master she served wanted that outcome.

*We’re both lucky, you and I.*

A money pouch burdened with more weight than it can bear is bound to tear. But if you tie it shut before all that weight is put inside, it won’t.

In that sense, they had missed disaster by a hair’s breadth.

The Grand Mage’s Magic had been prepared a step ahead of this moment. Jin Taekyung’s strike was a step behind.

And that tiny difference in timing, no more than an instant, changed the fate of them both.

*Pour forth, flames of hell.*

Fwoosh!

An immense energy exploded around the Grand Mage.

Its power began spreading far faster than Jin Taekyung had expected. He had only one choice left.

Shwoosh!

The spearhead tore through space.

At the same time, a One Annihilation larger than ever before, and therefore not even half-formed,finally met the barrier between them.

Gooooom.

A deafening roar made his ears ring, and white light washed over the hill.

* * *

Amid the faint pain coming from all over his body, the old Daoist steadied his ragged breathing.

Hoo.

His sweetish-smelling breath slowly dispersed.

Beyond the red haze of his vision, stained by blood running down from the scar on his forehead, two men stood tall as iron towers.

No—as soon as he thought he saw them, they vanished.

Whish.

A faint whistle, chillingly subtle, pierced his ears.

An alarm rang in his mind, warning him of danger. His brain finished its judgment and ordered his body to move.

Dodge.

Move now to avoid the enemy.

But his body, already badly wounded, couldn’t move as it normally would.

Shhk!

A wave of excruciating pain.

The two blades he hadn’t managed to avoid completely slashed his side and shoulder, and the tremendous energy held within the steel tore deep through his body.

*Hng…!*

His vision blurred.

But the Wind-and-Cloud Sword Lord soon steadied his wavering form and unleashed his treasured sword. Brilliant Sword Force flared along the blade, now only half its former length.

Bang! Bang! Baaang!

Three clashes, as swift as lightning. Then one figure shot through the cloud of dust like a cannonball.

“Sect Leader!”

The Zhongnan Sect disciples fighting amid the Dark Heaven cultists screamed.

At that very moment, two figures appeared from nowhere and caught the Wind-and-Cloud Sword Lord as he flew backward.

Grind.

Only after sliding back several feet did they finally stop.

Coughing up dark blood, the Wind-and-Cloud Sword Lord moved his lips toward his helpers, whose faces were blurred in his sight.

“Senior Brothers…”

“Damn it, don’t say a word.”

The First Senior Brother, the Roaring Fury Swordsman, snapped back irritably. Then the Second Senior Brother, the Taeeul Merciless Sword, spoke, his expression grave.

“This is enough. Junior Brother, Sect Leader.”

This is enough.

It was only a short sentence, but the Wind-and-Cloud Sword Lord immediately understood what it meant.

And that was why he couldn’t believe what he’d just heard.

“Enough? What in the world are you…”

“We’re out of time. The longer this goes on, the greater our sect’s losses will be.”

“Senior Brother!”

His voice rang with shock.

But the Taeeul Merciless Sword pressed his lips together, while the Roaring Fury Swordsman slowly stepped toward the two approaching Black Ghosts, gritting his teeth.

“The Second Brother is right. We’ve already secured a way out. Give the order, damn it! Now!”

He sounded more like he was berating him than urging him.

In the midst of this unexpected turn, the Wind-and-Cloud Sword Lord stared blankly at his two Senior Brothers.

“Are you… serious?”

But neither the Roaring Fury Swordsman nor the Taeeul Merciless Sword answered.

Unable to meet the wide, disbelieving eyes of their Junior Brother, they only watched the Black Ghosts before them, fear in their eyes.

They knew.

They knew how far their position strayed from the right path.

And seeing them like that, the Wind-and-Cloud Sword Lord finally accepted the unbelievable truth.

“…You were serious. Both of you.”

What was he supposed to call this feeling?

It was strange.

They had spent their entire lives together, studying under the same Master. Yet something about them felt unfamiliar, as if he were seeing them for the first time.

*Retreat. Retreat.*

The two words echoed in his hollow heart, and suddenly he remembered the past.

All the memories from the day he first joined the Zhongnan Sect until now.

Even in the distant past, long buried in dust, the three Senior and Junior Brothers had always been together.

That was why he’d been happy.

They were closer to martial artists than Daoists, and sometimes caused trouble with their aggressive words and actions, but they were still his Senior Brothers.

On the day he was appointed Sect Leader of the Zhongnan Sect, they’d been angry that they weren’t chosen—but in the end, they’d accepted it and followed him.

When trouble arose with the Nanman Beast Palace during the Great Faction War.

And just a year ago, when they’d been humiliated one after another by Jeok Cheongang and Jin Taekyung because of their own mistakes.

The Wind-and-Cloud Sword Lord had stood up for them. He’d stood up to those who criticized his Senior Brothers and defended them.

When they both recovered from their Internal Injuries at an astonishing pace, contrary to everyone’s expectations, he’d been the happiest of all.

But…

“Why have you become like this?”

The Wind-and-Cloud Sword Lord let out a quiet sigh.

He shrugged off the support of his two Senior Brothers, who stared at him with wide eyes, and gripped the hilt—all that remained of his beloved sword—so tightly it seemed ready to break.

“Do you remember? When our Master gave me this sword, he said: ‘You need not strive to become a Daoist. Just live rightly. If you uphold your duty as a human being, that is what makes you a Daoist.’”

“……”

“……”

“If you want so badly to live, then go, Senior Brothers. I’ll stay. That is the only way not to disgrace the name of the Great Zhongnan Sect we inherited from our Master.”

The Wind-and-Cloud Sword Lord, the Roaring Fury Swordsman, and the Taeeul Merciless Sword all knew.

Everyone on the battlefield knew.

If the Zhongnan Sect, one of the forces holding the battlefront together at this point, withdrew, this battle would be a certain defeat.

That was why the Wind-and-Cloud Sword Lord could never retreat.

At least, he couldn’t.

Grnk.

He bit his tongue. The sharp pain cleared his vision.

The Wind-and-Cloud Sword Lord stepped toward the two Black Ghosts, who approached in billowing clouds of black smoke.

Squish.

His steps were heavy. So was his heart.

Perhaps he, too, wanted to flee this place.

But the Wind-and-Cloud Sword Lord didn’t stop.

He couldn’t run away.

That was the duty his Master had taught him to uphold as a human being.

*Come to think of it, I wasn’t much of a Daoist either.*

He’d always envied the Huashan Sect for forging ahead, and pursued only the Zhongnan Sect’s interests.

He’d grown the sect’s influence through wealth exchanged in collusion with those in power, and accepted Disciples for their talent rather than their character.

He’d believed it was the right way to serve the Zhongnan Sect.

But even so, he’d never forgotten the bonds of affection and loyalty.

And even now, countless allies were fighting for their lives here.

In the most dangerous place, a young man was facing a crisis greater than anyone else’s.

Shame.

That was why he couldn’t retreat.

“Come. No—this time, I’ll come to you.”

The Wind-and-Cloud Sword Lord’s voice was thick with blood.

His eyes clearer than ever, he watched the two monsters approaching him and poured every last bit of energy into the beloved sword, now no longer worthy of the name.

Tsssss!

Brilliant Sword Force blazed.

The final flame he could kindle as Sect Leader of the Zhongnan Sect, as a martial artist.

“For the Great Zhongnan Sect.”

He murmured the words, then hurled himself forward with all his might.

“Don’t!”

“Junior Brother, Sect Leader!”

Leaving the cries of his Senior Brothers behind, the Wind-and-Cloud Sword Lord flew at them like a moth to a flame. Two streaks of light waited for him.

Whish! Sshhh!

A massive battle-ax that shattered the wind, and a white sword blade that sliced through space.

Charging into the wave of their destructive power, the Wind-and-Cloud Sword Lord calmly knew:

It was over.

Even this strike, made with every ounce of strength he had, wouldn’t stop them breathing.

But then, an unexpected turn—one that neither the Wind-and-Cloud Sword Lord, who had accepted his own death, nor anyone else on the battlefield could have predicted—took place.

Whoom—KWA-BOOOOM!

A distant, blinding flash struck like a massive shock wave, slamming into the area.

An explosion. A calamity.

He didn’t know what to call it, but one thing was clear.

Grind!

The unexpected shock wave threw the two Black Ghosts off balance where they stood, while the Wind-and-Cloud Sword Lord’s strike, already hurtling through the air, slipped between their two streaks of light.

Shhk!

The Heavenly River Thirty-Six Swords, made of dazzling light, cleaved through space.

Fwoosh.

The Wind-and-Cloud Sword Lord swept past the two Black Ghosts like the wind. And he—and everyone else on the battlefield—looked up on instinct.

Then, at last, they saw it.

Flicker.

A sphere of flame so enormous it was hard to believe it belonged to this world.

Hellfire, dragged up from the depths of hell—Hell Fire.
```
