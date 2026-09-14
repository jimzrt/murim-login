<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0092.txt",
      "sha256": "f83c3af08eb9d93c916d52b2fd644c7e8474623f4944b91f2b9cac7317630e1b",
      "bytes": 12890
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2f155b5c91353a1446db616e15b9fbb2faef6291947ecf0cd80a3035ad876165",
      "bytes": 3712
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5b811828f19441068845470455cc9193de2cdba2dcb677fe2f155dde9d77664e",
      "bytes": 10008
    },
    {
      "path": "characters/Im Chunsoo.md",
      "sha256": "1822e67cbfecc8194c5d426d4d66054c853cc824d7ae4e3cd4412fad8df38e35",
      "bytes": 666
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "001abc20dac7b681eb32488b68d28aa826c22fd12b929fc471faa7ff5ed46a5e",
      "bytes": 23901
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c596007ffe4741722024812ce7f3b0760859fd83f4cd08bbfad8d8fb719b3a00",
      "bytes": 9066
    }
  ],
  "estimated_tokens": 13529
}
-->

# Durable State Update — Chapter 92

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 92. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 92. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 92,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 92,
    "continuity_sources": [92],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "The party sells The Minotaur's Labyrinth byproducts and Magic Gems to the Administration.",
    "Im Kkeokjeong warns that Sangdong Guild is a powerful local Guild capable of threatening Peace Guild.",
    "Im Chunsoo is Sangdong Guild's A-rank Guild Master and founder, known as Frozen for his exceptional ice magic.",
    "Im Changsoo transferred the promised four billion won to Jin Taekyung after Im Chunsoo learned about his transfers and beat him.",
    "Kim Jeonghee is Taekyung and Hayeon's mother; Hayeon knows that she secretly worked in a restaurant kitchen for over a year, and Jeonghee quit after the owner insulted and attacked Taekyung.",
    "Taekyung's father died when a Gate opened downtown during the Great Cataclysm.",
    "Kim Minsu is the restaurant owner's son, a D-rank Hunter in Sangdong Guild, and is not known personally by Im Changsoo.",
    "Taekyung is a C-rank Hunter rather than the F-rank Hunter the restaurant owner believed him to be, and he can use the Jin Family's Cultivation Technique to perform Circulate Qi for Healing on others.",
    "Hayeon and Kim Jeonghee recovered substantially after receiving Circulate Qi for Healing from Taekyung; Hayeon also asked whether she could drop out of school after learning about his raid earnings.",
    "Taekyung's reality and Murim Inventories are separate.",
    "Peace Guild's Guild house remodeling is scheduled to finish in one week, and Taekyung is on paid vacation until then.",
    "Choi Minwoo and Butler Kim suspect that Taekyung may be a third-awakening Hunter; Butler Kim will investigate.",
    "Sangdong Guild is monitoring Peace Guild and has marked Taekyung as a major target; Choi has not warned him because he wants Sangdong's investigation to reveal more.",
    "Taekyung agreed to buy a meaningful former family home for 3.38 billion won, paid a ten-percent deposit, and plans to remodel it and move after Hayeon's college entrance examination.",
    "Park Jihwang changed his name to Park Jihoon and is now a Hunter in Team 1 of Myeongdong Guild.",
    "Taekyung judged Jihoon's strength to be comparable to Im Changsoo's, possibly greater.",
    "Hong Woojin is a B-rank mage and information broker who specializes in tracking and surveillance magic.",
    "Woojin is investigating Taekyung through a cat's Link; Taekyung's Qi Sense did not detect the surveillance, though Woojin nearly exposed himself."
  ],
  "continuity_sources": [
    91
  ],
  "open_questions": [
    "Whether Im Chunsoo or Sangdong Guild will retaliate against Peace Guild remains unresolved.",
    "What will happen to Kim Jeonghee after leaving the restaurant remains unresolved.",
    "Whether Hayeon will actually drop out of school remains unresolved.",
    "Whether third-awakening Hunters exist and whether Taekyung is one remains unresolved.",
    "Why Hong Woojin is investigating Taekyung and what information he seeks remains unresolved."
  ],
  "safe_through": 91,
  "temporary_decisions": [
    "Use Frozen for 프로즌 and preserve the tiger-father/dog-son wordplay in 호부견자.",
    "Use ajumma for 아줌마 and goshiwon for 고시원, each with an explanatory footnote.",
    "Use Minsu for 민수.",
    "Render 운기요상 as Circulate Qi for Healing and 하급 포션 as Lesser Potion.",
    "Render 3차 각성자 as third-awakening Hunter and 3차 각성 as third awakening.",
    "Render 피의 일주일 as Bloody Week and 전세 as jeonse lease.",
    "Render 사장님 as Boss in the real-estate context, including young Boss.",
    "Render 박지황/박지훈 as Park Jihwang/Park Jihoon, and 삼계탕 as samgyetang with an explanatory footnote."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 임춘수    | **Im Chunsoo**    |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 정파     | **orthodox faction**                             |                                                       |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 평화 | **Peace Guild** | Guild name. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |

## Listed compact profiles

### Im Chunsoo.md

# Im Chunsoo (임춘수)

- **Safe through:** Chapter 86
- **Aliases:** Frozen
- **Role:** A-rank Hunter; founder and Guild Master of Sangdong Guild; renowned ice mage
- **Personality:** Intimidating, severe, and extremely short-tempered, though he has tried to moderate his temper with age
- **Voice:** Sharp and commanding, with a comparatively gentle tone when deliberately controlling his temper; becomes violently profane when enraged
- **Relationships:** Father of Im Changsoo, whom he considers a pathetic disappointment and immediately fires and punishes after learning of Changsoo's actions

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 91
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

## Korean source

```text
＃92화



[표적 보고서]

이름 : 진태경

나이 : 27

거주지 : 주소지 xxx-xxx 희망 고시원. 가족과 별거 중.

가족관계 : 1남 1녀 중 장남. 11년 전 아버지 사고사. 어머니와 여동생에 관한 정보는 따로 첨부.



조사를 지시한 지 사흘 만에 받아 보는 보고서다. 다섯 장에 걸쳐 빽빽하게 적힌 정보들을 읽은 임춘수가 입을 열었다.

“야, 1팀장아.”

“예, 길드장님.”

맞은편에 앉아 있던 1팀장이 대답했다. 길드장인 임춘수를 제외하면 상동 길드 유일한 A급 헌터이자 임춘수의 충직한 오른팔이다.

“이 보고서, 읽어 봤냐?”

“아직 안 읽어 봤습니다.”

“왜?”

“길드장님 지시니까요. 추후 들어오는 정보는 중간에서 거르지 말고 그대로 보고하라고 하셨습니다.”

“그럼 이참에 읽어 봐.”

임춘수가 내미는 보고서를 공손히 받아 든 1팀장의 눈동자가 바삐 움직였다. 10분 정도 후, 고개를 든 그가 중얼거렸다.

“이건 좀.”

“그 보고서, 어떻게 생각하냐?”

“전 길드장님 판단에 따를 뿐입니다.”

“아냐, 허심탄회하게 말해 봐.”

잠깐 망설이던 1팀장이 대답했다.

“정보가 잘못된 것 같습니다.”

“정확히 어떤 부분이?”

“보고서 대상인 진태경은 불과 보름 전까지 F급 헌터였습니다. 그러나 C급 헌터로 재각성에 성공했죠. 여기까지는 드문 일이긴 해도 불가능하진 않습니다.”

“계속.”

“하지만 임창수 팀장, 아니 임창수 헌터와 해당 레이드에 참여했던 인원들의 증언에 의하면 진태경은 B급 몬스터인 미노타우로스 무리를 단신으로 해치웠습니다.”

“최소 다섯 마리. 최대 열 마리였지, 아마?”

“네. 심지어 보스 몬스터는 일격에 쓰러트렸다고 했죠.”

“그래. C급 헌터 나부랭이가 미노타우로스 대전사를 한 방에. 이게 말이 되냐?”

“말이 안 된다고 생각합니다.”

“그럼 뭘까?”

결코 몰라서 물어보는 것이 아니다. 1팀장이 자신과 같은 생각을 하고 있는지 다시 한번 확인하는 과정일 뿐이다.

“의심이 가는 부분이 셋 있습니다.”

“읊어 봐.”

“첫째, 보고서가 잘못됐을 경우입니다.”

“이 보고서, 누가 작성한 거지? 홍, 홍 뭐였는데. 홍길동은 확실히 아니고.”

“홍우진입니다. 아직 젊고 경력은 얼마 되지 않았습니다만, 실력은 정평이 나 있습니다.”

“그래, 홍우진인지 홍길동인지 하는 그 새끼한테 다시 한번 확인해. 으름장도 좀 놓고. 아무튼 그래서 두 번째는?”

“둘째, 임창수 헌터와 다른 인원들이 입을 맞춰 거짓말을 한 경우입니다.”

“창수 그 녀석이 정신이 똑바로 안 박혀 있어서 그렇지, 살면서 나한테 거짓말 쳐 본 적이 없다. 계속.”

“마지막은 진태경이 아직 확인되지 않은 A급 헌터이거나 혹은…….”

침착하던 1팀장의 얼굴 위에 곤란한 빛이 스쳤다. 잠시 후, 그가 머뭇머뭇 입을 열었다.

“3차 각성자가 아닐까요?”

“3차?”

“……네.”

“1팀장아. 네가 말해 놓고도 황당하지? 3차 각성자가 말이 되냐, 응?”

1팀장은 고개를 숙이는 것으로 대답을 대신했다.

그 모습에 혀를 찬 임춘수가 보고서를 집어 들었다. 그의 손끝에서부터 극한의 냉기가 흘러나온다.

파스스슥. 차창!

“보고서 다시 작성해. 이번 주까지 끝마치고 월요일 출근할 때 책상 앞에 갖다 놔. 산뜻하게.”

“알겠습니다.”

“그리고 거, 누구야. 평화 길드인가 사랑 길드인가 거기 다른 놈들 관련 정보는 어떻게 됐어?”

“……저, 그에 관해서 지금 막 보고드리려고 했습니다만.”

“뭐야, 하나도 파악 안 됐어?”

“세 명 제외하고는 전부 파악 완료된 상태입니다.”

임춘수가 눈살을 찌푸렸다.

“세 명? 그중 하나는 진태경일 테고. 나머지 둘은?”

“평화 길드의 길드장과 팀장입니다.”

아들놈에게 들어 본 적이 있다. 팀장이라는 젊은 놈은 싸가지가 없고, 길드장이라는 장년인은 레이드 내내 허허 웃기만 하는 속없는 인간이라고.

“그놈들이 왜?”

“락(Lock)이 걸려 있었습니다.”

“뭐?”

“말씀드린 그대롭니다. 개인 정보는 물론이고 계좌 관련해서까지 모두 보안 상태라 감찰팀에서도 당혹스러워하고 있습니다.”

“돈 아꼈냐?”

길드를 운영하려면 기관의 도움이 필요하다. 각 기관에 근무하는 타락한 공무원들은 뇌물을 받고 정보를 넘겨주는 걸 주저하지 않는다.

“안 그래도 듬뿍 안겨 줬는데…….”

“그랬는데?”

“그쪽에서도 좀 꺼리는 기색이 역력합니다. 그쪽 말로는 상부 기관에서 보안을 걸어 놔서 건드리기가 어렵다더군요.”

임춘수는 황당했다.

만들어진 지 한 달도 안 된 길드. 길드원을 다 합쳐 봐야 레이드 팀 하나도 안 나오는 소규모 길드다. 아니, 그 정도면 길드가 아니라 친목회라고 해도 이상하지 않다.

그런데 그깟 놈들이 뭐라고 락이 걸려 있단 말인가?

“허, 이 자식들 봐라.”

“어떻게 할까요?”

“일단 그 부분은 더 깊게 파지 말고 내버려 둬. 이번에 돈 찔러 준 놈들 입단속도 확실히 하고.”

대격변 시절, 불같은 성격으로 유명했던 임찬수는 길드를 운영하면서 중요한 한 가지를 배웠다.

목표를 이루기 위해서는, 그리고 목표 이상의 성과를 얻기 위해서는 침착하고 신중해야 한다는 것이다.

“그럼 그 셋 빼고는 전부 파악 끝났지?”

“네, 완벽합니다.”

철두철미한 성격으로 신임을 얻은 1팀장의 말이다. 임춘수는 고개를 끄덕였다.

“보안 걸려 있다는 두 놈은 방금 내가 말한 대로 조치하고. 우선 진태경 그놈만 집중적으로 파. 길드 감사팀 몇 명 동원해서 따로 감시 인원 늘리고.”

“따로……말입니까?”

“그래, 보고서 상태 보니까 영 아니야. 생각해 보면 우리 길드 감사팀도 뭐, 딱히 밀릴 거 없잖아?”

“그렇긴 합니다만.”

1팀장이 순간 멈칫했다. 의뢰를 하러 갔을 때 홍우진이 신신당부했던 말이 생각나서였다.



‘이 의뢰, 받는 순간 이거 내 일 되는 겁니다. 알죠? 일주일 안에 이 새끼 그날 입은 팬티 색까지 알아낼 테니까 믿고 맡겨요. 괜히 그쪽에서 일 벌렸다가 감시 대상이 눈치 까면 내 일 망치는 거니까.’



경력은 짧아도 일 잘한다고 알음알음 입소문이 나 있는 홍우진이다. 말투는 건방졌지만 프로다운 모습에 신뢰가 갔고, 직접 약속까지 했다.

‘말씀드려야 할 것 같은데.’

하지만 1팀장이 꺼내려던 반대 의견은 임춘수의 한마디에 목구멍 안으로 쏙 돌아갔다.

“왜? 더 할 말 있어?”

“아, 아닙니다. 그대로 전달하겠습니다.”

“그래, 가 봐.”

요즘 임춘수의 기분이 좋지 않다. 최대한 비위를 맞춰 주면서 좋은 방향으로 이끌어 가는 것이 그의 일이다.

‘괜찮겠지? 괜찮을 거야.’

1팀장은 길드장실을 나오면서도 찝찝한 기분을 감추지 못했다.



* * *



집, 휴가.

이 두 단어는 생각만으로도 행복감을 준다. 실제로도 그랬고. 그런데…….

왜앵. 왜애애애앵.

“아오, 미치겠네.”

나는 전광석화 같은 속도로 파리를 후려쳤다. 평범한 손바닥도 아닌 공력이 실린 손바닥이다. 일격에 즉사한 파리를 쓰레기통에 버리고 소파로 돌아왔다.

“뭔 놈의 파리 새끼들이 이렇게 많아?”

물을 마시려고 잠깐 거실로 나온 하연이가 한숨을 푹 내쉬었다.

“여름이니까 그렇지, 오빠 바보야?”

“그 정도가 아니라니까, 지금.”

“뭐 많아 봤자 얼마나 많다고. 방금도 한 마리밖에 없었잖아.”

“한 마리씩 계속 들어오니까 문제지. 잡는 족족 어디서 자꾸 들어오네.”

“몇 마리나 잡았는데?”

“하늘에 맹세코 오전부터 지금까지 100마리는 잡았다.”

“과장하는 것 봐. 이래서 남자들이란…….”

“진짜라고!”

“알았어, 알았어.”

와, 미치겠네. 나는 머리를 쥐어뜯으며 새로운 파리를 때려잡았다. 백 마리? 결코 과장이 아니다. 이놈의 동네는 어떻게 되었길래 한 집에 파리가 이렇게 들끓을 수 있지?

‘창문에 꿀이라도 발라 놨나.’

처음에는 그냥 거슬리는 정도였다. 앞서 하연이가 말했던 것처럼 여름이니까 당연한 현상이라고 생각했다.

하지만 갈수록 뭔가 이상하다는 걸 깨달았다.

‘한 30마리쯤 잡은 후였지.’

이 염병할 것들이 쉬지 않고 들어온다! 한 놈을 잡으면 또 한 놈이, 그놈을 잡으면 다른 놈이 들어와서 자리를 잡았다.

집 안의 모든 창문을 닫고 기감으로 수색 작업까지 거쳤음에도 파리 군단의 악몽은 이어졌다.

왜애애앵.

“저거 봐, 그새를 못 참고 또 한 마리 들어오잖아. 이놈들 도대체 어디서 들어오는 거야?”

미처 발견 못 한 미세한 틈 같은 게 있나 꼼꼼하게 살펴봤지만 나로서는 도저히 알 수 없었다. 말 그대로 개미 새끼 한 마리 통과할 만한 공간에서 들어오는 듯싶었다.

“때려잡지 말고 가만히 둬. 그럼 조용해지니까.”

“그게 무슨 창의적인 헛소리냐. 가만히 둔다고 쟤들이 가만히 있어? 왱왱 하는 소리에 잠도 못 잘 게 뻔한데.”

“내 방 파리는 가만히 있던데?”

“뭐?”

“내 방에도 한 세 마리 정도 있다고. 처음에는 신경 쓰여서 잡을까 했는데, 가만히 두니까 안 날아다니고 가만히 책상에 앉아 있어.”

“그거야 잠깐이고. 너 안 보는 사이에 엄청 날아다닐걸.”

“그냥 좀 게으른 파리들인 것 같던데. 한 번도 안 움직였어.”

“말이 되는 소리를 해라.”

“진짜라니까. 10만 원 내기 콜?”

“10만 원은 있냐? 수험생 주제에.”

“당연히 있지. 지난번에 오빠한테 받은 거.”

“나한테 받은 용돈으로 나랑 내기를 하겠다고?”

“쫄리면 뒈지시든지.”

“……콜.”

시바, 돈이 이렇게 돌고 도는구나. 우리는 하연이의 방으로 곧장 직행했다. 얌전히 앉아 있는 파리 한 마리를 가리키며 녀석이 의기양양하게 웃는다.

“봤지? 내 말이 맞지? 빨리 10만 원 내놔.”

“내놓긴 뭘 내놔. 실험을 해 봐야지.”

나는 파리 위로 손바닥을 내리쳤다. 딱 일반인 수준의, 파리가 충분히 피할 수 있는 속도였다. 그런데…….

움찔. 후다닥.

그 순간에 화들짝 놀라더니 다리를 바쁘게 놀려 도망치는 파리.

그 모습을 본 나는 황당함을 금치 못했다. 하연이도 저게 뭔가 하는 얼굴이다.

“동생아.”

“으, 응.”

“요즘 파리들은 다 저러냐?”

“그, 그럴 수도 있지 않을까? 아무튼 10만 원 줘.”

“줘야지. 주긴 주는데…… 저 파리 좀 이상하지 않아?”

“파리가 파리지. 그냥 좀 이상한 애 같은데.”

“저런 파리가 어디 있어. 내가 살면서 고블린에 미노타우로스는 봤어도 이렇게까지 안 날아다니는 파리는 처음 본다.”

말이 끝난 그 순간이었다.

왜애애앵-

“…….”

“…….”

수상해. 너무 수상해. 타이밍도 공교롭지만 마치 평범해 보이려고 애쓰는 듯한 날갯짓은 더 이상하다. 날아다니는 것도 뭔가 어설프게 비틀거리고.

‘그런 건 둘째치고 기분 나빠. 이 느낌 묘하게 익숙한데.’

어디서 비슷한 기분을 느꼈더라?

아, 그랬지. 이틀 전 집 보러 갔다가 돌아오던 그 골목길.

어쩐지 누군가 나를 감시하는 것 같은 기시감.

‘내가 진짜 예민한 건가.’

파리를 노려보던 내가 [기감]을 끌어 올렸다. 이제 반경 70미터에 이르는 기감의 발동 범위가 집 전체 구석구석으로 뻗어 나갔다.

그리고 아무도 예상치 못한 일이 일어났다.

띠링. 띠링. 띠링.



[Lv.1 집파리 – 패밀리어]

[Lv.1 검정파리 – 패밀리어]

[Lv.1 금파리 - 패밀리어]



“……?”

뭔데, 이거.
```

## Final English reading copy

```markdown
# Chapter 92

> **Target Report**
>
> **Name:** Jin Taekyung
>
> **Age:** 27
>
> **Residence:** Address xxx-xxx, Hope Goshiwon[^1]. Living separately from his family.
>
> **Family:** Eldest son in a family of one son and one daughter. Father died in an accident eleven years ago. Information on his mother and younger sister attached separately.

This was the report Im Chunsoo received three days after ordering the investigation. After reading through the densely packed information filling five pages, he opened his mouth.

“Hey, Team 1 Leader.”

“Yes, Guild Master.”

The Team 1 Leader seated across from him answered. Apart from Guild Master Im Chunsoo, he was the only A-rank Hunter in Sangdong Guild, as well as Im Chunsoo’s loyal right hand.

“Did you read this report?”

“Not yet.”

“Why not?”

“Because it was your order, Guild Master. You told us to report any information that came in without filtering it along the way.”

“Then read it now.”

The Team 1 Leader politely accepted the report Im Chunsoo held out to him. His eyes moved rapidly across the pages. About ten minutes later, he raised his head and muttered,

“This is a little…”

“What do you think of the report?”

“I can only follow your judgment, Guild Master.”

“No. Speak frankly.”

After a brief hesitation, the Team 1 Leader answered.

“I think the information is incorrect.”

“Which part, exactly?”

“The subject of the report, Jin Taekyung, was an F-rank Hunter until only half a month ago. However, he succeeded in reawakening as a C-rank Hunter. That much is rare, but not impossible.”

“Go on.”

“But according to the testimony of Team Leader Im Changsoo—no, Hunter Im Changsoo—and the others who participated in that raid, Jin Taekyung single-handedly defeated a group of B-rank monsters, the Minotaurs.”

“Minimum five. Maximum ten, if I remember correctly?”

“Yes. They even said he brought down the boss monster with a single strike.”

“Right. A mere C-rank Hunter taking down a Minotaur Warrior with one blow. Does that make any sense?”

“I don’t think it does.”

“Then what is it?”

He was not asking because he genuinely did not know. He only wanted to confirm once again whether the Team 1 Leader was thinking the same thing he was.

“There are three things that concern me.”

“List them.”

“First, the report may be wrong.”

“Who wrote this report? Hong… What was it? Definitely not Hong Gil-dong.”

“Hong Woojin. He’s still young and doesn’t have much experience, but his ability is well known.”

“Right, that Hong Woojin—or Hong Gil-dong, or whatever the hell his name is. Check with that bastard again. Put some pressure on him, too. Anyway, what’s the second?”

“Second, Hunter Im Changsoo and the others may have coordinated their stories and lied.”

“Changsoo’s an idiot who can’t think straight, but he’s never lied to me in his life. Continue.”

“The last possibility is that Jin Taekyung is an A-rank Hunter whose strength has not yet been confirmed, or perhaps…”

A troubled look crossed the otherwise calm Team 1 Leader’s face. After a moment, he hesitantly opened his mouth.

“Could he be a third-awakening Hunter?”

“Third awakening?”

“…Yes.”

“Team 1 Leader. Doesn’t it sound absurd even to you? A third-awakening Hunter? Does that make any sense?”

The Team 1 Leader answered by lowering his head.

Im Chunsoo clicked his tongue at the sight and picked up the report. Extreme cold began to flow from his fingertips.

Crackle. Crash!

“Rewrite the report. Finish it by the end of this week and put it on my desk when you come in on Monday. Make it nice and clean.”

“Yes, sir.”

“And what about the information on the other people from that Peace Guild—or was it Love Guild?”

“……I was just about to report on that.”

“What? You haven’t found out anything?”

“We’ve finished identifying everyone except for three people.”

Im Chunsoo frowned.

“Three? One of them must be Jin Taekyung. Who are the other two?”

“The Guild Master and Team Leader of Peace Guild.”

He had heard about them from his son. The young Team Leader was an insolent brat, while the middle-aged Guild Master was a clueless man who had done nothing but chuckle throughout the entire raid.

“Why those two?”

“There was a Lock on them.”

“What?”

“Exactly as I said. Not only their personal information, but even their account details are all under security restrictions. The Audit Team is at a loss as well.”

“Did you skimp on the money?”

“Not at all. I already gave them plenty…”

“And yet?”

“They seem very reluctant on their end as well. They said an upper agency had placed the security lock, making it difficult for them to touch.”

Im Chunsoo was dumbfounded.

A Guild that had not even existed for a month. A small Guild whose entire membership could not even make up one raid team. No, at that point, calling it a Guild was strange. It would not have been odd to call it a social club instead.

And yet, who the hell were those bastards to have a Lock placed on them?

“Huh. Look at these bastards.”

“What should we do?”

“Don’t dig any deeper into that part for now. Leave it alone. And make absolutely sure the people we paid this time keep their mouths shut.”

During the Great Cataclysm, Im Chunsoo had been famous for his fiery temper. But after running a Guild, he had learned one important thing.

To achieve a goal—and to gain results beyond that goal—one had to remain calm and cautious.

“So everything else is completely investigated?”

“Yes. Completely.”

That was the answer of the Team 1 Leader, who had earned Im Chunsoo’s trust through his meticulous nature. Im Chunsoo nodded.

“Deal with those two locked targets as I said. For now, focus only on Jin Taekyung. Mobilize a few people from the Guild Audit Team and increase the surveillance separately.”

“Separately…?”

“Yes. Looking at the state of this report, it’s no good. When you think about it, our Guild Audit Team isn’t exactly outclassed, is it?”

“That’s true, but…”

The Team 1 Leader suddenly hesitated. He remembered what Hong Woojin had repeatedly stressed when he went to commission Woojin for the job.

> “The moment I accept this assignment, it becomes my job. Got it? Within a week, I’ll find out the color of this bastard’s underwear on the day in question, so leave it to me. If you cause trouble on your end and the surveillance target catches on, you’ll ruin my job.”

Hong Woojin had little experience, but word had spread that he was good at his work. Despite Woojin’s arrogant way of speaking, his professionalism had inspired trust, and the Team 1 Leader had personally given him his word.

*I should probably tell him.*

But the objection the Team 1 Leader was about to raise went straight back down his throat at Im Chunsoo’s next words.

“Why? Is there something else you want to say?”

“Oh, no, sir. I’ll relay it exactly as you said.”

“Good. You can go.”

Im Chunsoo had been in a bad mood lately. It was the Team 1 Leader’s job to keep him appeased as much as possible and guide him in a favorable direction.

*It’ll be fine, right? It will be.*

Even after leaving the Guild Master’s office, the Team 1 Leader could not shake his uneasy feeling.

* * *

Home. Vacation.

Just thinking about those two words made me happy. And in reality, it was just as wonderful. But…

Bzzzz. Bzzzzzz.

“Ah, this is driving me crazy.”

I swatted at a fly with lightning-fast speed. It was not an ordinary palm strike, either—my palm was charged with internal energy. After killing the fly instantly, I tossed it into the trash and returned to the sofa.

“Why the hell are there so many flies?”

Hayeon, who had briefly come out into the living room to get a drink of water, let out a deep sigh.

“It’s summer, you idiot, Oppa.”

“It’s not just that.”

“What’s the big deal? How many could there be? There was only one just now.”

“That’s the problem. They keep coming in one at a time. Every time I catch one, another one keeps coming in from somewhere.”

“How many have you caught?”

“I swear to heaven, I’ve caught at least a hundred since this morning.”

“Look at you exaggerating. This is why men are…”

“I’m serious!”

“Okay, okay.”

Damn, this was driving me crazy. I tore at my hair and swatted down another fly. A hundred? I was not exaggerating at all. What had happened to this neighborhood that so many flies could swarm into one house?

*Did someone smear honey on the windows?*

At first, they had only been annoying. Just like Hayeon had said, I thought it was a normal phenomenon because it was summer.

But the more time passed, the more I realized that something was strange.

*It was after I’d killed about thirty of them.*

These damn things kept coming in without a break! I would kill one, then another would come in. I would kill that one, and a different fly would take its place.

Even after closing every window in the house and searching with my Qi Sense, the nightmare of the fly army continued.

Bzzzzzz.

“See? Another one came in before we could even turn around. Where the hell are these things coming from?”

I carefully searched for some tiny gap I had failed to notice, but I could not figure it out. They seemed to be coming through spaces barely large enough for a single ant to pass through.

“Don’t swat them. Just leave them alone. Then they’ll quiet down.”

“What kind of creative bullshit is that? You think they’ll stay still just because you leave them alone? We won’t be able to sleep with all that buzzing.”

“The flies in my room stay still.”

“What?”

“There are about three in my room, too. They bothered me at first, so I thought about killing them, but when I left them alone, they stopped flying around and just sat on my desk.”

“That’s only temporary. They must fly around like crazy when you’re not looking.”

“I think they’re just lazy flies. They haven’t moved even once.”

“Say something that makes sense.”

“I’m serious. Want to bet a hundred thousand won?”

“You even have a hundred thousand won? You’re an examinee.”

“Of course I do. It’s from the money you gave me last time.”

“You’re going to bet against me with the allowance I gave you?”

“If you’re scared, you can just die.”

“……Deal.”

Shit. So this was how money went around in circles.

We went straight to Hayeon’s room. She pointed at a fly sitting quietly in place and grinned triumphantly.

“See? I was right, wasn’t I? Hand over the hundred thousand won.”

“Hand over what? We need to run an experiment first.”

I brought my palm down over the fly. I struck at an ordinary person’s speed, slow enough for the fly to dodge easily. But then…

Flinch. Scramble.

The fly startled violently and scurried away, moving its legs as fast as it could.

I could not hide my bewilderment. Hayeon wore a similar expression.

“Sis.”

“Y-Yeah?”

“Are all flies these days like that?”

“Th-They could be, couldn’t they? Anyway, give me the hundred thousand won.”

“I’ll give it to you. I will. But isn’t that fly strange?”

“A fly is a fly. It’s just a weird one.”

“What kind of fly acts like that? I’ve seen goblins and Minotaurs in my life, but I’ve never seen a fly that flies around so little.”

The instant I finished speaking—

Bzzzzzz—

“……”

“……”

Suspicious. Extremely suspicious.

The timing was questionable enough, but the way its wings moved—as if it were trying hard to look ordinary—was even stranger. Even its flight was awkward and unsteady.

*Forget that. It gives me the creeps. This feeling is weirdly familiar.*

Where had I felt something similar?

Oh, right. That alley I had walked through on the way home two days ago, after looking at a house.

That déjà vu of someone secretly watching me.

*Am I really just being oversensitive?*

I glared at the fly and raised my Qi Sense. Its activation range now extended to a radius of seventy meters, spreading into every corner of the house.

And then something no one could have expected happened.

Ding. Ding. Ding.

> **System**
>
> Lv. 1 Housefly—Familiar
>
> Lv. 1 Black Blow Fly—Familiar
>
> Lv. 1 Green Bottle Fly—Familiar

“……?”

*What the hell is this?*

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.
```
