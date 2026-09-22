<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0642.txt",
      "sha256": "5ba0bbf8d9335463c5f30a83df2ba7cc75544a147a28138ddb3d20e7448e1df8",
      "bytes": 13220
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3be89c394946b4f8da14b949a6f72720726bdc0a4a769a6b9b2f9b5c8a367225",
      "bytes": 1454
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2e54c7fa9b2504231369591cadd144fe1f3d21672db80e5ee729597516271371",
      "bytes": 197596
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "06c713966f5641a0fa574073b5cebf477f0b4cf2df90f4f059a85825ee912725",
      "bytes": 808
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "356d8bc7598395bfe833a829b7dc5c0b1d9aca4a09363dc001e5f76aba0e9840",
      "bytes": 560
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "ed53a7b0347c2108da194bf5429b74bea69e2c4f69e2136161557d6db70e8eb3",
      "bytes": 623
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "65e05987d02b85103645a85dfe9c7b0638dbf466e40e00dfa53329f02df6ad88",
      "bytes": 1347
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ef467ee1105fe9ed5aedd1eb9a1eb20067c7d29924f7e4dcbbe0c8ad0402c155",
      "bytes": 1936
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5087e402ad2882b86e60486ba78146f084eca6e1533c4c1565b8c2c318c637e5",
      "bytes": 622
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "19710a04c51b06c69dc5cdf625c2d27f2ba89ef305a8d7e88d5cfe64666942f4",
      "bytes": 871
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "b0e24846b10c2571f0ae399a01e6974241d4108f4488288f73d852325401c79c",
      "bytes": 542
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2ee77e9a1d5d7d04bc6461137b6bdb37bcf4edf48b220c849a97822225533a4e",
      "bytes": 202599
    }
  ],
  "estimated_tokens": 11523
}
-->

# Durable State Update — Chapter 642

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 642. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 642. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 642,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 642,
    "continuity_sources": [642],
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
    "The Poisonblood Grounds swamp is a Thousand-Year Spider slaughterhouse and food storage facility containing hundreds of web-wrapped victims.",
    "Approximately two hundred elite warriors from Ailao Mountain remain alive inside the spiderwebs and are to be transported to the Nanman Beast Palace.",
    "The Thousand-Year Spider webs appear to shield the victims from the Poison Mist, so the survivors are left wrapped until evacuation.",
    "The missing ferocious beasts have not been found in the Poisonblood Grounds.",
    "A faint presence is approaching or hiding more than ten zhang from Jin Taekyung and the Beast Miao King.",
    "Dark Heaven’s involvement in the Thousand-Year Spider attack remains suspected but unconfirmed."
  ],
  "continuity_sources": [
    641
  ],
  "open_questions": [
    "What is the faint presence sensed more than ten zhang away?",
    "Where did the missing ferocious beasts go?",
    "Did Dark Heaven influence the Thousand-Year Spider attack, and why did it occur on the final day of the tribal competition?",
    "What does Ailao Mountain’s Wraith intend to do?",
    "What are the pure-white eggs in the swamp, and what will emerge from them?"
  ],
  "safe_through": 641,
  "temporary_decisions": [
    "Use Sword Demon for 검마.",
    "Use two-headed horn snake for 쌍두각사.",
    "Use black frog for 흑와.",
    "Use golden bee for 금봉."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무림맹    | **Murim Alliance**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 중원     | **Central Plains**                               |                                                       |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 장일 | **Jang Il** | Twenty-five-year-old two-knot Beggars' Sect Disciple killed near Emei. |
| 피독주 | **poison-warding pearl** | Poison-neutralizing artifact carried by the black-clad attackers. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 요족 | **Yao people** | One of Nanman's four great tribes, led by Yohi. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 독무 | **Poison Mist** | Deep green mist covering the Poisonblood Grounds swamp. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 천년지주 | **Thousand-Year Spider** | Monster appearing at the end of the chapter. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 636
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he lost a beloved son in the Great Faction War, bears a burn scar from Jeok Cheongang after calling him a crazy old man, opposes the Nanman Beast Palace joining the Murim Alliance, and helps Yohi keep Heugung under control.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 641
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace and is responsible for the forces stationed at Ailao Mountain.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 632
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung is foolish, easily flattered, and politically dependent on stronger personalities despite leading a powerful tribe.
- **Voice:** Heugung speaks with warm enthusiasm and exaggerated devotion toward Yohi.
- **Relationships:** Yohi and Baeksang keep Heugung under their control, while Heugung responds to Yohi's manipulation with apparent infatuation.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 631
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 637
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 637
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 636
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 632
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, and manipulates Heugung alongside Baeksang.

## Korean source

```text
＃642화



바스락.

미세한 소음과 함께 저 멀리에서부터 빠르게 가까워지는 기척. 그 사실을 알아차린 나는 빛살 같은 속도로 기척이 느껴지는 방향을 향해 백염을 겨누었다.

즉각 공력을 끌어올린 야수묘왕의 머릿속에도 나와 같은 생각이 스치고 있을 것이다.

‘애뇌산의 망령.’

하지만 다음 순간, 그 예상은 보기 좋게 빗나갔다. 검게 물든 풀숲 너머로 언뜻 보이는 새하얀 형체를 확인한 나는 한숨과 함께 창날을 늘어트렸다.

“무야호?”

- 크앙!

사사사삭!

짧지만 강한 울음소리와 함께 바람처럼 달려온 백호가 반갑게 나를…… 그대로 스쳐 지나가더니 야수묘왕의 발치에서 발라당 배를 뒤집어 깠다.

- 헥. 헥. 헥.

“그래, 그래. 용케 찾아왔구나. 영특한 녀석 같으니.”

저 정도면 백호가 아니라 실버 리트리버라고 불러야 하지 않나 싶다. 물론 덩치는 리트리버 열 마리를 합쳐 놓은 것 같지만.

‘그나저나 이 녀석이 돌아왔다는 건…….’

내 머릿속에 떠오른 생각을 읽은 듯, 한껏 재롱을 피우는 백호의 배를 쓰다듬어 주던 야수묘왕이 물었다.

“다른 이들은 어디 있느냐?”

- 그르릉.

기분 좋은 울음소리를 흘리며 일어난 백호가 돌연 크게 울부짖었다. 맹수의 포효가 짙은 어둠과 독무를 뚫고 울려 퍼지자, 얼마 지나지 않아 저 멀리에서 횃불이 일렁였다.

그 개수가 어림잡아 수십에서 일백.

그리고 그 선두에는 낯익은 얼굴들이 있었다.

“궁주.”

“아버님! 무사하십니까!”

유난히도 굳은 얼굴을 한 백상과 야율목을 위시한 남만야수궁의 전사들. 뒤이어 나타난 화룡각 대원들이 나를 향해 달려온다.

“조장니이임!”

“무진아. 이건 혹시나 해서 말하는 건데, 내 품에 안기거나 그러면 곱게는 못 죽는다.”

“……옙.”

비련의 여주인공에 빙의된 채 달려드는 혁무진을 단박에 차단한 나는, 막 입을 열려는 다른 대원들을 향해 어깨를 으쓱해 보였다.

“처음부터 이야기하자면 긴데…… 여기서 들을래? 아니면 밖에서 들을래?”

대답은 들으나 마나였다.

감성 팝송이 흘러나오는 분위기 좋은 카페라면 모를까. 독무가 흘러나오는 스산한 분위기의 독혈지에서 긴 이야기를 듣고 싶은 사람은 아무도 없을 테니까.

그리고 시스템은 내가 잠시 잊고 있던 퀘스트에 대해 알려 주는 것을 잊지 않았다.

띠링.



- 퀘스트, [님아, 그 늪을 건너지 마오]를 성공적으로 완수했습니다!

- 퀘스트 보상이 주어집니다!

- 상당한 경험치와 명성을 획득했습니다!

- [최상급 피독주x5]를 획득했습니다!

- 매우 희귀한 업적, [어케 돌아왔누]를 달성하셨습니다!

- 희귀한 칭호, [독혈지 개척자]를 획득하셨습니다!



* * *



그날, 남만의 밤은 유난히도 어둡고 길었다. 그러나 모든 일에는 시작과 끝이 있는 법.

모두가 잠든 깊은 밤. 긴급히 애뇌산으로 향했던 일백의 최정예 전사가 남만야수궁으로 귀환했을 때는 동이 틀 무렵이었고, 그런 그들의 모습을 목격한 이들의 숫자는 적지 않았다.

“자네 그 이야기 들었나? 간밤에 엄청난 일이 있었다더만.”

“무슨 이야기?”

“그, 왜. 글쎄 외궁 서문 쪽에 사는 몽씨 영감한테 들은 이야긴데…….”

“헉!”

“뭐여. 아직 말도 안 꺼냈는데.”

“그 영감이 아직도 살아 있었나? 분명히 작년에 죽은 줄 알았는데.”

“아이, 싯팔.”

아침 햇살과 함께 빠르게 퍼져 나간 소문의 골자는 이랬다.

간밤에 남만의 모처에서 큰일이 벌어졌고, 백족의 대족장인 백상과 소궁주 야율목이 일백의 최정예를 이끌고 외궁을 벗어났다는 것. 그리고 몇 시진 만에 귀환한 그들의 선두에 자신들의 궁주인 야수묘왕과 진태경이 있었다는 것.

평소 부족들 간의 분쟁에 무력으로 개입하지 않는 남만야수궁의 특성상, 궁주가 직접 나섰다는 것만으로도 제법 큰 사건이었다. 하지만 소문의 내용은 여기에서 끝나지 않았다.

“한데 문제가 생긴 곳이, 다름 아닌 애뇌산이었다더군.”

“애뇌산? 그 애뇌산을 말하는 거요?”

“그럼 남만에 다른 애뇌산도 있나? 오늘 날이 밝자마자 애뇌산에서 백 리 떨어진 마을에 사는 요족 상인들이 알려 준 거니까 확실할 걸세. 밤늦게까지 장부를 정리하다가 우연히 목격했다더군.”

오독문(五毒門)이라는 이름은 남만인들에게 있어 영원히 지워지지 않을 멍에와도 같다. 이 땅의 선조들은 오독문에 맞서 싸웠고, 숱한 희생을 치른 끝에야 지금의 질서와 법칙을 만들 수 있었으니까.

그런데 하필이면 일이 벌어진 곳이 오독문의 옛 본거지였던 애뇌산이라니.

평소였다면 입에도 담기 싫은 금지(禁地)였지만, 그곳에 문제가 생겼다면 이야기가 달라졌다.

“이런 미친. 계속 말해 보시오. 어서!”.

좌판이 끝없이 늘어선 저잣거리. 후미진 골목. 발길이 끊이지 않는 객잔…….

입에서 나온 목소리는 귀를 타고 전해졌고, 다시 또 다른 누군가의 입을 통해 흘러나왔다.

그리고 이 어수선한 분위기와 소문들은, 오늘 열릴 부족 대회의를 위해 모인 부족장들도 익히 인지하고 있었다.

현재 외궁, 내궁 가릴 것 없이 떠도는 소문이 생각 이상으로 정확하다는 것 역시도.

“지금 온 사방이 그 소문으로 난리요. 모르는 사람이 없더군.”

“더 큰 문제는 그게 단순한 헛소문이 아니라는 거지. 그렇지 않소?”

대회의를 위해 일 년 만에 한자리에 모인 그들이었지만, 서로의 안부를 물을 시간 따위는 없었다.

일찍이 내궁의 거대한 대전(大殿)에 각자 자리를 차지한 부족장들은 심각한 표정으로 대화를 이어 갔다.

“다들 미리 언질을 받았으니 알고 있겠지만, 이건 보통 일이 아니외다. 애뇌산. 그것도 독혈지에 있어야 할 놈들에게 벌써 일백에 달하는 정예가 희생되었으니.”

“천년지주가 나타났다는 이야기는 들었소만. 솔직히 본인으로서는 쉽게 믿을 수 없는 부분이오. 하나도 아니고 다섯 마리라는 부분에서는 더더욱.”

“믿기 힘들겠지만 전부 틀림없는 사실이오. 놈들의 사체도 남아 있다고 하니 거짓일 수가 없지. 애뇌산에 주둔하고 있던 전사들의 죽음에 진노한 궁주께서 독혈지까지 쫓아가 놈들을 추살했다고 했소.”

막힘없이 대답한 중년의 부족장이 나직이 한 마디를 덧붙였다.

“무림맹에서 온 그 젊은 한족. 열화신룡 진태경도 함께.”

이 자리에 모인 부족장들은 크기를 막론하고 남만의 일부분을 다스리는 영주들이다. 그들 역시 당연하게도 젊은 이방인에 관한 정보를 알고 있었고, 그에 대한 반응은 가지각색이었다.

“호오.”

“음.”

“크흠.”

어떤 부족장은 탄성과 함께 고개를 끄덕였고, 어떤 부족장은 불편한 헛기침과 함께 괜히 허공만 응시했다.

하지만 며칠 전의 분위기와 분명한 차이가 있다면, 이번만큼은 그 누구도 ‘빌어먹을 한족 놈’이라는 말을 꺼내지 않는다는 것이었다.

평소 한족을 꺼리는 부족장들조차 알고 있었다. 이번 사건 해결에 있어 진태경의 공이 결코 적지 않았음을.

“그가 아니었다면 이번 일이 이토록 빠르게 끝나지는 않았을 거요. 어쩌면 섣부르게 뒤쫓아 간 궁주께서 도리어 화를 입으셨을지도 모르…….”

쾅!

갑작스럽게 울려 퍼진 굉음에 이어지려던 목소리가 파묻혔다.

동시에 삼십여 쌍의 시선이 한곳으로 쏠렸다. 진태경이 언급되던 때부터 언짢은 표정을 짓고 있던 부족장 하나가 돌탁자를 두드린 것이다.

“내 어지간하면 참으려고 했는데, 더 이상은 불편해서 못 들어 주겠군. 말조심하게, 장 족장. 궁주께서는 당신이 생각하는 것보다 훨씬 강한 분이시니까. 아니, 남만의 모두가 마찬가지지. 나약한 한족 놈의 도움 따위는 필요 없어!”

대화를 주도하고 있던 중년의 부족장이 눈살을 찌푸렸다.

“아주 용맹하고 자부심 넘치는 말, 참으로 감명 깊게 들었네. 한데 그 나약한 한족 놈이 독혈지에서 천년지주 두 마리와 수천의 독물을 처리했다는 말은 못 들었나? 그가 바로 그 화왕(火王)의 진전을 이은 중원의 이름난 전사라는 건?”

“그, 그건…….”

“그리고 오 년 전, 궁주께서 친히 중재하셨음에도 불구하고 우리 부족의 영역을 침범한 게 누군가? 자네 아닌가? 주둥이가 독사에 물렸어도 말은 바로 하자고. 자네가 충성을 바치는 대상은 궁주가 아니라 백상 대족장일세. 자네가 그의 충견(忠犬)이라는 건 남만 모두가 알아.”

“뭣이? 충견! 이 개새끼가!”

“개새끼? 이 오독문이 남긴 독 찌꺼기 같은 새끼가 어딜……!”

쾅!

자리를 박차고 일어난 두 부족장이 서로를 향해 칼이라도 뽑아 들 것처럼 으르렁거리던 그 순간.

구구궁!

굳게 닫혀 있던 거대한 석문(石門)이 열리고, 세 인영이 대전을 향해 걸음을 내디뎠다.

저벅. 저벅.

어느새 고요해진 내부를 울리는 발걸음. 선두에서 문득 걸음을 멈춘 사내의 입술 사이로, 차가운 냉기를 머금은 목소리가 흘러나왔다.

“내가 대화를 방해한 모양이군.”

“……!”

“……!”

“개의치 말고 계속하게.”

그러나 어디에서도 목소리는 새어 나오지 않았다.

언제 그랬냐는 듯, 조금 전까지만 해도 오가던 고성은 삽시간에 사라지고 무거운 침묵이 주위를 짓눌렀다. 동시에 대립하고 있던 두 부족장의 표정에 희비가 엇갈렸다.

“오셨습니까, 백상 대족장님.”

굽실거리는 충견을 힐끗 바라본 백상이 중년의 부족장을 응시했다.

“흥미로운 대화였네. 계속 듣고 싶을 만큼.”

“…….”

“못 본 사이 많이 과묵해진 모양이군, 장 족장.”

입술을 깨문 중년의 부족장이 고개를 숙였다.

“백상 대족장님을 뵙습니다.”

백상의 우측에 시립 해 있던 요족의 대족장, 요희가 피식 웃었다.

“우리는 보이지도 않나 보네. 안 그래요, 흑웅 오라버니?”

“으응? 어어. 그럼 안 되지. 우리 어여쁜 요희를 앞에 두고도 예의를 갖추지 않다니. 그러면 안 돼.”

요희를 바라보며 헤벌쭉 웃고 있던 흑웅이 짐짓 엄한 표정을 지었지만, 이내 그를 향한 백상의 서늘한 시선에 통통한 몸을 움츠려야 했다.

“죄, 죄송합니다. 백 숙부. 한데 제가 무슨 잘못이라도…….”

“에이. 잘못은 무슨. 우리 착하고 잘생긴 흑웅 오라버니는 잘못한 거 없어요. 그렇죠?”

“그, 그렇지. 요희 말이 맞지.”

말없이 두 사람을 응시하던 백상은 혀를 차며 잠시 멈췄던 걸음을 옮겼다.

수십 명이 둘러앉을 수 있을 만큼 거대한 탁자에 존재하는 유일한 상석(上席). 그로부터 가장 가까운 세 개의 자리가 바로 궁주를 제외한 세 대족장들의 위치다.

드르륵. 탁.

앞서 차례대로 도착한 스물여덟 명의 부족장. 그리고 지금 막 도착한 세 명의 대족장까지. 도합 서른한 개의 자리가 저마다의 주인을 찾았다.

하지만 매해 보아 왔던 이 익숙한 풍경 속에서, 백상은 문득 이질감을 느끼며 입을 열었다.

“두 자리가 비는군.”

불쑥 흘러나온 한마디.

처음에는 그 누구도 백상이 한 말의 의미를 알아차리지 못했다. 그러나 잠시 부족장들이 느꼈던 의아함은, 뒤이어 들려온 요희의 웃음기 섞인 목소리에 사라졌다.

“그러게요. 희한하네. 왜 두 자리가 빌까?”

대회의에서 마련되는 자리는 오직 서른두 개뿐이었다. 백 년 전에도 그랬고, 지금도 마찬가지다. 부족장이 아니라면 소궁주조차 시립해 있어야 한다.

하지만 이제 단 하나만 남아 있어야 할 빈자리가, 오늘은 두 개다.

“도대체 왜…….”

그리고 누군가의 입술 사이로 의문이 담긴 중얼거림이 흘러나온 그 순간.

구구궁.

또다시 움직이는 거대한 석문 너머, 비로소 두 인영이 모습을 드러냈다. 그 모습을 확인한 백상의 눈동자가 깊숙하게 가라앉았다.
```

## Final English reading copy

```markdown
# Chapter 642

*Rustle.*

Along with the faint noise came a presence rapidly drawing closer from far away. The moment I noticed it, I aimed White Flame toward the source at lightning speed.

The same thought must have flashed through the Beast Miao King’s mind as he immediately drew up his internal energy.

*The Wraith of Ailao Mountain.*

But the next moment, that prediction missed spectacularly. When I caught sight of a pure-white shape beyond the blackened grass, I lowered the spearhead with a sigh.

“Muyaho?”

- Grrr!

*Shasha-shasha!*

White Tiger came running like the wind with a short but powerful cry, happily rushed toward me…… then passed right by without a second glance and flopped onto its back at the Beast Miao King’s feet.

- Pant. Pant. Pant.

“Yes, yes. You managed to find your way here. What a clever little fellow.”

At this point, I wondered if we should call it a silver retriever instead of a white tiger. Of course, it was about the size of ten retrievers put together.

*Come to think of it, the fact that this guy came back means……*

As if he had read the thought that surfaced in my mind, the Beast Miao King stroked White Tiger’s belly while it did its utmost to charm him and asked,

“Where are the others?”

- Grrrr.

White Tiger rose with a pleased growl, then suddenly let out a mighty roar. The beast’s cry rang through the thick darkness and Poison Mist. Before long, torchlight flickered in the distance.

The torches numbered roughly several dozen to a hundred.

And at the front were some familiar faces.

“Palace Lord.”

“Father! Are you all right?”

Baeksang, Yayul Mok, and the warriors of the Nanman Beast Palace approached, their faces unusually grim. The Fire Dragon Pavilion members came running toward me behind them.

“Captain!”

“Mujin, just in case you’re wondering, if you throw yourself into my arms or anything like that, you won’t die a pleasant death.”

“……Yes, sir.”

I immediately cut off Hyuk Mujin, who was charging toward me as if he had been possessed by the heroine of a tragic romance. Then I shrugged at the other members, who were just opening their mouths.

“To tell the whole story from the beginning would take a while…… Do you want to hear it here, or outside?”

There was no need to hear their answer.

Maybe if we were in a pleasant café with sentimental pop music playing in the background. But no one wanted to listen to a long story in the Poisonblood Grounds, with its desolate atmosphere and drifting Poison Mist.

And the System did not forget to remind me of the Quest I had briefly forgotten.

*Beep. Ding.*

> **System**
>
> - **Quest: My Love, Don’t Cross That Swamp** has been successfully completed!
>
> - **Quest Reward** will be granted!
>
> - You have acquired a considerable amount of **EXP** and **Fame**!
>
> - You have acquired **5 Top-Grade Poison-Warding Pearls**!
>
> - You have earned the very rare **Achievement: How’d You Get Back?**!
>
> - You have acquired the rare **Title: Poisonblood Grounds Pioneer**!

* * *

That night, Nanman’s darkness was unusually deep and long.

But everything had a beginning and an end.

Deep in the night, while everyone slept, the hundred elite warriors who had hurried to Ailao Mountain were still on their way back. By the time they returned to the Nanman Beast Palace, dawn was breaking, and quite a few people witnessed their arrival.

“Did you hear the story? Apparently something huge happened last night.”

“What story?”

“Well, you know. I heard it from old man Mong, who lives near the west gate of the Outer Palace……”

“Gasp!”

“What? I haven’t even started yet.”

“Was that old man still alive? I was sure he died last year.”

“Ah, fuck.”

The gist of the rumor that spread rapidly with the morning sunlight was as follows.

Something major had happened somewhere in Nanman the previous night. Baeksang, the great chieftain of the Bai people, and the Young Palace Lord Yayul Mok had led a hundred elite warriors out of the Outer Palace. And after returning only a few shichen later, the Beast Miao King and Jin Taekyung had been at the head of their procession.

The Nanman Beast Palace normally did not intervene in disputes between the tribes by force. Because of that, the fact that the Palace Lord had personally taken action meant that this was a fairly major incident.

But the rumor did not end there.

“But I heard the place where the trouble happened was none other than Ailao Mountain.”

“Ailao Mountain? You mean that Ailao Mountain?”

“Are there any other Ailao Mountains in Nanman? Yao merchants who live in a village a hundred li away told us about it at first light, so it must be true. Apparently they happened to see it while staying up late to finish their ledgers.”

To the people of Nanman, the name Five Poisons Sect was an everlasting yoke that could never be erased. Their ancestors had fought against the Five Poisons Sect, and only after countless sacrifices had they managed to establish the order and laws that existed today.

And yet, of all places, the incident had occurred in Ailao Mountain, the Five Poisons Sect’s former headquarters.

Under normal circumstances, it was a forbidden land they did not even want to mention. But if something had happened there, that changed things.

“What the hell? Keep going! Hurry!”

The marketplace, lined with endless street stalls. Secluded alleys. Inns where people came and went without end……

The voices that left one person’s mouth traveled from ear to ear, then flowed out through someone else’s lips.

And the chieftains who had gathered for the tribal grand council being held today were well aware of the commotion and the rumors.

They also knew that the rumors spreading throughout both the Outer Palace and Inner Palace were far more accurate than expected.

“The whole place is in an uproar over that rumor. There isn’t a single person who doesn’t know.”

“The bigger problem is that it isn’t merely a baseless rumor. Isn’t that right?”

The chieftains had gathered in one place for the first time in a year for the grand council, but they had no time to exchange pleasantries.

The chieftains, who had claimed their places early in the enormous main hall of the Inner Palace, continued their conversation with grave expressions.

“You all received advance word, so you already know this, but this is no ordinary matter. Ailao Mountain. Nearly a hundred elites have already been sacrificed to the creatures that were supposed to be in the Poisonblood Grounds.”

“I heard that Thousand-Year Spiders appeared. To be honest, I find that difficult to believe. Even more so when there were five of them, not just one.”

“It may be difficult to believe, but it is all true. Their corpses are still there, so it cannot be a lie. Enraged by the deaths of the warriors stationed at Ailao Mountain, the Palace Lord pursued them all the way to the Poisonblood Grounds and hunted them down.”

The middle-aged chieftain who had answered without hesitation added one more thing in a low voice.

“That young Han Chinese warrior from the Murim Alliance. Blazing Flame Divine Dragon Jin Taekyung was with him as well.”

The chieftains gathered here were lords who each governed a part of Nanman, regardless of the size of their tribe. Naturally, they all knew about the young outsider, and their reactions varied.

“Oh.”

“Hmm.”

“Ahem.”

One chieftain nodded with an exclamation of admiration. Another gave an uncomfortable cough and stared pointlessly into the empty air.

But if there was one clear difference from the atmosphere of a few days ago, it was that not a single person called him a “damned Han Chinese bastard” this time.

Even the chieftains who normally disliked Han Chinese people knew that Jin Taekyung’s contribution to resolving this incident had been far from insignificant.

“If it weren’t for him, this matter would not have ended so quickly. Perhaps the Palace Lord, who rashly went after them, might even have suffered harm instead……”

*Bang!*

A sudden boom swallowed the rest of his words.

At the same time, more than thirty pairs of eyes turned toward the same spot. One of the chieftains, who had worn an unpleasant expression ever since Jin Taekyung was mentioned, had struck the stone table.

“I tried to hold my tongue, but I can’t sit here and listen any longer. Watch your words, Chief Jang. The Palace Lord is far stronger than you think. No, the same goes for everyone in Nanman. We have no need for help from some weak Han Chinese bastard!”

The middle-aged chieftain who had been leading the conversation frowned.

“What brave and prideful words. Truly moving. But didn’t you hear that weak Han Chinese bastard dealt with two Thousand-Year Spiders and thousands of venomous beasts in the Poisonblood Grounds? That he is a renowned warrior of the Central Plains who inherited the Fire King’s legacy?”

“Th-that……”

“And five years ago, despite the Palace Lord personally mediating the matter, who was it that invaded our tribe’s territory? You, wasn’t it? Even if a venomous snake has bitten your mouth, let’s call things what they are. The one you swear loyalty to is not the Palace Lord, but Great Chieftain Baeksang. Everyone in Nanman knows that you are his loyal dog.”

“What? Loyal dog! You son of a bitch!”

“Son of a bitch? You piece of poisonous refuse left behind by the Five Poisons Sect—how dare you……”

*Bang!*

At that very moment, as the two chieftains leaped to their feet and snarled at each other as if they were about to draw their swords—

*Rumble……*

The enormous stone gate, which had been tightly shut, opened. Three figures stepped into the hall.

*Thud. Thud.*

Their footsteps echoed through the interior, which had suddenly fallen silent. The man at the front stopped, and a voice carrying a chill flowed from between his lips.

“Looks like I interrupted your conversation.”

“……!”

“……!”

“Don’t mind me. Carry on.”

But no voice emerged from anywhere.

As if nothing had happened, the shouting that had filled the hall only moments ago vanished in an instant, replaced by a heavy silence that pressed down on everyone. At the same time, the expressions of the two opposing chieftains split between joy and sorrow.

“Welcome, Great Chieftain Baeksang.”

Baeksang cast a sidelong glance at the groveling loyal dog, then fixed his gaze on the middle-aged chieftain.

“That was an interesting conversation. Interesting enough that I would like to hear more.”

“……”

“You seem to have become much quieter since I last saw you, Chief Jang.”

The middle-aged chieftain bit his lip and lowered his head.

“I greet Great Chieftain Baeksang.”

Yohi, the great chieftain of the Yao people, who stood at Baeksang’s right, let out a quiet laugh.

“We must be invisible. Right, Big Brother Heugung?”

“Hm? Oh, yes. That won’t do. To fail to show proper courtesy even with our lovely Yohi standing before them…… That won’t do at all.”

Heugung had been staring at Yohi with a goofy grin. He put on a deliberately stern expression, but Baeksang’s icy gaze made him hunch his plump body.

“S-sorry, Uncle Baek. But did I do something wrong……”

“Aww, what did you do wrong? Our good and handsome Big Brother Heugung hasn’t done anything wrong. Right?”

“R-right. Yohi’s right.”

Baeksang silently watched the two of them, clicked his tongue, and resumed walking.

There was only one head seat at the enormous table, which was large enough for several dozen people to sit around. The three seats closest to it belonged to the three great chieftains besides the Palace Lord.

*Scrape. Clack.*

The twenty-eight chieftains who had arrived earlier in turn, and the three great chieftains who had just arrived.

A total of thirty-one seats had found their owners.

But amid this familiar scene that Baeksang had seen every year, he suddenly felt something out of place and opened his mouth.

“Two seats are empty.”

The words slipped out unexpectedly.

At first, no one realized what Baeksang meant. But the chieftains’ brief puzzlement soon vanished when Yohi spoke in a voice filled with laughter.

“That’s true. How strange. Why would two seats be empty?”

Only thirty-two seats were prepared for the grand council. That had been true a hundred years ago, and it was still true now. Anyone who was not a chieftain—even the Young Palace Lord—was expected to stand in attendance.

There should have been only one empty seat.

Today, there were two.

“Why in the world……”

And just as a puzzled murmur escaped someone’s lips—

*Rumble……*

Beyond the enormous stone gate that began moving once again, two figures finally appeared.

Baeksang’s eyes sank deeply as soon as he saw them.
```
