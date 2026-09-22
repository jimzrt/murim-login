<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0702.txt",
      "sha256": "ee88861f60bfcd2dd3f93b3f272dabbd33c926ced8e7f595946f7553969c905e",
      "bytes": 13802
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9d4720c58adf44a89c2bb0887c1e9a64c3a25b28d7a84b051de99b78407f57e3",
      "bytes": 2284
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "377408edd6bffa87540301dadb4da6acf3c4b03a8a29b32bdd22758532ccb70f",
      "bytes": 206401
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "83cdc10aaf72b85d54496dcc41aa6864be4167c74821f8394dd76b96b9a87687",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a83c52dc73ada82248f7b4570ce47218a909273f72837c33dfc261c5e8365651",
      "bytes": 1926
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e2ff3e3baaf4add61e9d7d076de198967ae65847dc243a4066b6f1c8d793aca5",
      "bytes": 622
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "2160b15213bb697cf3417458d9ea1f77f88c596922a0abf7a4da4836a0ca2b04",
      "bytes": 841
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "bc60083bd3985d471b20cc751f30b7f938e505cd6b67ae1b4600721dfc64e0e1",
      "bytes": 787
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "fe31a303e569801f37c85c805f30f030f54a120d14e90ff5747520a8af64533e",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "39588518517f0306c0f8c6983a12c725399d58da9336fd2022f2fd66d620875e",
      "bytes": 216408
    }
  ],
  "estimated_tokens": 11553
}
-->

# Durable State Update — Chapter 702

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 702. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 702. Profile updates may replace only one
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
  "chapter": 702,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 702,
    "continuity_sources": [702],
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
    "The rift's demonic qi is causing the humans and beasts remaining in the Inner Palace to mutate, and the Southern Heaven Demon Empress grows stronger as the demonic qi thickens.",
    "The Southern Heaven Demon Empress is Honglan, the creator of the rift behind the Inner Palace, and she is fighting Jin Taekyung while pursuing the Lord of Heaven's plan.",
    "The Southern Heaven Demon Empress's masked hunting dog regenerates from shattered bones and severe wounds through a power that defies heaven and appears unable to feel pain.",
    "Jin Taekyung is injured but continues fighting the Southern Heaven Demon Empress and the masked man alongside the exhausted guardian spirit.",
    "Jin and the guardian spirit have divided the two opponents between them and must end the battle before the Inner Palace's humans and beasts complete their mutation.",
    "The Lord of Heaven is strongly interested in Jin, but the reason remains unknown; Jin believes this interest restrained the Southern Heaven Demon Empress from killing him in Hubei Province.",
    "Jin's identity as Jeok Cheongang's sole Disciple and the Fire Gate Clan's successor makes him a major obstacle to Dark Heaven's plans.",
    "Jin provoked the Southern Heaven Demon Empress into attacking despite knowing that she is at least comparable to the Ten Kings and grows stronger through the rift.",
    "Jin's thigh has been cut, and the confrontation with the Southern Heaven Demon Empress remains unresolved."
  ],
  "continuity_sources": [
    701
  ],
  "open_questions": [
    "What is the masked man's identity, and what is his relationship with the Great Snow Fiend?",
    "Why is the Lord of Heaven interested in Jin Taekyung?",
    "Can Jin and the guardian spirit stop the mutation in the Inner Palace before it finishes?",
    "Can Jin survive and continue fighting after the Southern Heaven Demon Empress's attack?"
  ],
  "safe_through": 701,
  "temporary_decisions": [
    "Use magical power for 마력 and demonic qi for 마기.",
    "Use defying heaven for 역천 and Regeneration for 재생.",
    "Use masked man for 복면인 and leave his identity unresolved.",
    "Keep Jin's combat dialogue blunt, profane, and deliberately provocative."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 일격     | **One Strike**                         |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 철구 | **iron balls** | Training weights attached to Taekyung. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 701
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 701
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an injured leader fighting the Southern Heaven Demon Empress and her masked hunting dog to save the humans and beasts in the Inner Palace.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 701
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 701
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, the former Lower District Sect singing courtesan, the creator of the massive rift behind Nanman's Inner Palace, and the enemy who grows stronger as its demonic qi thickens while pursuing the Lord of Heaven's plan.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 697
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 699
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃702화



슈화악!

곧게 편 수도(手刀)가 바람을 가르며 내리꽂힌다.

가늘면서도 새하얀, 살면서 물 한 방울이나 묻혀 봤을까 싶은 손.

그러나 진태경은 안다. 저 손에 얼마나 많은 핏물이 흘렀는지.

눈이 부시도록 환하게 웃는 남천마후의 아름다운 얼굴 뒤에, 어떤 어둠이 도사리고 있는지.

‘괴물.’

새삼 뇌리에 떠오른 두 글자.

유성처럼 떨어져 내린 핏빛 강기가 진태경의 정수리를 파고들려는 그 순간, 못 박힌 듯 굳어 있던 두 다리가 움직였다.

서걱!

지면이 두부처럼 갈라진다. 한 끗 차이로 강기를 피해 낸 진태경이 섬전처럼 창을 뻗었다.

슈확!

가공할 만한 속도와 힘. 더불어 무서우리만치 정확하게 일점(一點)을 향해 쏘아지는 창날.

그것은 일평생 권각을 연마하여 초절정의 경지에 오른 권사(拳士)라 할지라도 감히 맞받아치지 못할 일격이었지만, 남천마후는 달랐다.

아니.

적어도 오늘의 남천마후에게는 충분히 그럴 만한 힘과 자격이 있었다.

콰드드득!

공수납백인(空手納白刃).

합장(合掌)하듯 마주한 남천마후의 양손 사이로, 겁화가 일렁이는 창날이 파르르 떨린다.

진즉 잿가루가 되고도 남았을 새하얀 손에는 강대한 기운이 집약되어 있었다.

주름 하나 없이 팽팽한 입꼬리가 슬며시 올라갔다.

“고작 이 정도로…….”

비웃음 가득한 목소리가 흘러나온 그 순간.

툭. 투둑.

점점이 떨어지는 핏물의 존재를 확인한 남천마후가 입을 다물었다.

반 박자 늦게 느껴지는 통증과 함께 쑥스럽다는 듯 웃는 한 사람의 얼굴이 시야에 들어온다.

“어, 내가 깜빡하고 말 안 했구나. 이거 만년한철이야.”

“……!”

“근데 뭐라고?”

고운 미간이 일그러진 그때, 진태경이 손에 쥐고 있던 창대를 놓으며 양팔을 뻗었다.

‘장력(掌力)?’

하지만 남천마후의 짐작은 보기 좋게 빗나갔다.

쉬쉭!

난데없이 목과 가슴을 향해 쏘아지는 두 자루의 비수. 당장 피하기에는 너무나도 가까운 거리다.

어쩔 수 없이 붙잡고 있던 창날을 놓은 남천마후가 크게 소매를 떨쳤다.

콰아아!

풍성한 옷소매에서 터져 나온 바람이 비수를 날려 보낸 순간. 진태경의 발끝이 느릿하게 기울어지던 백염(白炎)의 창대 끝을 잡았다.

아니, 걷어찼다.

‘……뭐?’

걷어차?

그것도 지금 같은 상황에서 가장 큰 도움이 될 신병이기를?

충격과도 같은 의문과 함께, 섬광이 남천마후의 얼굴을 향해 날아들었다.

쐐애액! 촤악!

그야말로 찰나에 벌어진 일이었고, 그 이상으로 변칙적인 공격이었기에 완전히 피하는 것은 불가능에 가까웠다.

본능적인 움직임으로 고개를 틀었던 남천마후는 귓불에서 전해지는 통증을 느끼며 눈을 부릅떴다.

“감히!”

귀걸이만 깨졌다면 이토록 분노하진 않았을 것이다. 제법 마음에 든 물건이긴 했어도 얼마든지 다시 구할 수 있으니까.

그러나 귓불이 찢어진 것으로도 모자라 머리카락도 잘렸다.

언제나 그녀의 자랑거리였던 풍성하고 윤기 나는 머리카락이, 무려 절반이나 잘려 나간 것이다.

“죽엇!”

콰아아아아!

잠시 주춤했던 미증유의 기운이 가녀린 전신을 타고 솟구쳤다.

거대한 바위도 단번에 으스러트릴 것만 같은 압력. 그러나 남천마후는 미처 알지 못했다.

젊다 못해 새파란 눈앞의 적이, 한때 천근이 훌쩍 넘는 철구를 매달고 절벽을 올랐음을.

콰직. 우드득!

반경 십여 장을 짓누르는 압력에 지면이 꺼지고, 몸부림치던 인간과 맹수들의 사지가 꺾여 나간다.

- 크륵, 크르륵!

“끄아아아악!”

핏물과 단말마(斷末摩)가 흘러넘치는 공간 속, 압력을 견뎌 낸 진태경이 발을 굴렀다.

쾅!

발끝을 따라 피어오른 한 줄기 화염과 함께 나아가는 신형.

그와 동시에 맹렬하게 휘둘러진 손끝에서, 언제 쥐었는지 모를 한 자루의 창이 벼락처럼 공간을 갈랐다.

쐐애애애액! 꽈앙!

굉음과 함께 터져 나온 기파(氣波)가 세상을 뒤흔든다. 창날의 옆면을 정확히 잡아챈 남천마후의 손에서 거대한 기운이 일렁였다.

콰직!

창날을 감싸던 열양지기도, 솜씨 좋은 대장장이가 백 번도 넘게 담금질한 강철도 두부처럼 으스러진다.

남천마후의 입가에 살기 어린 미소가 맺혔다.

‘멍청한 녀석.’

진태경의 실수는 만년한철(萬年寒鐵)로 이루어진 희대의 신병이기를 스스로 포기했다는 것이다.

지금부터 남천마후는 감히 자신의 아름다운 몸에 상처를 입힌 것으로도 모자라, 귀중한 머리카락마저 자른 저 어린놈에게 그에 마땅한 대가를 치르게 할 생각이었다.

‘최대한 몸 성히 데려가려 했는데. 아무래도 안 되겠어.’

처음에는 지엄하신 천주께서 진태경에게 흥미를 보이신다기에, 그분의 충실한 종복으로서 저 어린놈을 잡아 바치려 했었다.

하지만 이제는 생각이 바뀌었다.

지금 남천마후의 눈에 비친 진태경은 앙칼진 고양이가 아니라 한 마리의 당당한 맹수였다.

비록 나이는 어려도 대호(大虎) 못지않은 날카로운 이빨과 발톱을 지닌.

그건 자칫하면 이 아름다운 육신에 더 큰 상처를 입힐 수도 있는 무기다.

남천마후의 붉은 안광(眼光)에 섬전처럼 들이닥치는 진태경의 모습이 비쳤다.

‘팔다리 한두 개 날아가는 것 정도는 감수하렴. 어차피 나중에 붙여 줄 테니.’

마음속으로 뇌까린 남천마후가 양 소매를 떨쳤다.

파파팟!

으스러진 창날의 파편이 수십, 수백으로 나뉘어 공간을 뒤덮었다.

하나하나가 강기를 머금은 암기의 파도 앞에서, 진태경은 한 치의 망설임도 없이 힘껏 그러쥔 주먹을 내질렀다.

콰아아아!

멸염신권(滅炎神拳). 굳은살로 가득한 주먹의 끝에서 튀어나온 화룡이 수백 개의 파편을 집어삼킨다.

초고온의 열기에 벌겋게 달아오른 파편들이 쇳물이 되어 지면을 적셨다.

치이이익.

하지만 소나기처럼 쏟아져 내리는 쇳물 아래, 공간을 격하며 쏘아진 진태경을 기다리고 있는 것은 남천마후의 섬섬옥수였다.

후웅!

바람을 지우며 다가오는 다섯 개의 손가락.

마치 갈퀴처럼 휘어진 그것이 오른팔을 노리며 휘둘려진 순간, 진태경은 처음부터 예상이라도 했던 것처럼 몸을 비틀었다.

이대로면 뜯겨 나갈 오른팔을 지키기 위한 회피가 아닌, 스스로 적에게 목을 들이대는 자살 행위.

그러나 동시에, 상대의 의표(意表)를 찌르는 치명적인 한 수이기도 했다.

‘이런 미친……!’

남천마후의 마음속에서 비명이 울려 퍼졌다.

존엄하신 천주께서 흥미를 보이신 이상, 그녀에게 있어 진태경은 절대 죽어서는 안 되는 존재다.

애당초 그를 생포하고자 하는 이유 역시 천주에 대한 충성심의 표출일 뿐.

아직 별다른 명령도 내려지지 않았는데 진태경이 자신의 손에 죽는다면 천주의 분노를 홀로 감당해야 할지도 몰랐다.

‘안 돼!’

입 안에서만 감도는 외침과 함께, 남천마후는 황급히 용솟음치던 공력을 끌어당겼다.

동시에 오직 한 가지 목적을 위해 움직인 전신의 근육과 기혈이 뒤틀리고, 역류(逆流)의 파도가 그녀를 덮쳤다.

울컥!

“쿠에에엑!”

몸속 깊숙한 곳으로부터 솟구친 피 화살이 남천마후의 입술 사이로 뿜어진다.

마지막 순간, 가까스로 방향을 뒤튼 손끝의 강기가 진태경의 목을 비껴 나갔다.

쉭! 피핏!

칼날 같은 바람에 베어 나가는 살갗.

그러나 진태경은 조금도 동요하지 않았다. 아니, 처음부터 동요할 이유가 없었다.

‘이 순간만을 기다렸으니까.’

차갑게 식은 머릿속은 이미 모든 계산을 끝마쳤다.

진태경이 판단한 남천마후의 무위는 낮게 잡아도 십왕(十王). 어쩌면 삼성(三星)에 버금간다.

그녀가 사용하는 무공의 수준은 서천마군과 비등하거나 오히려 못할 수도 있지만, 그 간극을 메우고도 남을 만큼의 압도적인 공력을 지녔다.

그리고 이런 수준의 고수를 상대할 때에는 오직 한 가지 방법밖에 없었다.

단 하나의 틈.

진태경은 스스로의 목숨을 판 돈 삼아 도박을 걸었고, 처음이자 마지막이 될 기회를 얻었다.

그리고…….

‘다시 한번. 목숨을 건다.’

인벤토리 오픈. 소환.

뇌리에 울려 퍼지는 명령어와 함께 섬전처럼 손을 뻗는다.

서걱!

이토록 강대한 괴물의 것이라고는 믿겨 지지 않는, 가느다란 팔목이 깨끗이 잘려 나감과 동시에 비명이 터져 나왔다.

“아아아아악!!”

마기에 휩싸여 몸부림치는 남만야수궁의 어떤 생명체보다, 아니 진태경이 들어본 모든 것을 통틀어 가장 크고 고통에 찬 비명소리.

어찌 보면 당연한 일이다.

사람은 타고나길 망각의 동물이며, 고통을 주는 것에 익숙해진 강자는 자신의 고통을 잊기 마련이니까.

하지만 그럼에도 불구하고, 상대는 남천마후였다.

“진태경-!”

쉬쉭!

찢어지는 듯한 외침과 함께 쏘아지는 신형.

혼탁한 어둠이 뒤섞인 남천마후의 핏빛 안광을 마주한 진태경은 본능적으로 깨달았다.

이번만큼은 완전히 피할 수도, 막을 수도 없다는 것을.

막대한 내상을 입은 탓인지 자세는 흐트러져 있었고, 피를 토해 내면서까지 억지로 끌어올린 공력은 거칠기 짝이 없었지만…… 그렇기에 더 위험하다.

아니, 진정으로 위험한 것은 지금 남천마후에게서 느껴지는 살심(殺心)이었다.

“감히! 감히 네놈 따위가!”

애당초 행운은 한 번뿐이었다.

분노와 고통에 사로잡혀, 주인에 대한 충심(忠心)마저 잊은 괴물이 강력한 기운에 휩싸인 일장을 뻗는다.

세상이 느려지고 어둠과 핏빛 강기가 혼탁하게 뒤섞인 장력이 공간을 지우며 달려든다.

콰아아아아!

바다가, 태산이 일어나 덮치는 듯한 압도적인 힘.

전신의 털이 바짝 곤두서는 듯한 두려움이 전신을 사로잡았지만, 진태경은 알고 있었다.

이곳에서 단 한 걸음이라도 물러나면 모든 것이 끝장이라는 것을.

목숨을 내던져서라도 나아가야 한다는 것을.

‘와라.’

무엇을 향한 부름인지 모를 마음속 뇌까림과 함께, 진태경의 발끝이 피에 젖은 흙을 밟는다.

콰득.

목숨만큼이나 무거운 공력이 실린 한걸음에 지면이 움푹 주저앉고, 이내 열기를 머금고 폭발했다.

쾅!

지면을 스치듯 낮게 숙여진 신형이 포탄처럼 쏘아진다.

인간의 것이라고는 믿겨 지지 않는, 미증유의 기운이 실린 새하얀 손바닥이 시야를 가득 메운다.

핏빛 섬광 사이로 악귀처럼 일그러진 한 사람의 얼굴도 함께.

“죽엇!”

바로 그때.

‘인벤토리 오픈. 소환.’

당장이라도 장력을 쏟아낼 것처럼 한껏 펼쳐져 있던 진태경의 손이 오므려졌다.

텅 비어 있던 손아귀에 서늘한 창대가 잡히고, 길게 뻗어 나간 창날이 두 사람 사이의 공간을 지웠다.

그리고…….

쐐애애액! 쉭!

거친 파공성과 함께 목덜미를 아슬아슬하게 스쳐 지나가는 창날. 그와 동시에 남천마후의 눈동자에 희미한 환희가 떠올랐다.

‘읽었다. 완벽하게.’

진태경이 사용하는 저 기예(技藝)는 분명 놀랍고 위협적이지만, 남천마후는 혼잡한 전투의 흐름 속에서 모든 것을 정확히 예측해냈다.

아니, 그렇다고 믿었다.

곧장 진태경의 목을 날려 버리려던 그 순간. 문득 등 뒤에서 불어온 서늘한 바람을 느끼기 전까지는.

쉭.

“……!”

귓가를 파고드는 미세한 파공성.

본능적으로 몸을 회전시킨 남천마후의 옆구리를, 얼음처럼 차갑고 극도로 예리한 무언가가 할퀴고 지나간다.

서걱!

분수처럼 터져나오는 핏물과 함께 근육과 핏줄이 잘리고 기혈(氣血)이 뒤엉키는 것이 느껴졌다.

‘이, 이건.’

역류다.

앞서 입은 내상을 가라앉히기도 전에 찾아온 두 번째 역류인 동시에, 지금껏 입은 어떤 상처보다 치명적인.

‘처음부터…… 이걸 노린 거야.’

하얗게 물든 시야 속을 스친 한 줄기 깨달음.

울컥. 솟구치는 핏물을 삼키며 돌아선 남천마후는 마침내 볼 수 있었다.

고오오오옹.

주인의 부름에 응한, 투명한 창날의 끝에서 휘몰아치는 청백색의 화염을.

깊숙이 가라앉은 한 사람의 눈동자 아래, 소리 없이 달싹이는 입술이 완성시킨 두 글자를.

일섬(一殲).

남천마후의 눈이 부릅떠진 그 순간.

- 인간!

갑작스럽게 울려 퍼진 누군가의 다급한 의념(疑念)과 함께, 남만의 그 누구도 본 적 없는 거대한 와류(渦流)가 터져 나왔다.

콰아아아아!
```

## Final English reading copy

```markdown
# Chapter 702

Shwaaak!

A straightened hand-blade sliced through the air and came crashing down.

A slender, snow-white hand—one that looked as though it had never had a single drop of water touch it in its life.

But Jin Taekyung knew.

He knew how much blood had flowed from that hand.

He knew what kind of darkness lurked behind the beautiful face of the Southern Heaven Demon Empress, smiling so brightly that it hurt to look at.

*Monster.*

Those two words surfaced in his mind once more.

At the moment the blood-red Force falling like a meteor sought to pierce the crown of Jin Taekyung’s head, his two legs, which had been frozen stiff as though nailed to the ground, finally moved.

Shhk!

The earth split apart like tofu. Jin Taekyung narrowly evaded the Force and thrust his spear forward like a flash of lightning.

Shwaaak!

Terrifying speed and power. Along with them, a spearhead shot toward a single point with frightening precision.

Even a fistfighter who had honed his hand-to-hand techniques for his entire life and reached the Supreme Peak realm would have been unable to meet that strike head-on.

But the Southern Heaven Demon Empress was different.

No.

At the very least, today’s Southern Heaven Demon Empress possessed enough power and qualification to do so.

Krrrkkk!

*Empty-Hand Seizes the Blade.*

The spearhead, hellfire flickering around it, trembled between the Southern Heaven Demon Empress’s palms, which she had brought together as though in prayer.

Her snow-white hands, which should have been reduced to ash long ago, held a tremendous concentration of energy.

The corners of her smooth lips, free of even a single wrinkle, slowly lifted.

“With only this much…”

The instant her voice, filled with mockery, emerged—

Plop. Plip.

The Southern Heaven Demon Empress noticed the drops of blood falling one by one and closed her mouth.

As the pain arrived half a beat late, she saw Jin Taekyung smiling sheepishly at her.

“Oh, I forgot to mention. This is Ten-Thousand-Year Cold Iron.”

“……!”

“But what were you saying?”

The Southern Heaven Demon Empress’s delicate brow twisted. At that moment, Jin Taekyung released the spear shaft in his hands and stretched out both arms.

*Palm Force?*

But the Southern Heaven Demon Empress’s guess missed its mark completely.

Shhk! Shhk!

Two daggers suddenly shot toward her throat and chest. They were too close for her to evade immediately.

Left with no choice but to release the spearhead she had been holding, the Southern Heaven Demon Empress shook her sleeves violently.

Whoooosh!

The wind that burst from her voluminous sleeves sent the daggers flying away.

At that instant, Jin Taekyung’s toe caught the end of the White Flame’s spear shaft, which had been slowly tilting.

No—he kicked it.

*…What?*

He kicked it?

And in a situation like this, he had kicked away the divine weapon that would have helped him most?

Along with that shockingly baffling question, a flash of light shot toward the Southern Heaven Demon Empress’s face.

Shwaaack! Slash!

It happened in the blink of an eye, and the attack was even more irregular than it was fast. Fully evading it was nearly impossible.

The Southern Heaven Demon Empress turned her head on instinct and felt pain shoot from her earlobe. Her eyes flew open.

“How dare you!”

She would not have been this furious if only her earring had shattered. It had been a possession she rather liked, but she could always obtain another one.

But her earlobe had been torn, and her hair had been cut as well.

Fully half of her thick, glossy hair—always a source of pride—had been cut away.

“Die!”

Kraaaaaash!

The unprecedented energy that had faltered for a moment surged through her slender body.

The pressure seemed capable of crushing even a massive boulder in an instant.

But the Southern Heaven Demon Empress did not know.

The young—no, the impossibly young—enemy before her had once climbed a cliff with iron balls weighing well over a thousand geun strapped to his body.

Crack. Crrrunch!

The earth sank beneath the pressure crushing everything within a radius of over ten jang, while the limbs of the humans and beasts struggling in the area twisted and snapped.

—Krrk, krrrk!

“Aaaaaagh!”

Amid the space overflowing with blood and dying screams, Jin Taekyung, who had endured the pressure, stamped his foot.

Boom!

Along with a line of flame that rose from his toe, his body shot forward.

At the same time, a spear that no one knew when he had taken hold of split the air like lightning as it swung fiercely from his fingertips.

Shwaaaargh! Boom!

A shockwave burst out with a deafening roar and shook the world. The Southern Heaven Demon Empress’s hand, which had caught the side of the spearhead with perfect precision, was filled with surging power.

Crack!

The Scorching Yang Qi surrounding the spearhead, along with the steel that a skilled blacksmith had folded and tempered more than a hundred times, crumbled like tofu.

A murderous smile formed at the corner of the Southern Heaven Demon Empress’s mouth.

*Foolish boy.*

Jin Taekyung’s mistake was that he had given up a peerless divine weapon made of Ten-Thousand-Year Cold Iron of his own accord.

From this moment on, the Southern Heaven Demon Empress intended to make that young brat pay the proper price—not only for daring to injure her beautiful body, but for cutting off her precious hair as well.

*I intended to take him back in the best condition possible. But I suppose that won’t do anymore.*

At first, after hearing that the exalted Lord of Heaven had taken an interest in Jin Taekyung, she had intended to act as the Lord’s faithful servant and capture the young man to offer him up.

But now she had changed her mind.

The Jin Taekyung reflected in the Southern Heaven Demon Empress’s eyes was no longer a sharp-tempered cat.

He was a proud beast.

Although he was young, he possessed teeth and claws as sharp as those of a great tiger.

And those were weapons that might inflict even more serious wounds on this beautiful body of hers if she made a mistake.

Jin Taekyung’s figure rushed into the Southern Heaven Demon Empress’s blood-red eyes like a flash of lightning.

*You should be prepared to lose a limb or two. I’ll reattach them later anyway.*

Muttering inwardly, the Southern Heaven Demon Empress shook both sleeves.

Papapapap!

The shattered spearhead split into dozens, then hundreds, of fragments and covered the air.

Before the wave of hidden weapons, each carrying Force, Jin Taekyung thrust out his tightly clenched fist without a moment’s hesitation.

Kraaaaaash!

The Flame-Extinguishing Divine Fist.

A fire dragon sprang from the end of his callused fist and swallowed hundreds of fragments.

The fragments, heated red-hot by the extreme temperature, melted into liquid iron and poured across the ground.

Hissssssss.

But beneath the molten iron raining down like a shower, what awaited Jin Taekyung as he shot through the air was the Southern Heaven Demon Empress’s slender, jade-like hand.

Whoosh!

Five fingers swept toward him, erasing the wind.

Curled like a rake, they swung toward his right arm.

Jin Taekyung twisted his body as though he had anticipated it from the beginning.

It was not an evasion meant to protect the right arm that would otherwise be torn away. It was a suicidal act in which he willingly offered his neck to the enemy.

But at the same time, it was also a lethal move that struck at an opening the opponent had never expected.

*What kind of lunacy is this…!*

A scream rang out in the Southern Heaven Demon Empress’s mind.

Now that the exalted Lord of Heaven had taken an interest in Jin Taekyung, he was someone who absolutely could not die.

Her original reason for capturing him had merely been an expression of loyalty to the Lord of Heaven.

If Jin Taekyung died by her hand before any particular order had been issued, she might have to bear the Lord of Heaven’s fury alone.

*No!*

Along with the cry that never escaped her mouth, the Southern Heaven Demon Empress hurriedly pulled back the internal energy that had been surging upward.

At the same time, the muscles and qi-blood throughout her body, which had moved solely toward that one purpose, twisted.

A wave of backflow overwhelmed her.

Urk!

“Kwaaaagh!”

A jet of blood surged up from deep within her body and spurted between the Southern Heaven Demon Empress’s lips.

At the final moment, the Force around her fingertips, whose direction she had barely managed to twist, veered past Jin Taekyung’s throat.

Shhk! Spit!

His skin was sliced away by wind as sharp as a blade.

But Jin Taekyung did not waver in the slightest.

No. He had no reason to waver from the beginning.

*I’ve been waiting for this moment.*

His mind, cold as ice, had already finished calculating everything.

Jin Taekyung estimated the Southern Heaven Demon Empress’s martial power to be at least that of the Ten Kings.

Perhaps she was even comparable to the Three Saints.

The level of the martial arts she used might have been equal to or even inferior to that of the Western Heaven Demon Lord, but she possessed overwhelming internal energy enough to more than make up for the difference.

And when facing a master of this level, there was only one possible method.

A single opening.

Jin Taekyung had placed his life on the table as his wager and obtained a chance that would come only once.

And…

*I’ll bet my life again.*

*Inventory Open. Summon.*

Along with the commands ringing through his mind, he thrust out his hand like a flash of lightning.

Shhk!

A slender wrist, impossible to believe belonged to such a powerful monster, was cleanly severed.

A scream burst forth.

“Aaaaaaaagh!”

It was louder and filled with more pain than the scream of any creature of the Nanman Beast Palace writhing under the demonic qi.

No—it was the loudest, most agonized scream Jin Taekyung had ever heard in his life.

In a way, it was only natural.

Humans were animals born to forget, and powerful people who had grown accustomed to inflicting pain inevitably forgot their own.

But even so, his opponent was the Southern Heaven Demon Empress.

“Jin Taekyung—!”

Shhk!

Along with her ripping cry, her body shot forward.

As Jin Taekyung met the Southern Heaven Demon Empress’s blood-red eyes, clouded with darkness, he realized on instinct.

This time, he would be unable to evade completely.

He would be unable to block completely.

Perhaps because of the massive Internal Injury she had suffered, her stance was unsteady. The internal energy she had forcibly dragged up while vomiting blood was rough beyond measure.

But that was precisely why she was more dangerous.

No.

The truly dangerous thing was the killing intent Jin Taekyung felt from the Southern Heaven Demon Empress.

“How dare you! How dare someone like you!”

Luck only came once.

A monster consumed by anger and pain, one that had even forgotten its loyalty to its master, thrust out a palm wrapped in powerful energy.

The world slowed.

A palm strike in which darkness and blood-red Force were muddled together rushed forward, erasing the space in its path.

Kraaaaaash!

It was an overwhelming force, as though a sea and a mountain had risen and come crashing down upon him.

Fear that made every hair on his body stand on end seized Jin Taekyung.

But he knew.

If he took even a single step backward here, everything would be over.

He had to move forward, even if he had to throw away his life to do it.

*Come.*

Along with the thought he muttered inwardly, though he did not know what he was calling toward him, Jin Taekyung’s foot stepped onto the blood-soaked earth.

Crush.

The ground sank beneath a single step carrying internal energy as heavy as life itself, then exploded while holding the heat within it.

Boom!

His body, crouched low enough to skim the ground, shot forward like a cannonball.

A snow-white palm filled his field of vision, carrying unprecedented energy that was impossible to believe belonged to a human.

A face distorted like a Fiend appeared within the blood-red flash as well.

“Die!”

Right then—

*Inventory Open. Summon.*

Jin Taekyung’s hand, spread wide as though it were about to unleash Palm Force, suddenly clenched.

A cold spear shaft appeared in his empty palm, and the spearhead extending from it erased the space between the two of them.

And then…

Shwaaaargh! Shhk!

The spearhead passed within a hair’s breadth of the back of the Southern Heaven Demon Empress’s neck with a harsh sound as it tore through the air.

At the same time, faint delight rose in her eyes.

*I read him. Perfectly.*

The technique Jin Taekyung used was certainly astonishing and threatening.

But amid the chaotic flow of battle, the Southern Heaven Demon Empress had accurately predicted everything.

Or so she believed.

Until the instant before she cut off Jin Taekyung’s head, when she suddenly felt a chill of wind blow from behind her.

Shhk.

“……!”

A faint sound of air being cut pierced her ears.

The Southern Heaven Demon Empress instinctively spun around.

Something as cold as ice and razor-sharp raked across her side.

Shhk!

Along with blood bursting out like a fountain, she felt her muscles and veins sever and her qi-blood become tangled.

*This… this is…*

Backflow.

A second backflow had struck before she could even settle the Internal Injury she had suffered earlier—and it was more fatal than any wound she had received until now.

*From the beginning… this was what he was aiming for.*

A flash of insight passed through her whitened field of vision.

The Southern Heaven Demon Empress swallowed the blood surging up her throat and turned around.

At last, she saw it.

Goooooong.

Blue-white flames whirled around the tip of a transparent spearhead in answer to its master’s call.

Beneath the deeply sunken eyes of one man, silently moving lips completed two words.

*One Annihilation.*

The moment the Southern Heaven Demon Empress’s eyes flew wide—

—Human!

Along with someone’s sudden, urgent thought, a massive vortex unlike anything anyone in Nanman had ever seen exploded outward.

Kraaaaaash!
```
