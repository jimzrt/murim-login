<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0097.txt",
      "sha256": "47cd7a57c0efba870de3589294e3e1d5724f62125774c81096a2a00595951af4",
      "bytes": 13395
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b835960bc892bcc0add39da1e713ead480f80b016f6efa75fcc8f15cdf018ff9",
      "bytes": 2158
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8c5e8b96be5f9aca3aea3f792b4623838a9f9dfb15b8e5d04288a0abbb919749",
      "bytes": 11955
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "05560f435ee6bc5b971840e31e29d94177d97f261f717fd5135cb4b18495cd7f",
      "bytes": 23942
    },
    {
      "path": "characters/Kim Gwondong.md",
      "sha256": "0b3216d2c3360b01d17dfa898cbbedf9c2371a93290d74d0b26a5dcf087886f4",
      "bytes": 629
    },
    {
      "path": "characters/Kim Junsu.md",
      "sha256": "8d89d186e688d054e7d7f6d7050fbba0647f833c1ed097f9a49a7e68e8a9beb8",
      "bytes": 594
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c14266bd1b9cc707a7cb00f34b09cd2053752cefc7553737bd0e8e6cf456a630",
      "bytes": 10403
    }
  ],
  "estimated_tokens": 14756
}
-->

# Durable State Update — Chapter 97

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 97. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 97. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 97,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 97,
    "continuity_sources": [97],
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
    "Sangdong Guild’s Security Team is monitoring Jin Taekyung with its sole Familiar mage, Kim Junsu, and multiple C-rank stealth and tracking Hunters.",
    "Kim Junsu is a C-rank mental mage who uses Familiars and is suffering from exhaustion and anxiety about his hair loss.",
    "Kim Gwondong is a C-rank Security Team Hunter assigned to surveillance and disguises himself as a friendly neighbor.",
    "The Security Team has been watching Taekyung for days and has installed eavesdropping-magic Equipment in two nearby real-estate offices.",
    "The Security Team uses a black Lv. 2 Cat Familiar to track Taekyung after he leaves home.",
    "Taekyung detects the black kitten as a Familiar, identifies the disguised neighbor as Lv. 42 Kim Gwondong, and concludes that the two actors are not working together.",
    "The Security Team Leader wants to demonstrate that his team is superior to Hong Woojin and impress the Guild Master before the upcoming personnel reshuffle.",
    "The Security Team Leader believes Taekyung is an ordinary C-rank Hunter and dismisses Im Changsoo’s claim that Taekyung cleared a B-rank Gate alone.",
    "Taekyung enters the real-estate office while Sangdong Guild’s Security Team maintains full surveillance readiness."
  ],
  "continuity_sources": [
    96
  ],
  "open_questions": [
    "Why did Sangdong Guild’s Guild Master issue a special warning about Taekyung?",
    "Whether Taekyung’s conclusion that the black Familiar and Kim Gwondong are unrelated is correct remains unresolved.",
    "Whether the Security Team’s operation and Hong Woojin’s investigation share the same commissioning chain remains unresolved."
  ],
  "safe_through": 96,
  "temporary_decisions": [
    "Render 정신계 마법사 as mental mage and 보안팀 as Security Team.",
    "Use Kim Junsu, Kim Gwondong, Nabi, and Goyang for 김준수, 김권동, 나비, and 고양시.",
    "Render 개냥이 as dog-cat with an explanatory footnote.",
    "Use target, Familiar, Link, and eavesdropping-magic Equipment for 표적, 패밀리어, 링크, and 도청 마법 장비."
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
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |

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
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 96
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

### Kim Gwondong.md

# Kim Gwondong (김권동)

- **Safe through:** Chapter 96
- **Aliases:** None
- **Role:** Level 42 C-rank Hunter in Sangdong Guild’s Security Team, specializing in surveillance and disguise.
- **Personality:** Cautious, observant, pragmatic, and cynical about his superior’s orders and accountability.
- **Voice:** Friendly and ordinary while acting as a neighbor; deferential aloud to his Team Leader and profane internally.
- **Relationships:** Works under the unnamed Security Team Leader and cooperates with Kim Junsu and the other surveillance Hunters.

### Kim Junsu.md

# Kim Junsu (김준수)

- **Safe through:** Chapter 96
- **Aliases:** None
- **Role:** C-rank Hunter in Sangdong Guild’s Security Team; the Guild’s sole Familiar mage and a rare mental mage.
- **Personality:** Exhausted, anxious about his worsening hair loss, dutiful, and privately profane about his workload.
- **Voice:** Polite and restrained aloud; internally self-pitying, sarcastic, and profane.
- **Relationships:** Works under the unnamed Security Team Leader alongside Kim Gwondong and other surveillance Hunters.

## Korean source

```text
＃97화



“어머, 어서 오세용.”

40대로 보이는 아주머니가 콧소리와 함께 나를 맞이했다.

집에서 가까운 부동산이라 그런가? 가끔 집에 올 때 얼핏 스쳐 갔던 얼굴 같기도 하다.

“젊은 분이 오셨네. 뭐 마실래요? 커피? 율무차? 콜라?”

“커피로 주세요.”

“블랙, 프림, 아니면…….”

“블랙이요.”

“총각이 커피 마실 줄 아네.”

쉴 새 없이 다다다 쏘아 대는 말을 한 귀로 흘리며 자리에 앉았다. 수다스러운 부동산 아줌마보다 더 신경 써야 할 곳이 있었기 때문이다.

‘이건…….’

부동산 내부에 흐르고 있는 익숙한 기운.

바로 마나(Mana)다.

‘도청 마법인가?’

사장이 설치해 놓은 보안 마법일 확률은 거의 없다. 집도 아니고 부동산에 비싼 마법 제품을 둘 리는 없으니까.

나를 감시하는 놈들이 미리 손을 쓴 게 분명했다.

‘뭐, 충분히 예상했던 일이지.’

패밀리어까지 쓰는 놈들이니 도청 마법 정도야 애교다.

문제는 도대체 놈들이 몇 명이며 어디 있냐는 건데…….

“자아, 커피 나왔습니다.”

나는 예의 바른 웃음을 지으며 커피잔을 받았다.

“아, 감사합니다.”

감사하다는 말은 진심이다.

지금부터 놈들의 근거지를 알려 줄 사람이니까.



* * *



- 그래서, 우리 잘생긴 사장님은 어떻게 오셨을까?

- 집 좀 알아보려고요.

도청 마법이 전달해 주는 음성은 또렷했다. 잠시 패밀리어 마법을 해제한 김준수와 또 다른 팀원, 보안팀장은 약속이나 한 듯이 서로를 바라봤다.

“저놈 얼마 전에도 부동산 가지 않았냐?”

“네, 고양시 쪽으로 갔었죠. 그때는 저희가 투입되기 전이라 1팀장님이 홍우진한테 정보 받아서 넘겨주셨고.”

“준수 말이 맞습니다. 나중에 저희가 부동산 찾아가서 캐 보니까 계약금까지 걸고 왔더라고요.”

“쟤 계좌에 지금 얼마 들어 있지?”

진태경의 계좌 현황은 이미 훤히 알고 있는 보안팀이다.

보안팀장의 말에 팀원이 재빨리 태블릿을 꺼내 보고서를 띄웠다.

“약 37억 정도 됩니다. 이 중에 30억 원은 새로운 집 매입 비용으로 나갈 거고요.”

“그거, 구입하는 거 확실해?”

“조만간 집주인이랑 날 잡아서 계약한다는 말까지 들었으니까 구입할 생각인 건 확실합니다. 조사해 보니 표적이 어릴 때 살던 동네라서 좀 각별한 의미가 있는 것 같더군요.”

“그렇단 말이지…….”

보안팀장은 눈살을 찌푸렸다.

곧 새로운 집에 전 재산의 대부분을 쏟아부을 놈이다. 그런데 이제 와서 이 동네에 무슨 집을 또 알아본단 말인가?

‘심지어 길드도 부천에 있고.’

무슨 생각인지는 몰라도 어쩐지 찝찝한 기분이다.

“야, 소리 좀만 더 키워 봐.”

“옙.”

세 사람의 귀에 이어지는 대화가 흘러 들어온다.

- 원하는 조건이 어떻게 되시는데?

- 월세 아니면 전세요.

- 몇 개 있긴 한데…… 알다시피 이 동네가 안전 구역에 걸쳐져 있어서 좀 비싸.

- 괜찮아요. 저 헌터거든요.

- 어머, 헌터였어? 어쩐지 몸 좋더라니. 등급이 어떻게 돼? 아, 이런 거 물어보면 좀 주책인가?

- 뭐 그럭저럭? 별로 안 높아요. C급.

- 어머, 어머. 돈 잘 벌겠네. 팔뚝 한 번 만져 봐도 돼? 오호호!

- 하하, 매물 좋은 거 보여 주시면 생각해 볼게요. 아니, 아예 싹 다 보여 주세요. 전세고 매매고 마음에 드는 거 있으면 사 버려야지.

듣고 있던 세 사람은 기가 찼다.

“이 새끼 아주 신났네. 신났어.”

“오죽하겠습니까. F급으로 살다가 재각성 후 목돈 턱턱 들어오니까 가오가 확 살겠죠.”

“음, 그렇지. 한창 그럴 때지.”

다들 경험해 봐서 안다. 새로운 세계에 발을 디딘 저 기분.

비싸서 쳐다보지도 못하던 명품이 우습게 느껴지고 사람들의 보는 눈이 달라진다.

“저 자식이 딱 그 상태네, 지금.”

“마음에 드는 게 있으면 사긴 개뿔이. 계약한 집 잔금 치르면 네 잔고로는 전세가 고작이다, 이놈아.”

“그래도 부럽네요. 쟤는 뭐 먹고 머리털이 저렇게 풍성하지?”

진태경의 치기 어린 언행들을 지켜보고 있자니 한심하면서도 피식 실소가 새어 나온다.

어느새 세 사람의 마음이 느슨하게 풀어졌다. 귀는 열려 있지만 라디오 방송을 듣는 기분이다.

- 여기 어때요? 전세로 하면 5억 정도? 안전 구역인 거 감안하면 시세보다 훨씬 저렴하게 내놓은 거야.

- 괜찮네요. 다른 곳은 없어요?

- 왜 없겠어, 당연히 있지. 방금 보여 준 곳 바로 옆옆 동에 매물 있는데…… 아, 여긴 얼마 전에 나갔었네. 월세였는데 조건이 워낙 좋아서.

- 아, 그래요?

- 응. 총각이 며칠만 더 일찍 왔어도 건지는 건데. 관리가 잘 안 되어 있는 대신에 월세가 쌌거든. 뭐 그거야 돈 있으면 리모델링으로 해결할 수 있는 문제니까.

- 그거 아쉽네요.

- 나도 아쉬워. 웬 무섭게 생긴 아저씨가 와서 무슨 명령조로 얘기하더라니까? 지가 나한테 집을 맡겨 놨나…… 나도 기왕이면 젊고 잘생긴 총각한테 넘기는 게 기분 좋잖아. 그치?

- 어휴, 완전 꼰대였나 보네요.

- 조폭인가 싶어서 찍소리 못 했지. 몸에서도 홀아비 냄새가 진동을 해서 아주 죽는 줄 알았어. 호호호.

빠드득.

옆에서 들려오는 이 가는 소리. 김준수와 팀원은 터져 나오려는 웃음을 꾹 억눌렀다.

‘팀장이네.’

‘팀장이야.’

조폭 같은 인상에 홀아비 냄새. 여기까지만 들어도 보안팀장이란 사실을 알 수 있다.

인상이 어찌나 험악한지, 그가 처음 상동 길드에 입사했을 당시 면접관이 무서워서 더 볼 것도 없이 뽑았다는 소문도 있을 정도다.

“저 아줌마가 미쳤나…….”

이를 바득바득 갈던 팀장이 고개를 홱 돌렸다. 웃음을 참느라 얼굴이 벌겋게 달아오른 두 사람이 황급히 고개를 숙였다.

“참느라 힘들어 보인다?”

“아, 아닙니다.”

“그런 사실 없습니다.”

애써 부정해 보지만 이미 빈정이 상할 대로 상한 팀장은 자리에서 일어났다. 40대 중반의 솔로인 그에게 있어 홀아비라는 말은 결코 건드려서는 안 되는 부분이었다.

“홀아비 냄새 씻으러 사우나 다녀올 테니까 오는 즉시 볼 수 있도록 녹취록 작성해 놔.”

“예?”

김준수와 다른 팀원은 어이가 없었다.

부동산에서 허세 부리는 C급 헌터와 푼수 아줌마. 두 사람의 별것 없는 대화에 무슨 녹취록까지 작성한단 말인가.

“팀장님. 이거 다 자동으로 저장되고 있는…….”

“각자 소견서도 A4 용지 한 장 꽉 채워서 준비해. 중요한 표적이니까 팀원들 의견도 수렴해 봐야지.”

“…….”

“…….”

도대체 언제부터 팀원들 의견을 물어봤다고? 그리고 그 중요한 표적을 두고 팀장이란 양반이 사우나를 간다는 게 말이 되나.

속 좁은 상관의 화풀이에 두 사람의 표정이 일그러졌다.

“내 말 못 들었어? 복명복창한다, 실시!”

“……네.”

“……실시.”

“자식들이 빠져 가지고 말이야. 팀장 알기를 아주 개똥으로 알아요.”

부하들을 노려본 보안팀장이 씩씩거리며 방을 빠져나갔다.

쾅! 아파트 현관문 닫히는 소리에 남아 있던 두 사람이 동시에 참았던 말을 토해 낸다.

“아니, 시바.”

“이건 해도 해도 너무한 거 아니에요?”

“지 인상 더럽고 결혼 못 한 걸 왜 우리한테 화풀이하냐고.”

“인상만 더럽습니까? 아줌마 얘기 들어 보니까 명령조로 얘기했다잖아요. 인성까지 글러 먹은 거지.”

“나 참, 진짜 더러워서 못 해 먹겠네.”

“아, 진짜 스트레스받으면 안 되는데. 머리 더 빠지는데.”

물기 어린 목소리로 중얼거린 김준수가 정수리를 더듬었다. 모르긴 몰라도 잠깐 사이에 열 가닥은 빠진 것 같다.

“녹취록이랑 소견서, 어떡해요?”

“어떡하긴, 팀장 지랄하는 거 보기 싫으면 써야지. 병원 가서 진단 소견서 떼어 올래?”

“…….”

“대충 써, 대충. 패밀리어 마법 쓰느라 못 썼다고 옆에서 커버 쳐 줄 테니까.”

한숨을 푹 내쉰 두 사람은 본격적으로 팀장을 욕하기 시작했다. 그 와중에도 송신기 너머에서는 대화가 이어졌다.

- 괜찮네요. 남향이라 햇빛도 잘 들어오고. 그 옆 동은 어때요? 설마 여기도 나간 건 아니죠?

- 응? 아냐. 요즘 경기가 안 좋아서 최근에 나간 곳은…… 그런데 총각.

- 예?

- 팔뚝 진짜 단단하다. 세상에, 이 근육이랑 핏줄 도드라진 것 좀 봐.

- …….



* * *



“총각, 또 와. 두 번 와!”

아줌마의 아쉬움 섞인 배웅을 뒤로하고 부동산을 나섰다. 방금 그녀의 손길이 스친 팔뚝에는 닭살이 오소소 돋아 있다.

‘아줌마나 아저씨나, 철없이 나이 먹으면 젊은 애한테 치근덕거리는 건 비슷하다니까.’

끈적끈적한 눈빛에 도망치듯 자리를 떴지만 이미 부동산을 찾은 목적은 달성한 후라 별 미련은 없었다.

‘최근에 거래된 매물 확인.’

오늘은 임창수와의 레이드로부터 정확히 5일째 되는 날이다.

그 말인즉슨, 감시자들이 붙은 것은 아무리 빨라도 5일 안이라는 뜻이 된다.

‘나름 연기랍시고 티 나지 않게 돌려서 묻긴 했는데…….’

도청 마법의 존재를 아는 나로서는 다분히 의도적인 언행이었다. 허세와 사치로 똘똘 뭉친, 별거 없는 C급 헌터로 비치길 바랐으니까.

‘속아 넘어갔을지는 미지수지만.’

부동산 아줌마와의 대화는 중요한 단서였다. 나는 미리 외워 두었던 주소를 마음속으로 중얼거렸다.

‘5동 901호. 4동 302호. 3동 202호.’

이 세 곳이 최근 5일간 거래된 매물이다.

기준은 우리 집. 패밀리어 마법이 닿는 범위인 최대 500m로 잡았다. 감시자들은 분명 이 안에 있다.

‘문제는 어떻게 찾아내냐는 거지.’

내 목적은 놈들을 쫓아내는 게 아니라, 잡아서 족친 후에 배후를 알아내는 거다. 섣부르게 헛다리 짚었다가는 도주할 가능성이 있다.

‘자동차에 숨어 있을 가능성도 있으니까 주차장도 한번 살펴보고.’

근방의 집을 뒤지기 시작하면 낌새를 눈치채겠지만 주차장은 자연스럽게 수색할 수 있다.

산책하는 척 [기감]으로 훑어보면 게임 끝이지, 뭐.



[Lv.42 김권동]



“어, 또 만났네?”

그래, 이 아저씨처럼.

나는 알은체를 해 오는 김권동에게 인사를 건넸다.

“그러게요. 또 뵙네요.”

“부동산 가신다면서? 벌써 볼일 끝난 거야?”

“그냥 문의만 했어요. 그런데 막상 가서 알아보니까 집값이 만만치가 않더라고요. 바로 도망쳐 나왔죠.”

“이 동네가 다 그렇지, 뭐. 그래도 젊은 친구가 능력이 있네. 난 그 나이에 집에서 밥만 축냈는데.”

“능력이요? 하하.”

진짜 능력이 뭔지 알면 까무러칠걸.

내 속마음도 모른 채 따라 웃던 김권동이 입을 열었다.

“그럼 난 이만 갑니다. 저쪽 공원까지 돌고 와야 해서.”

“산책을 좋아하시나 봐요?”

“응? 그거야 좋아서 하는 게 아니라 필요해서 하는 거지. 그쪽도 내 나이 되면 힘들걸?”

보란 듯이 얇은 팔다리를 흔들어 보인다. 겉모습만 보면 마르고 배만 나온 중년 아저씨가 따로 없다.

‘민간인처럼 보이기는 하네.’

다른 사람이면 깜빡 속아 넘어갔을 모습이다.

하지만 42레벨이나 되는 민간인이 있을 리가 있나.

‘아마도 C급 헌터. 체형으로 봐서는 은신, 추격 계열.’

상대가 헌터라는 것만 알면 유추해 낼 수 있는 정보는 많다.

나는 김권동에게 인사했다.

“그럼 다음에 또 뵙죠.”

“그거야 볼 수도 있고, 못 볼 수도 있고. 하하.”

글쎄, 나는 꼭 보고 싶은데.

물론 그때는 지금처럼 하하 호호 웃으면서 헤어지진 않을 거다. 지금 당장이라도 때려눕히고 싶지만, 아직은 때가 아니었다.

꾸벅.

살짝 고개 숙여 인사하고 자리를 뜨려는데 등 뒤에서 그의 목소리가 들렸다.

“아, 맞다. 그 고양이 진짜 똑똑한 놈 같던데? 오는 길에 보니까 아직도 거기 있더라고.”

패밀리어를 잊지 말고 주워 가라는 친절한 안내 방송까지 해 준다.

그리고 그의 말처럼 고양이는 아까와 같은 곳에서 날 기다리고 있었다.

야옹.

그래. 형 왔다, 인마.
```

## Final English reading copy

```markdown
# Chapter 97

“Oh my, welcome!”

An ajumma who looked to be in her forties greeted me with a nasal sing-song.

Maybe it was because this real-estate office was close to home. Her face looked vaguely familiar, as though I had passed her by on my way home once or twice.

“Young man, what would you like to drink? Coffee? Yulmu tea?[^1] Cola?”

“Coffee, please.”

“Black, creamer, or…”

“Black.”

“Well, look at you. A young bachelor who knows how to drink coffee.”

I let her rapid-fire chatter go in one ear and out the other as I took a seat. There was another place I needed to pay more attention to than the talkative real-estate ajumma.

*This is…*

The familiar energy flowing through the real-estate office.

It was mana.

*Wiretapping magic?*

There was almost no chance it was security magic installed by the owner. Who would put an expensive magic product in a real-estate office instead of their home?

The people watching me had clearly made preparations in advance.

*Well, it was something I expected.*

They were using Familiars, after all. Wiretapping magic was the least of it.

The question was how many of them there were and where they were hiding…

“Here you go. One coffee.”

I accepted the cup with a polite smile.

“Ah, thank you.”

I meant that sincerely.

She was about to tell me where their base was.

* * *

—So, what brings our handsome boss here?

—I’m looking for a house.

The voice transmitted by the eavesdropping magic was perfectly clear. Kim Junsu, who had briefly deactivated his Familiar magic, exchanged a look with another team member and the Security Team Leader.

“Didn’t that bastard go to a real-estate office recently, too?”

“Yes. He went to Goyang. At the time, we hadn’t been assigned to him yet, so the Team 1 Leader got the information from Hong Woojin and passed it along.”

“Junsu’s right. We went to the real-estate office afterward and dug around a little. Apparently, he even put down a deposit.”

“How much money does he have in his account right now?”

The Security Team already knew Jin Taekyung’s account balance inside and out.

At the Security Team Leader’s question, a team member quickly pulled out a tablet and brought up the report.

“About 3.7 billion won. Three billion of that will go toward buying the new house.”

“Are you sure he’s going to buy it?”

“We even heard that he’s planning to set a date with the owner and sign the contract soon, so he definitely intends to purchase it. We looked into it, and apparently it’s the neighborhood where the target lived as a child. It seems to have some special meaning to him.”

“I see…”

The Security Team Leader frowned.

The man was about to pour most of his fortune into a new house. So why was he looking into another house in this neighborhood now?

*Even though his Guild is in Bucheon.*

Whatever he was thinking, the whole thing left an unpleasant feeling in the Security Team Leader’s gut.

“Hey, turn up the volume a little.”

“Yes, sir.”

The conversation continued to flow into the three men’s ears.

—What kind of conditions are you looking for?

—Either monthly rent or a jeonse lease.

—I do have a few, but… as you know, this neighborhood straddles a safety zone, so it’s a little expensive.

—That’s fine. I’m a Hunter.

—Oh my, you’re a Hunter? I knew you looked fit. What rank are you? Ah, is it rude of me to ask something like that?

—Somewhere around there. It’s not very high. C-rank.

—Oh my, oh my. You must make good money. Can I feel that arm? Oh-ho-ho!

—Ha-ha. Show me some good listings and I’ll think about it. No, show me everything. Jeonse, purchases, whatever. If I find something I like, I’ll just buy it.

The three men listening were dumbfounded.

“That bastard’s really enjoying himself.”

“Can you blame him? He lived as an F-rank Hunter, then after his reawakening, big chunks of money started rolling in. Of course his ego would swell.”

“Hmm, true. That’s the age for it.”

They all knew from experience. The feeling of stepping into a new world.

Luxury goods they had once been unable to look at because they were too expensive suddenly seemed laughable, and other people started looking at them differently.

“That bastard’s exactly like that right now.”

“‘If I find something I like, I’ll buy it,’ my ass. Once you pay the balance on the house you already contracted for, your account will barely cover a jeonse deposit, you idiot.”

“Still, I’m jealous. What does he eat to have such thick hair?”

Watching Jin Taekyung’s childish, cocky behavior was pathetic, but a quiet laugh escaped them anyway.

Before they knew it, the three men had relaxed. Their ears were still open, but they felt as if they were listening to a radio broadcast.

—How about this place? Around five hundred million won for a jeonse lease? Considering that it’s in a safety zone, it’s much cheaper than market price.

—Not bad. Are there any others?

—Of course there are. There’s another listing in the building two over from the one I just showed you… Oh, this one already went off the market. It was monthly rent, but the terms were exceptionally good.

—Oh, really?

—Yeah. If you’d come a few days earlier, young man, you could’ve snagged it. The place wasn’t well maintained, but the rent was cheap. Of course, if you have money, remodeling can solve that problem.

—That’s a shame.

—Tell me about it. Some scary-looking man came by and spoke to me in this commanding tone. Did he think I’d been entrusted with his house or something? I’d much rather hand it over to a young, handsome bachelor, you know. Right?

—Ugh, I guess he was a total old-fashioned jerk.

—I thought he might be a gangster, so I couldn’t so much as squeak. The smell of an old bachelor was practically pouring off him. I thought I was going to die. Ho-ho-ho.

Grrrind.

The sound of teeth grinding came from beside them. Kim Junsu and the other team member suppressed the laughter threatening to burst out.

*It’s the Team Leader.*

*It really is the Team Leader.*

A gangster-like impression and the smell of an old bachelor. Just hearing that much was enough to identify the Security Team Leader.

His expression was so frightening that there was even a rumor that when he first joined Sangdong Guild, the interviewer had been too scared to look any further and hired him on the spot.

“Has that ajumma lost her mind…?”

The Team Leader ground his teeth and whipped his head around. The two men, whose faces had flushed red from holding back their laughter, hurriedly lowered their heads.

“You two look like you’re having a hard time holding it in.”

“Oh, no, sir.”

“There’s no such thing.”

They tried desperately to deny it, but the Team Leader was already thoroughly offended. He stood up.

For a single man in his mid-forties, the words *old bachelor* touched on a subject that absolutely should not be touched.

“I’m going to the sauna to wash off this old-bachelor smell, so have the transcript ready for me to read as soon as I get back.”

“What?”

Kim Junsu and the other team member were dumbfounded.

A C-rank Hunter showing off at a real-estate office and a scatterbrained ajumma. Why would anyone write up a transcript of their completely unremarkable conversation?

“Team Leader, it’s all being saved automatically…”

“Prepare a full-page A4 statement of your individual opinions, too. He’s an important target, so we should gather the team’s input.”

“…”

“…”

Since when had he ever asked for their opinions? And how could it make sense for the Team Leader to go to a sauna while they were dealing with such an important target?

Their expressions twisted at the narrow-minded superior’s petty retaliation.

“Didn’t you hear me? Repeat the order back. Execute!”

“…Yes.”

“…Execute.”

“You bastards have gotten way too lax. You treat your Team Leader like dog shit.”

The Security Team Leader glared at his subordinates, snorted angrily, and left the room.

Bang!

The apartment’s front door slammed shut. The two men left behind immediately let out everything they had been holding in.

“Man, fuck this.”

“Isn’t this taking things way too far?”

“Why is he taking out the fact that he has an ugly face and can’t get married on us?”

“Is his face the only problem? That ajumma said he spoke in a commanding tone. His personality’s rotten, too.”

“This is so damn unpleasant. I can’t keep doing this.”

“Ah, I really can’t afford to get stressed out. It’ll make even more of my hair fall out.”

Kim Junsu muttered in a voice thick with tears and felt the top of his head.

He couldn’t be sure, but it seemed like at least ten hairs had fallen out in the last few moments.

“Then what do we do about the transcript and the statements?”

“What do you think? If you don’t want to watch the Team Leader throw a fit, you have to write them. Want to go to the hospital and get a medical statement?”

“…”

“Just write something rough. I’ll cover for you and say you couldn’t write because you were using Familiar magic.”

After letting out a deep sigh, the two men began cursing the Team Leader in earnest.

Even then, the conversation continued through the transmitter.

—It’s nice. Since it faces south, it gets plenty of sunlight. What about the building next to it? Don’t tell me that one’s gone, too?

—Huh? No, it’s still available. Business has been slow lately, so the places that went recently were… Wait, young man.

—Yes?

—That arm of yours is really solid. Goodness, look at those muscles and veins.

—…

* * *

“Young man, come again. Come twice!”

I left the real-estate office with the ajumma’s regretful farewell behind me.

Goose bumps had risen all over the arm her hand had just brushed.

*Whether it’s an ajumma or an ajusshi, people who grow old without growing up are all alike when it comes to hitting on younger people.*

I had escaped as if fleeing from her sticky gaze, but I had already accomplished my purpose in visiting the real-estate office, so I had no reason to linger.

*Confirm the listings that were recently sold or leased.*

Today was exactly five days after the raid with Im Changsoo.

That meant the surveillance team had been assigned to me no more than five days ago.

*I tried to act and ask about it indirectly without making it obvious, but…*

Knowing that eavesdropping magic was in place, I had deliberately behaved that way. I wanted to come across as an unremarkable C-rank Hunter packed full of arrogance and extravagance.

*Whether they fell for it or not was another matter.*

My conversation with the real-estate ajumma had given me an important clue. I repeated the addresses I had memorized in advance in my head.

*Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.*

These were the listings that had changed hands in the past five days.

I had used our house as the center point and set the range at a maximum of five hundred meters—the distance Familiar magic could reach.

The watchers were definitely somewhere within that range.

*The problem is how to find them.*

My goal wasn’t to drive them away. I wanted to catch them, beat the hell out of them, and find out who was behind them.

If I jumped at the wrong lead, they might realize what was happening and run.

*They could be hiding in a car, too, so I should check the parking lot.*

If I started searching the nearby houses, they would notice something was wrong. But I could search the parking lot naturally.

All I had to do was scan the area with Qi Sense while pretending to take a walk.

Game over.

> **System**
>
> **Lv. 42 Kim Gwondong**

“Oh, we meet again.”

Just like this man.

I returned Kim Gwondong’s familiar greeting.

“Indeed. We meet again.”

“You said you were going to the real-estate office. Are you done already?”

“I just asked a few questions. But when I actually went there and looked into it, the house prices weren’t exactly cheap. I ran right back out.”

“That’s how this neighborhood is. Still, you’re doing well for yourself, young man. At your age, I was just sitting at home eating my parents’ food.”

“Doing well? Ha-ha.”

If he knew what real ability looked like, he’d faint.

Kim Gwondong laughed along, unaware of my thoughts, then spoke.

“Well, I should be going. I need to walk as far as the park over there.”

“You must like taking walks.”

“Huh? It’s not that I do it because I like it. I do it because I need to. You’ll have a hard time too once you reach my age.”

He deliberately waved his thin arms and legs.

From the outside, he looked exactly like an ordinary middle-aged man who was skinny everywhere except for his protruding belly.

*He certainly looks like a civilian.*

Anyone else would have been fooled.

But there was no way a civilian could be Level 42.

*Probably a C-rank Hunter. Judging by his build, he’s probably specialized in stealth and pursuit.*

Once you knew someone was a Hunter, there was a lot you could infer.

I said goodbye to Kim Gwondong.

“Then I’ll see you next time.”

“That depends. We might run into each other, or we might not. Ha-ha.”

Well, I definitely wanted to see him.

Of course, when that happened, I wouldn’t be parting from him with a smile and a laugh like I was now. I wanted to knock him flat right then and there, but it wasn’t time yet.

I gave him a slight bow and turned to leave.

“Oh, right. That cat seemed awfully smart. I saw it on my way over, and it was still there.”

He had even given me a friendly reminder not to forget to pick up my Familiar.

And just as he said, the cat was waiting for me in the same spot as before.

“Meow.”

Right. Hyung’s here, you punk.

[^1]: Yulmu tea is a sweet Korean grain beverage made from roasted Job’s tears.
```
